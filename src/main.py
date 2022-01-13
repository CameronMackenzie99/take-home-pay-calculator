"""Command line calculator for computing tax owed and net pay."""
import dataclasses

from moneyed import Money

from config import process_config, read_config
from export import export_result
from fetch import calc_takehome_pay


def main() -> None:
    """Reads config file and uses resulting data to calculate take home pay.
    Converts object to a dictionary and prints out contents.
    Exports dictionary to a json file in the specified directory.
    """
    config = process_config(read_config("src/config.json"))
    result = calc_takehome_pay(config)
    display = dataclasses.asdict(result)
    print("----------------------------------RESULT----------------------------------")
    for key, value in display.items():
        if isinstance(value, Money):
            print(f"{key}: {value}")
        elif isinstance(value, list):
            for i in display.get(key): # type: ignore
                print(f"{int(i[1]*100)}% Band: {i[0]}")
    print("--------------------------------------------------------------------------")
    export_result(display, config.export_dir)

if __name__ == "__main__":
    main()
