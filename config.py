import os



class Config(object):
      TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5784397162:AAEeRjN3HfHaUir5Z-NzBYwcmfGggDOG1-k")
      API_ID = int(os.environ.get("APP_ID", "14962060"))
      API_HASH = os.environ.get("API_HASH", "b726ce690552a5707dd80294907f39e1")
