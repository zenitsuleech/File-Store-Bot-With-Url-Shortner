import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "25349731"))
  API_HASH = os.environ.get("API_HASH", "58c4653460a25b1f55d22761337b5781")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6778234587:AAEVLx5PPwnVE1OFBzz45bFgK8OqInZfVfU")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "OtakuGuardianBot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002208728458"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "https://api-ssl.bitly.com/v4/shorten")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "e915ad166db42221219594d65b09177f90d653aa")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "7019977613"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://zenistuleech:KALxIvpAixPM9RCs@cluster0.na2qk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002167928083")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002159154574"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f""" 
   Otaku Guardian Bot
  Creator: [Mithun](https://t.me/mithun_naam_toh_suna_hoga)
  Languague Used: Python
  """
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [Mithun](https://t.me/mithun_naam_toh_suna_hoga)"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\n**Otaku Guardian Bot**
"""
