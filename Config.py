import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6008272730:AAGQDJWxgRcXVSn17BvIZYzRAEkMWEfvJZ4")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1sBuzgG6x2pmDL-LpX_eZPYM6fqXnBWPG5VR8e9xqug7T_Wrlw6Ws5OYUOankuKcqoX5GgCGh75clgrvOBPV4s2Udku9sbQCBlHuvKpdOuY2hHw-aahGABlViaZIcI9_sve9ZG8M-0KC9xdN4LMrxYpJXYAAyX4pN9rIL-jFUcOqptxa_YzWrOf32FrAzGBuqtR9qnEOdI7jmEne-MnjUAgmzvBX0oKOOuiZnY9IzD7ih7f6F7CaYmvbwfoQpartI2tPmAY9FbEvCBx0-ozSRzfNvAvtKCriKpvn0K1glZ1SQ9jU09lrV_k3WmXwWfnVcFxqb1Z2iYjkrEw27KoJR0u_uQ=") #pastw string session 
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "musiczaidtelthon_bot")
    SUPPORT = os.environ.get("SUPPORT", "zxsaewm") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "saewrtmo") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/ff3cb7f3cf126c248d9dd.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/90364215558428720a18a.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6145569463")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True" #optional
