from config import CalcConfig
from engine import TaxableIncomeCalculator, PersonalAllowanceCalculator, TaxCalculator

def ask_salary():
    return int(input("What is your gross yearly salary?: "))

salary = ask_salary()

def calc_personal_allowance(config: CalcConfig):
    calculator = PersonalAllowanceCalculator(salary, config.pa_threshold, config.base_pa)
    return calculator.calc()

def calc_taxable_salary(config: CalcConfig) -> int:
    calculator = TaxableIncomeCalculator(salary, calc_personal_allowance(config))
    return calculator.calc()

def calc_takehome_pay(config: CalcConfig):
    """Asks user for gross salary and returns tax due and take home pay."""
    calculator = TaxCalculator(calc_taxable_salary(config), config.tax_bands, config.tax_rates)
    return calculator.calc()
