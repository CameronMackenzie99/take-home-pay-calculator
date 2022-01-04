"""Defines attributes of config object and function for reading the config file."""
from dataclasses import dataclass
import json
from typing import List

@dataclass
class CalcConfig:
    """Configuration settings for calculations."""
    tax_bands: List[int]
    tax_rates: List[int]
    pa_threshold: int
    base_pa: int
    export_dir: str


def read_config(config_file: str) -> CalcConfig:
    """Reads the .json config file and unpacks the data."""
    with open(config_file, 'r', encoding="utf-8") as file:
        data = json.load(file)
        return CalcConfig(**data)
