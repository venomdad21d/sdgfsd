import os


class Mody(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 21793031))

    API_HASH = os.environ.get("API_HASH", "52e91180e35e6d91898764b43c567493")
    
    USER_NAME = os.environ.get("USER_NAME", "")
    
    SESSION = os.environ.get("SESSION", "")

    BOT_USER = os.environ.get("BOT_USER", "")

    VIA_USER = os.environ.get("VIA_USER", "")

    MENTION = os.environ.get("MENTION", "")
