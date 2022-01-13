"""Defines attributes of config object and function for reading the config file."""
import json
from dataclasses import dataclass
from decimal import Decimal
from typing import List

from moneyed import Money

from money import convert_list_to_money, convert_to_money


@dataclass
class CalcConfig:
    """Configuration settings for calculations."""
    tax_bands: List[int]
    tax_rates: List[float]
    pa_threshold: int
    base_pa: int
    export_dir: str


def read_config(config_file: str) -> CalcConfig:
    """Reads the .json config file and unpacks the data."""
    with open(config_file, 'r', encoding="utf-8") as file:
        data = json.load(file)
        return CalcConfig(**data)

@dataclass
class CalcMoneyConfig:
    """Configuration settings for calculations, after conversion to Money and decimal objects."""
    tax_bands: List[Money]
    tax_rates: List[Decimal]
    pa_threshold: Money
    base_pa: Money
    export_dir: str

def process_config(calc_config: CalcConfig) -> CalcMoneyConfig:
    """Converts configuration file attributes to Money and decimal objects."""
    tax_bands = convert_list_to_money(calc_config.tax_bands)
    tax_rates = [Decimal(str(i)) for i in calc_config.tax_rates]
    pa_threshold  =convert_to_money(calc_config.pa_threshold)
    base_pa = convert_to_money(calc_config.base_pa)
    export_dir = calc_config.export_dir
    return CalcMoneyConfig(
        tax_bands,
        tax_rates,
        pa_threshold,
        base_pa,
        export_dir,
        )
