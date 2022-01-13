"""Fetches calculation results from engine.py and returns a calcuation result object."""
from moneyed import Money

from calculate import CalcResult
from config import CalcMoneyConfig
from engine import (PersonalAllowanceCalculator, TaxableIncomeCalculator,
                    TaxCalculator)
from money import convert_to_money


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

salary = ask_salary()

def calc_personal_allowance(config: CalcMoneyConfig) -> Money:
    """Calculates personal allowance from engine.py using salary and config parameters."""
    calculator = PersonalAllowanceCalculator(salary, config.pa_threshold, config.base_pa)
    return calculator.calc()

def calc_taxable_salary(config: CalcMoneyConfig) -> Money:
    """Calculates taxable salary from engine.py using salary and calls calc_personal_allowance."""
    calculator = TaxableIncomeCalculator(salary, calc_personal_allowance(config))
    return calculator.calc()

def calc_takehome_pay(config: CalcMoneyConfig) -> CalcResult:
    """Calculates take home pay from engine.py by calling calc_taxable_salary
    and using config parameters. Returns a CalcResult object.
    """
    calculator = TaxCalculator(calc_taxable_salary(config), config.tax_bands, config.tax_rates)
    tax_result = calculator.calc()
    return CalcResult(
        gross_pay = salary,
        tax_free_allowance = calc_personal_allowance(config),
        total_taxable = tax_result.total_taxable,
        total_tax_due = tax_result.total_tax_due,
        tax_due = tax_result.tax_due,
        net_pay = salary - tax_result.total_tax_due
    )
