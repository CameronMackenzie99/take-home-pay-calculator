from dataclasses import dataclass
import json
from typing import List

@dataclass
class CalcConfig:
    tax_bands: str
    tax_rates: str
    # export_dir: str TODO: export results to csv


def read_config(config_file: str) -> CalcConfig:
    """Reads the .json configuration file and unpack the data."""
    with open(config_file, 'r') as file:
        data = json.load(file)
        return CalcConfig(**data)