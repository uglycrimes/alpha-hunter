import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

def filter_coins(coin):
    if coin["liquidity"] < config["filters"]["min_liquidity"]:
        return False
    if coin["volume"] < config["filters"]["min_volume_24h"]:
        return False
    return True
