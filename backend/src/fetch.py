"""Fetches calculation results from engine.py and returns a calculation result object."""

from moneyed import Money

from src.calculate import CalcResult
from src.config import CalcMoneyConfig
from src.engine import (PersonalAllowanceCalculator, TaxableIncomeCalculator,
                        TaxCalculator)
from src.money import convert_to_money


def check_if_float(value: str):
    """Return boolean indicating whether a string represents a float."""
    try:
        float(value)
        return True
    except ValueError:
        return False


def ask_salary() -> Money:
    """Asks user for their gross yearly salary, and returns the integer value of it."""
    while True:
        sal = input("What is your gross yearly salary?: ")
        if sal.isdigit() or check_if_float(sal):
            break
        print("Invalid input, please enter only numbers")
    return convert_to_money(sal)


class CalculateTakeHomePay:
    """Composes Calculator classes to calculate take home pay and return a CalcResult."""
    def __init__(self, salary, config: CalcMoneyConfig):
        self.salary = salary
        self.personal_allowance: Money = Money(0, "GBP")
        self.config = config

    def calc_personal_allowance(self) -> Money:
        """Calculates personal allowance from engine.py using salary and config parameters."""
        pa_calculator = PersonalAllowanceCalculator(
            self.salary, self.config.pa_threshold, self.config.base_pa)
        self.personal_allowance = pa_calculator.calc()
        return self.personal_allowance

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
        tax_calculator = TaxCalculator(
            self.calc_taxable_salary(), self.config.tax_bands, self.config.tax_rates)
        tax_result = tax_calculator.calc()
        return CalcResult(
            gross_pay=self.salary,
            tax_free_allowance=self.personal_allowance,
            total_taxable=tax_result.total_taxable,
            total_tax_due=tax_result.total_tax_due,
            tax_due=tax_result.tax_due,
            net_pay=self.salary - tax_result.total_tax_due
        )
