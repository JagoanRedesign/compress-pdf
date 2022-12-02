import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5784397162:AAEeRjN3HfHaUir5Z-NzBYwcmfGggDOG1-k")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "14962060"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "b726ce690552a5707dd80294907f39e1")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
