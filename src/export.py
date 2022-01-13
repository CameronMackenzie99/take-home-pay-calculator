"""Exports results to json file."""
from datetime import datetime

import jsonpickle

from dir import working_directory


def export_result(result, export_dir: str) -> None:
    """Dumps calculation result into json file in export directory."""
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d,%H-%M-%S")
    with working_directory(export_dir):
        export_name = f"result_{timestamp}.json"
        file = open(export_name, "w", encoding="utf-8")
        encoded_result = jsonpickle.encode(result, unpicklable=False, indent=2, use_decimal=True)
        file.write(encoded_result) # type: ignore
