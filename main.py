# # Ask for user salary    
# class CalcTax:

#     tax_bands = [12570, 50270, 150000]
#     tax_rates = [20, 40, 45]

     

#         for band in self.tax_bands:
#             if self.salary <= band:



#     # def output_calc():
#     #     thpay = thpay_calc()
#     #     thpay.request_salary()

#     # def request_salary(self):
#     #     self.salary = input("What is your pre-tax salary?: ")
#     #     print ("£" + str(self.salary))

# calc_tax = CalcTax()
# CalcTax.calc_tax(26000, 10)
from dataclasses import dataclass
from config import CalcConfig, read_config







    # tax_list = [(pct * (salary - band)) for (band, pct) in zip(tax_bands, tax_amts)] 
    # max_tax = []
    # for index, sal in enumerate(tax_bands[:-1]):
    #     max_tax.append(tax_bands[index + 1] - sal)
    # max_tax = [segment * tax for segment, tax in zip(max_tax, tax_amts[:-1])]
    # for index, value in enumerate(tax_list):
    #     try:
    #         if value > max_tax[index]:
    #             tax_list[index] = max_tax[index]
    #     except:
    #         pass
    #     tax_to_pay = int(sum([x for x in tax_list if x > 0]))
    # return tax_to_pay

class NationalInsuranceCalculation:
    ni_bands = [9568, 50270]
    ni_amts = [0.12, 0.02]

    
# salary = int(input("What is your salary? "))

# print("So your gross annual salary is %r GBP" % (salary))
# print("\nYour take home pay is: " + str(salary - taxes(salary, tax_bands, tax_amts)) + " GBP")

def main() -> None:
    
    config = read_config("./config.json")
    result = calc_takehome_pay(config)
    export_data(result, config.exportdir)

if __name__ == "__main__":
    main()