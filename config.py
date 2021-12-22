from dataclasses import dataclass
import json
from typing import List

@dataclass
class CalcConfig:
    tax_bands: list
    tax_rates: list
    pa_threshold: int
    base_pa: int
    # export_dir: str TODO: export results to csv


def read_config(config_file: str) -> CalcConfig:
    """Reads the .json config file and unpacks the data."""
    with open(config_file, 'r') as file:
        data = json.load(file)
        return CalcConfig(**data)
