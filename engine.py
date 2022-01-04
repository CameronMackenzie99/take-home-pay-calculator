"""Handles calculations from salary and config file inputs."""
from typing import List, Tuple

class PersonalAllowanceCalculator():
    """Calculates personal allowance."""
    def __init__(self, salary: int, pa_threshold: int, base_pa: int):
        self.salary = salary
        self.pa_threshold = pa_threshold
        self.base_pa = base_pa
        self.pa_reduction = None
        self.personal_allowance = None
    def calc(self) -> int:
        """Returns the personal allowance for a given gross salary,
        and a personal allowance threshold and base personal allowance
        defined in the config file."""
        if self.salary > self.pa_threshold:
            self.pa_reduction = (self.salary - self.pa_threshold) / 2
            if (self.pa_reduction * 2) < self.base_pa:
                self.personal_allowance = self.base_pa - self.pa_reduction
            else:
                self.personal_allowance = 0
        else:
            self.personal_allowance = self.base_pa
        return self.personal_allowance

class TaxableIncomeCalculator():
    """Calculates taxable income."""
    def __init__(self, salary: int, personal_allowance: int):
        self.personal_allowance = personal_allowance
        self.salary = salary
    def calc(self):
        """Returns the taxable income for a given salary and
        personal allowance."""
        if self.salary > self.personal_allowance:
            return self.salary - self.personal_allowance
        else:
            return 0

class TaxCalculator:
    """Calculates the tax due on a given gross salary."""
    def __init__(self, taxable: int, tax_bands: List[int], tax_rates: List[int]):
        self.taxable = taxable
        self.tax_bands = tax_bands
        self.tax_rates = tax_rates

    def calc(self)-> Tuple[int, int, List[Tuple[int, int]]]:
        """Returns the tax due on a given taxable amount,
        based on the tax bands and rates defined in the
        config file."""
        total_taxed = 0
        to_be_taxed = self.taxable
        taxable_list: List[int] = []
        for index, band in enumerate(self.tax_bands):
            if band is not self.tax_bands[-1]:
                # Check if remaining taxable exceeds band
                if to_be_taxed - (self.tax_bands[index + 1] - band) > 0:
                    taxable_list.append(self.tax_bands[index + 1]- band)
                    total_taxed += self.tax_bands[index + 1] - band
                    to_be_taxed -= self.tax_bands[index + 1] - band
                # if doesn't exceed, all remaining taxable is in that band
                else:
                    taxable_list.append(to_be_taxed)
                    to_be_taxed = 0
            # If top band, then all remaining taxable is in that band
            else:
                taxable_list.append(to_be_taxed)
        total_tax_due_list = [(segment * rate) for segment, rate in
                            list(zip(taxable_list, self.tax_rates))]
        total_tax_due = sum(total_tax_due_list)
        tax_due = list(zip(total_tax_due_list, self.tax_rates))
        total_taxable = self.taxable
        return total_taxable, total_tax_due, tax_due
