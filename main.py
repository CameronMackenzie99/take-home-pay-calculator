from config import read_config
from export import export_result
from fetch import calc_takehome_pay
import dataclasses

def main() -> None:
    
    config = read_config("./config.json")
    result = calc_takehome_pay(config)
    display = dataclasses.asdict(result)
    for i in display:
        print(f"{i}: {display[i]}")
    export_result(display, config.export_dir)

if __name__ == "__main__":
    main()
