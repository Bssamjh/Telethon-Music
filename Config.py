import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5711008656:AAGj9nPSW-_3ZyrS0-7gTJ_07GBxKvyWBHA")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1wBu7IUjlaHfTu1nVarSd8QEC8l5DS4x1ps_wO53cAE6BeMnDnaF6VG5MpkafW0UR9-O18urmwW68DoCHY36FR7hr2iH5BscXUx45jgCiVYs57kSJVL27DzASjxnZRRcym9fPeZHzXsCwLN9LdgdFmqv2nS6c0yrRSH1FrRHBhs9DqNyMAm4LTSanloGCWB2CkjiISIxRD9YqzwUiZKP4MS670-knqy1Ki-ewaBFTj1pJKkX5K2jLaP-d1EOSh55VOq2Ga1FpNlGfkduImXrO85XBEHnLh1uwAXoCxV6VZSoHauSkHS8EmgZLWNEfNrX1H5HVWaZiwK9IzEphHjgUUKKF4=") #pastw string session 
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "musiczoozuser_bot")
    SUPPORT = os.environ.get("SUPPORT", "rozsamo") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "tsamnxz") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5892511047")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True" #optional
