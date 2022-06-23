"""Fetches calculation results from engine.py and returns a calculation result object."""

from moneyed import Money

from src.calculate import CalcResult
from src.config import CalcMoneyConfig
from src.engine import (PersonalAllowanceCalculator, TaxableIncomeCalculator,
                        TaxCalculator, NationalInsuranceCalculator)
from src.money import convert_to_money

class CalculateTakeHomePay:
    """Composes Calculator classes to calculate take home pay and return a CalcResult."""
    def __init__(self, salary, config: CalcMoneyConfig):
        self.salary = salary
        self.personal_allowance: Money = Money(0, "GBP")
        self.national_insurance: Money = Money(0, "GBP")
        self.config = config

    def calc_personal_allowance(self) -> Money:
        """Calculates personal allowance from engine.py using salary and config parameters."""
        pa_calculator = PersonalAllowanceCalculator(
            self.salary, self.config.pa_threshold, self.config.base_pa)
        self.personal_allowance = pa_calculator.calc()
        return self.personal_allowance

    def calc_national_insurance(self) -> Money:
        """Calculates national insurance from engine.py using salary and config parameters."""
        ni_calculator = NationalInsuranceCalculator(
            self.salary, self.config.ni_bands, self.config.ni_rates)
        self.national_insurance = ni_calculator.calc()
        return self.national_insurance

    def calc_taxable_salary(self) -> Money:
        """Calculates taxable salary from engine.py using salary
        and calls calc_personal_allowance."""
        taxable_calculator = TaxableIncomeCalculator(
            self.salary, self.calc_personal_allowance())
        return taxable_calculator.calc()

    def calc_takehome_pay(self) -> CalcResult:
        """Calculates take home pay from engine.py by calling calc_taxable_salary
        and using config parameters. Returns a CalcResult object.
        """
        self.calc_national_insurance()
        tax_calculator = TaxCalculator(
            self.calc_taxable_salary(), self.config.tax_bands, self.config.tax_rates)
        tax_result = tax_calculator.calc()
        return CalcResult(
            gross_pay=self.salary,
            tax_free_allowance=self.personal_allowance,
            total_taxable=tax_result.total_taxable,
            total_tax_due=tax_result.total_tax_due,
            national_insurance=self.national_insurance,
            tax_due=tax_result.tax_due,
            net_pay=(self.salary - tax_result.total_tax_due - self.national_insurance)
            )
