from calculate import Calc, CalcResult


def zip_bands(bands: list, rates: list) -> list[tuple[int, int]]:
    """Combines two integer lists into a single list of tuples."""
    return list(zip(bands, rates))

class TaxCalculator(Calc):
   
    def __init__(self, salary, tax_bands, tax_rates):
        self.salary = salary
        self.tax_bands = tax_bands
        self.tax_rates = tax_rates

    def calc(self) -> CalcResult:
        """Returns the net pay for a given gross salary, 
        based on the tax bands and rates in the config file.
        """
        #TODO: Refactor to reuse for national insurance calculations.
        tax_list = [(pct * (self.salary - band)) for (band, pct) in zip_bands(self.tax_bands, self.tax_rates)]
        max_tax = []
        for index, sal in enumerate(self.tax_bands[:-1]):
            max_tax.append(self.tax_bands[index + 1] - sal)
        max_tax = [segment * tax for segment, tax in zip(max_tax, self.tax_rates[:-1])]
        for index, value in enumerate(tax_list):
            try:
                if value > max_tax[index]:
                    tax_list[index] = max_tax[index]
            except:
                pass
            
            gross_pay = self.salary
            total_tax_due = int(sum([x for x in tax_list if x > 0]))
            net_pay = gross_pay - total_tax_due
        
        return CalcResult(
            gross_pay,
            total_tax_due,
            net_pay
        )