import yaml
from telegram import Bot

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

bot = Bot(token=config["telegram"]["bot_token"])

def send_notification(message):
    bot.send_message(chat_id=config["telegram"]["chat_id"], text=message)
