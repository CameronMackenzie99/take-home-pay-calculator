"""API calculator for computing tax owed and net pay."""

from schemas.calculate import CalculationResponse

from src.config import process_config, read_config
from src.export import dataframe_to_json, export_result_to_dataframe
from src.fetch import CalculateTakeHomePay
from src.money import convert_to_money


def main(salary, tax_year) -> CalculationResponse:
    """Calls function to convert the salary to a money object, reads config file
    and uses resulting data to calculate take home pay and call function to export to dataframe.
    """
    input_salary = convert_to_money(salary)
    config = process_config(read_config("src/config.json", tax_year))
    result = CalculateTakeHomePay(input_salary, config).calc_takehome_pay()
    result_df = export_result_to_dataframe(result)
    result_json = dataframe_to_json(result_df)
    return result_json


if __name__ == "__main__":
    main(55000, "2021/22")
