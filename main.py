from config import read_config
from fetch import calc_takehome_pay

def main() -> None:
    
    config = read_config("./config.json")
    print(config)
    result = calc_takehome_pay(config)
    print(result)

if __name__ == "__main__":
    main()