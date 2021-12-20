from config import CalcConfig
from engine import TaxCalculator

def ask_salary():
    return int(input("What is your gross yearly salary?: "))

def calc_takehome_pay(config: CalcConfig):
    """Asks user for gross salary and returns tax due and take home pay."""
    salary = ask_salary()
    calculator = TaxCalculator(salary, config.tax_bands, config.tax_rates)
    return calculator.calc()



