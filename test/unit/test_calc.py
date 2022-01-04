"""Tests for calculations in engine module."""
import unittest

from src import engine

class TestPersonalAllowanceCalc(unittest.TestCase):
    """Test calculation of personal allowance."""
    def test_personal_allowance_calculator_no_red(self):
        """Test calculation of personal allowance with no reduction."""

        salary = 55000
        pa_threshold = 100000
        base_pa = 12579
        test_calc = engine.PersonalAllowanceCalculator(salary, pa_threshold, base_pa)

        result = test_calc.calc()

        self.assertEqual(result, 12579)
    def test_personal_allowance_calculator_partial_red(self):
        """Test calculation of personal allowance with partial reduction."""

        salary = 112000
        pa_threshold = 100000
        base_pa = 12579
        test_calc = engine.PersonalAllowanceCalculator(salary, pa_threshold, base_pa)

        result = test_calc.calc()

        self.assertEqual(result, 6579)

    def test_personal_allowance_calculator_full_red(self):
        """Test calculation of personal allowance with full reduction."""
        salary = 130000
        pa_threshold = 100000
        base_pa = 12579
        test_calc = engine.PersonalAllowanceCalculator(salary, pa_threshold, base_pa)

        result = test_calc.calc()

        self.assertEqual(result, 0)

class TestTaxableIncomeCalc(unittest.TestCase):
    """Test calculation of taxable income."""
    def test_taxable_income_calculator_below_threshold(self):
        """Test calculation of taxable income when salary is below personal allowance threshold."""

        salary = 0
        personal_allowance = 12579
        test_calc = engine.TaxableIncomeCalculator(salary, personal_allowance)

        result = test_calc.calc()

        self.assertEqual(result, 0)
    def test_taxable_income_calculator_above_threshold(self):
        """Test calculation of taxable income when salary is above personal allowance threshold."""

        salary = 112000
        personal_allowance = 6579
        test_calc = engine.TaxableIncomeCalculator(salary, personal_allowance)

        result = test_calc.calc()

        self.assertEqual(result, 105421)

    def test_taxable_income_calculator_high_above_threshold(self):
        """Test calculation of taxable income when salary is high above
        personal allowance threshold (i.e. personal allowance is zero)."""

        salary = 150000
        personal_allowance = 0
        test_calc = engine.TaxableIncomeCalculator(salary, personal_allowance)

        result = test_calc.calc()

        self.assertEqual(result, 150000)

class TestTaxCalc(unittest.TestCase):
    """Test calculation of tax."""
    def test_takehome_pay_calculator_no_tax(self):
        """Test calculation of tax when salary is below personal allowance threshold
        i.e no tax is due."""
        taxable = 0
        tax_bands = [0, 37700, 150000]
        tax_rates = [0.2, 0.4, 0.45]
        test_calc = engine.TaxCalculator(taxable, tax_bands, tax_rates)

        result = test_calc.calc()

        self.assertEqual(result[1], 0)

    def test_takehome_pay_calculator_lower_band(self):
        """Test calculation of tax when salary is below personal allowance threshold
        and tax is due in only the lower band."""
        taxable = 20000
        tax_bands = [0, 37700, 150000]
        tax_rates = [0.2, 0.4, 0.45]
        test_calc = engine.TaxCalculator(taxable, tax_bands, tax_rates)

        result = test_calc.calc()

        self.assertEqual(result[1], 4000)

    def test_takehome_pay_calculator_middle_band(self):
        """Test calculation of tax when salary is above personal allowance threshold
        and tax is due in the lower and middle bands."""
        taxable = 50000
        tax_bands = [0, 37700, 150000]
        tax_rates = [0.2, 0.4, 0.45]
        test_calc = engine.TaxCalculator(taxable, tax_bands, tax_rates)

        result = test_calc.calc()

        self.assertEqual(result[1], 12460)

    def test_takehome_pay_calculator_top_band(self):
        """Test calculation of tax when salary is above personal allowance threshold
        and tax is due in all bands."""
        taxable = 180000
        tax_bands = [0, 37700, 150000]
        tax_rates = [0.2, 0.4, 0.45]
        test_calc = engine.TaxCalculator(taxable, tax_bands, tax_rates)

        result = test_calc.calc()

        self.assertEqual(result[1], 65960)

if __name__ == '__main__':
    unittest.main()
