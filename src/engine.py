"""Handles calculations from salary and config file inputs."""
from dataclasses import dataclass
from decimal import Decimal
from typing import List, Tuple, Optional

from moneyed import Money

from money import convert_to_money


class PersonalAllowanceCalculator():
    """Calculates personal allowance."""
    def __init__(self, salary: Money, pa_threshold: Money, base_pa: Money):
        self.salary = salary
        self.pa_threshold = pa_threshold
        self.base_pa = base_pa
        self.pa_reduction: Optional[Money] = None
        self.personal_allowance: Optional[Money] = None
    def calc(self) -> Money:
        """Returns the personal allowance for a given gross salary,
        and a personal allowance threshold and base personal allowance
        defined in the config file."""
        if self.salary > self.pa_threshold:
            self.pa_reduction = (self.salary - self.pa_threshold) / 2 # type: ignore
            if (self.pa_reduction * 2) < self.base_pa: # type: ignore
                self.personal_allowance = self.base_pa - self.pa_reduction # type: ignore
            else:
                self.personal_allowance = convert_to_money(0)
        else:
            self.personal_allowance = self.base_pa
        return self.personal_allowance # type: ignore

class TaxableIncomeCalculator():
    """Calculates taxable income."""
    def __init__(self, salary: Money, personal_allowance: Money):
        self.personal_allowance = personal_allowance
        self.salary = salary
    def calc(self):
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
                    taxable_list.append(self.tax_bands[index + 1]- band)
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
        else:
            total_tax_due = convert_to_money(0)
        tax_due = list(zip(total_tax_due_list, self.tax_rates))
        total_taxable = self.taxable
        return TaxResult(
            total_taxable,
            total_tax_due, # type: ignore
            tax_due
        )
