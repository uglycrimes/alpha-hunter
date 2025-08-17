import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

def is_blacklisted(coin):
    return coin["address"] in config["blacklists"]["coins"]

def add_to_blacklist(coin):
    config["blacklists"]["coins"].append(coin["address"])
    with open("config.yaml", "w") as f:
        yaml.dump(config, f)
