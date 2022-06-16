"""Defines attributes of config object and function for reading the config file."""
import json
from dataclasses import dataclass
from decimal import Decimal
from typing import List

from moneyed import Money

from src.money import convert_list_to_money, convert_to_money


@dataclass
class CalcConfig:
    """Configuration settings for calculations."""
    tax_bands: List[int]
    tax_rates: List[float]
    ni_bands: List[int]
    ni_rates: List[float]
    pa_threshold: int
    base_pa: int


def read_config(config_file: str, tax_year: str) -> CalcConfig:
    """Reads the .json config file and unpacks the data."""
    with open(config_file, 'r', encoding="utf-8") as file:
        data = json.load(file)
        return CalcConfig(**data[tax_year])

@dataclass
class CalcMoneyConfig:
    """Configuration settings for calculations, after conversion to Money and decimal objects."""
    tax_bands: List[Money]
    tax_rates: List[Decimal]
    ni_bands: List[Money]
    ni_rates: List[Decimal]
    pa_threshold: Money
    base_pa: Money

def process_config(calc_config: CalcConfig) -> CalcMoneyConfig:
    """Converts configuration file attributes to Money and decimal objects."""
    tax_bands = convert_list_to_money(calc_config.tax_bands)
    tax_rates = [Decimal(str(i)) for i in calc_config.tax_rates]
    ni_bands = convert_list_to_money(calc_config.ni_bands)
    ni_rates = [Decimal(str(i)) for i in calc_config.ni_rates]
    pa_threshold  =convert_to_money(calc_config.pa_threshold)
    base_pa = convert_to_money(calc_config.base_pa)
    return CalcMoneyConfig(
        tax_bands,
        tax_rates,
        ni_bands,
        ni_rates,
        pa_threshold,
        base_pa,
        )
