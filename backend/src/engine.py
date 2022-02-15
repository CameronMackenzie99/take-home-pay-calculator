"""Handles calculations from salary and config file inputs."""
from dataclasses import dataclass
from decimal import Decimal
from typing import List, Tuple

from moneyed import Money

from src.money import convert_to_money


class PersonalAllowanceCalculator():
    """Calculates personal allowance."""

    def __init__(self, salary: Money, pa_threshold: Money, base_pa: Money):
        self.salary = salary
        self.pa_threshold = pa_threshold
        self.base_pa = base_pa
        self.pa_reduction: Money = Money(0, "GBP")
        self.personal_allowance: Money = Money(0, "GBP")

    def calc(self) -> Money:
        """Returns the personal allowance for a given gross salary,
        and a personal allowance threshold and base personal allowance
        defined in the config file."""
        if self.salary > self.pa_threshold:
            self.pa_reduction = ( #type: ignore - cannot be Decimal as dividing by integer
                self.salary - self.pa_threshold) / 2
            if (self.pa_reduction * 2) < self.base_pa:
                self.personal_allowance = self.base_pa - self.pa_reduction
            else:
                self.personal_allowance = convert_to_money(0)
        else:
            self.personal_allowance = self.base_pa
        return self.personal_allowance


class TaxableIncomeCalculator():
    """Calculates taxable income."""

    def __init__(self, salary: Money, personal_allowance: Money):
        self.personal_allowance = personal_allowance
        self.salary = salary

    def calc(self) -> Money:
        """Returns the taxable income for a given salary and
        personal allowance."""
        if self.salary > self.personal_allowance:
            return self.salary - self.personal_allowance
        else:
            return convert_to_money(0)


@dataclass
class TaxResult:
    """Properties calculated relating to tax."""
    total_taxable: Money
    total_tax_due: Money
    tax_due: List[Tuple[Money, Decimal]]


class TaxCalculator:
    """Calculates the tax due on a given gross salary."""

    def __init__(self, taxable: Money, tax_bands: List[Money], tax_rates: List[Decimal]):
        self.taxable = taxable
        self.tax_bands = tax_bands
        self.tax_rates = tax_rates

    def calc(self) -> TaxResult:
        """Returns the tax due on a given taxable amount,
        based on the tax bands and rates defined in the
        config file."""
        total_taxed = convert_to_money(0)
        to_be_taxed = self.taxable
        taxable_list: List[Money] = []
        for index, band in enumerate(self.tax_bands):
            if band is not self.tax_bands[-1]:
                # Check if remaining taxable exceeds band
                if to_be_taxed - (self.tax_bands[index + 1] - band) > convert_to_money(0):
                    taxable_list.append(self.tax_bands[index + 1] - band)
                    total_taxed += self.tax_bands[index + 1] - band
                    to_be_taxed -= self.tax_bands[index + 1] - band
                # if doesn't exceed, all remaining taxable is in that band
                else:
                    taxable_list.append(to_be_taxed)
                    to_be_taxed = convert_to_money(0)
            # If top band, then all remaining taxable is in that band
            else:
                taxable_list.append(to_be_taxed)
        total_tax_due_list = [(segment * rate) for segment, rate in
                              list(zip(taxable_list, self.tax_rates))]
        if sum(total_tax_due_list) != 0:
            total_tax_due = sum(total_tax_due_list)
            assert isinstance(total_tax_due, Money) # checks that sum is not zero from an empty list
        else:
            total_tax_due = convert_to_money(0)
        tax_due = list(zip(total_tax_due_list, self.tax_rates))
        total_taxable = self.taxable
        return TaxResult(
            total_taxable,
            total_tax_due,
            tax_due
        )

class NationalInsuranceCalculator:
    """Calculates the national insurance contributions due on a given gross salary."""

    def __init__(self, salary: Money, ni_bands: List[Money], ni_rates: List[Decimal]):
        self.salary = salary
        self.ni_bands = ni_bands
        self.ni_rates = ni_rates

    def calc(self) -> Money:
        """Returns the National Insurance deductions due on a given gross salary."""
        ni_deductible_bands:List[Money] = []
        # Check if no NI is due.
        if self.salary <= self.ni_bands[0]:
            return convert_to_money(0)
        for index, band in enumerate(self.ni_bands):
            if band != self.ni_bands[-1]:
                # check if salary falls between current band and the next band
                if self.salary <= self.ni_bands[index + 1] and self.salary > band:
                    # append salary portion that is in that band
                    ni_deductible_bands.append(self.salary - band)
                # else if salary exceeds next band
                elif self.salary > band:
                    # append difference between current and next band
                    ni_deductible_bands.append(self.ni_bands[index + 1] - band)
                # else the salary is less than the current band
                else:
                    # append value of 0 to that band
                    ni_deductible_bands.append(convert_to_money(0))
            # if it is the final band
            else:
                # if salary exceeds this band
                if self.salary > band:
                    # append salary above the top band
                    ni_deductible_bands.append(self.salary - band)
                else:
                    # append value of 0 to top band
                    ni_deductible_bands.append(convert_to_money(0))

        # multiply deductible salary in each band by the national insurance rate for that band
        ni_due_list = [amount * rate for amount, rate in zip(ni_deductible_bands, self.ni_rates)]
        total_ni_due = sum(ni_due_list)
        assert isinstance(total_ni_due, Money) # checks that sum is not zero from an empty list
        return total_ni_due
