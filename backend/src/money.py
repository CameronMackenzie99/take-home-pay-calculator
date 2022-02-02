"""Handles conversion of configuration parameters to Money objects
 which can be used in calculations losslessly."""
from typing import List, Union

from moneyed import Money


CURRENCY = "GBP"

def convert_to_money(value: Union[int, float, str]):
    """Returns a Money object of given value and currency."""
    return Money(value, currency=CURRENCY)

def convert_list_to_money(input_list: Union[List[int],List[float]]):
    """Returns a list of Money objects of given value and currency."""
    return [Money(i, currency=CURRENCY) for i in input_list]
