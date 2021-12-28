from datetime import datetime
import json

from dir import working_directory

def export_result(result: dict, export_dir: str) -> None:
    """Dumps calculation result into json file  in export directory."""
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d,%H-%M-%S")
    with working_directory(export_dir):
        export_name = f"result_{timestamp}.json"
        f = open(export_name, "w")
        json.dump(result, f)