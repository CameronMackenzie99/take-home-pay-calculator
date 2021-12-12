from dataclasses import dataclass
import numpy as np
import json
from typing import List

@dataclass
class CalcConfig:
    salary: int
    tax_bands: str
    tax_rates: str
    # export_dir: str


def read_config(config_file: str) -> CalcConfig:
    with open(config_file, 'r') as file:
        data = json.load(file)
        return CalcConfig(**data)