import time
from utils import fetch_coins
from filters import filter_coins
from blacklist import is_blacklisted, add_to_blacklist
from rugcheck import is_contract_good, is_supply_bundled
from telegram_bot import send_notification

def main():
    while True:
        coins = fetch_coins()
        for coin in coins:
            if is_blacklisted(coin):
                continue
            if not is_contract_good(coin["address"]):
                continue
            if is_supply_bundled(coin["address"]):
                add_to_blacklist(coin)
                continue
            if filter_coins(coin):
                send_notification(f"✅ New coin detected: {coin['symbol']}")
        time.sleep(60)

if __name__ == "__main__":
    main()
