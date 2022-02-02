"""Tests for calculations in engine module."""
import unittest
from decimal import Decimal

from moneyed import Money
from backend.src import engine


class TestPersonalAllowanceCalc(unittest.TestCase):
    """Test calculation of personal allowance."""
    def test_personal_allowance_calculator_no_red(self):
        """Test calculation of personal allowance with no reduction."""

        salary = Money(55000, "GBP")
        pa_threshold =  Money(100000, "GBP")
        base_pa =  Money(12579, "GBP")
        test_calc = engine.PersonalAllowanceCalculator(salary, pa_threshold, base_pa)

        result = test_calc.calc()

        self.assertEqual(result.amount, Decimal("12579"))

    def test_personal_allowance_calculator_partial_red(self):
        """Test calculation of personal allowance with partial reduction."""

        salary =  Money(112000, "GBP")
        pa_threshold =  Money(100000, "GBP")
        base_pa =  Money(12579, "GBP")
        test_calc = engine.PersonalAllowanceCalculator(salary, pa_threshold, base_pa)

        result = test_calc.calc()

        self.assertEqual(result.amount, Decimal("6579"))

    def test_personal_allowance_calculator_full_red(self):
        """Test calculation of personal allowance with full reduction."""
        salary = Money(130000, "GBP")
        pa_threshold = Money(100000, "GBP")
        base_pa = Money(12579, "GBP")
        test_calc = engine.PersonalAllowanceCalculator(salary, pa_threshold, base_pa)

        result = test_calc.calc()

        self.assertEqual(result.amount, Decimal("0"))

class TestTaxableIncomeCalc(unittest.TestCase):
    """Test calculation of taxable income."""
    def test_taxable_income_calculator_below_threshold(self):
        """Test calculation of taxable income when salary is below personal allowance threshold."""

        salary = Money(0, "GBP")
        personal_allowance = Money(12579, "GBP")
        test_calc = engine.TaxableIncomeCalculator(salary, personal_allowance)

        result = test_calc.calc()

        self.assertEqual(result.amount, Decimal("0"))
    def test_taxable_income_calculator_above_threshold(self):
        """Test calculation of taxable income when salary is above personal allowance threshold."""

        salary = Money(112000, "GBP")
        personal_allowance = Money(6579, "GBP")
        test_calc = engine.TaxableIncomeCalculator(salary, personal_allowance)

        result = test_calc.calc()

        self.assertEqual(result.amount, Decimal("105421"))

    def test_taxable_income_calculator_high_above_threshold(self):
        """Test calculation of taxable income when salary is high above
        personal allowance threshold (i.e. personal allowance is zero)."""

        salary = Money(150000, "GBP")
        personal_allowance = Money(0, "GBP")
        test_calc = engine.TaxableIncomeCalculator(salary, personal_allowance)

        result = test_calc.calc()

        self.assertEqual(result.amount, Decimal("150000"))

class TestTaxCalc(unittest.TestCase):
    """Test calculation of tax."""
    def test_takehome_pay_calculator_no_tax(self):
        """Test calculation of tax when salary is below personal allowance threshold
        i.e no tax is due."""
        taxable = Money(0, "GBP")
        tax_bands = [Money(0, "GBP"), Money(37700, "GBP"), Money(150000, "GBP")]
        tax_rates = [Decimal("0.2"), Decimal("0.4"), Decimal("0.45")]
        test_calc = engine.TaxCalculator(taxable, tax_bands, tax_rates)

        result = test_calc.calc()

        self.assertEqual(result.total_tax_due.amount, Decimal("0"))

    def test_takehome_pay_calculator_lower_band(self):
        """Test calculation of tax when salary is below personal allowance threshold
        and tax is due in only the lower band."""
        taxable = Money(20000, "GBP")
        tax_bands = [Money(0, "GBP"), Money(37700, "GBP"), Money(150000, "GBP")]
        tax_rates = [Decimal("0.2"), Decimal("0.4"), Decimal("0.45")]
        test_calc = engine.TaxCalculator(taxable, tax_bands, tax_rates)

        result = test_calc.calc()

        self.assertEqual(result.total_tax_due.amount, Decimal("4000"))

    def test_takehome_pay_calculator_middle_band(self):
        """Test calculation of tax when salary is above personal allowance threshold
        and tax is due in the lower and middle bands."""
        taxable = Money(50000, "GBP")
        tax_bands = [Money(0, "GBP"), Money(37700, "GBP"), Money(150000, "GBP")]
        tax_rates = [Decimal("0.2"), Decimal("0.4"), Decimal("0.45")]
        test_calc = engine.TaxCalculator(taxable, tax_bands, tax_rates)

        result = test_calc.calc()

        self.assertEqual(result.total_tax_due.amount, Decimal("12460"))

    def test_takehome_pay_calculator_top_band(self):
        """Test calculation of tax when salary is above personal allowance threshold
        and tax is due in all bands."""
        taxable = Money(180000, "GBP")
        tax_bands = [Money(0, "GBP"), Money(37700, "GBP"), Money(150000, "GBP")]
        tax_rates = [Decimal("0.2"), Decimal("0.4"), Decimal("0.45")]
        test_calc = engine.TaxCalculator(taxable, tax_bands, tax_rates)

        result = test_calc.calc()

        self.assertEqual(result.total_tax_due.amount, Decimal("65960"))

if __name__ == '__main__':
    unittest.main()
