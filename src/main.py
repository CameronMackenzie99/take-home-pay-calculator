"""Command line calculator for computing tax owed and net pay."""
import dataclasses
from config import read_config
from export import export_result
from fetch import calc_takehome_pay

def main() -> None:
    """Reads config file and uses resulting data to calculate take home pay.
    Converts object to a dictionary and prints out contents.
    Exports dictionary to a json file in the specified directory.
    """
    config = read_config("src/config.json")
    result = calc_takehome_pay(config)
    display = dataclasses.asdict(result)
    print("----------------------------------RESULT----------------------------------")
    for i in display:
        print(f"{i}: {display[i]}")
    export_result(display, config.export_dir)
    print("--------------------------------------------------------------------------")

if __name__ == "__main__":
    main()
