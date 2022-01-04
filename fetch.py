"""Fetches calculation results from engine.py and returns a calcuation result object."""
from calculate import CalcResult
from config import CalcConfig
from engine import TaxableIncomeCalculator, PersonalAllowanceCalculator, TaxCalculator

def ask_salary():
    """Asks user for their gross yearly salary, and returns the integer value of it."""
    return int(input("What is your gross yearly salary?: "))

salary = ask_salary()

def calc_personal_allowance(config: CalcConfig) -> int:
    """Calculates personal allowance from engine.py using salary and config parameters."""
    calculator = PersonalAllowanceCalculator(salary, config.pa_threshold, config.base_pa)
    return calculator.calc()

def calc_taxable_salary(config: CalcConfig) -> int:
    """Calculates taxable salary from engine.py using salary and calls calc_personal_allowance."""
    calculator = TaxableIncomeCalculator(salary, calc_personal_allowance(config))
    return calculator.calc()

def calc_takehome_pay(config: CalcConfig) -> CalcResult:
    """Calculates take home pay from engine.py by calling calc_taxable_salary
    and using config parameters. Returns a CalcResult object.
    """
    calculator = TaxCalculator(calc_taxable_salary(config), config.tax_bands, config.tax_rates)
    tax_result = calculator.calc()
    return CalcResult(
        gross_pay = salary,
        tax_free_allowance = calc_personal_allowance(config),
        total_taxable = tax_result[0],
        total_tax_due = tax_result[1],
        tax_due = tax_result[2],
        net_pay = salary - tax_result[1]
    )
