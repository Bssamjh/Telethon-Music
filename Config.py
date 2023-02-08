import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6256153474:AAHn8sf8VtJwQkHcAvaOTXpeZ3B9mmKQgAM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzgBuyvqpgkCKJcZJkjNw92wcVYIuoJ9d_pXhoMbW3ylaHh1dNYR3qE-ZKb-PKltTpC_qLiQTLvJHLBWWTDqe-bhZuK0cjIiBN-tXSzN6cosXpqe_FKJJUdaM-EsovBwiUJ97R5dLIukMHlU1T0Z_hBkzzF0-Mii4zo8EQCjU0rGQk-nOOvliYESsxvxqwbG4UPmpnghctL1TEus0FxOoZefVajR6kSgdKjPSECx8jOljtb0wz_qo6G3JjXx4Dh6PKJsY-tNLptGYNCFMDOdC31o7F6lvG4GIrJNWTMiHoGcdHUnFqr4RJjtXv2WptYBbDopGBEdj92AbA5XE6weUTpJRkU=") #pastw string session 
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "musiccxzesawe_bot")
    SUPPORT = os.environ.get("SUPPORT", "cxzftds") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "tsaewm") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6021847554")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True" #optional
