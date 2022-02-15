"""Exports results to json file."""

import json

import pandas as pd
from schemas.calculate import CalculationResponse


def export_result_to_dataframe(result) -> pd.DataFrame:
    """Exports calculation result to dataframe,
    and expands tax_due column into bands as new columns
    to replace the single column.
    """
    raw_df = pd.DataFrame([result])
    newcols = raw_df["tax_due"].apply(pd.Series)
    newcols = newcols.rename(columns=lambda x: "p" +
                           str(((newcols.at[0, x])[1]*100)//1) + "_tax_band")
    newcols = newcols.apply(lambda cell: cell[0], axis=0)
    newcols = newcols.drop([1])
    joined_df = pd.concat([raw_df[:], newcols[:]], axis=1)
    cleaned_df = joined_df.drop("tax_due", axis=1)
    return cleaned_df


def dataframe_to_json(dataframe: pd.DataFrame) -> CalculationResponse:
    """Converts dataframe to json string, and processes to a JSON object."""
    # to_json() method requires a default_handler of str to avoid maximum recursion depth bug.
    json_str = dataframe.to_json(default_handler=str, orient="records")
    # process string into a json object
    json_arr = json.loads(json_str)
    json_result = json_arr[0]
    return json_result
