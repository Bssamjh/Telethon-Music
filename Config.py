import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5891484684:AAFpRy-ruTs5w3azIDKvejfx5znU-9F4Amk")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzMBu55rKkMJdXTgeGmvondYXFuCEo0eWCNgzYaYGk3CDWFCReXeQKAh1u-AvcNlu9qL2stwm9cGuhekH0F7LQJt4yi4cdEMprB5Z8ox5mJPDCu6JjAlvrx6f2nAYRjdCnxO5xwhJvmvG2A1owKHk1ju5UEqBwswDC_FRXPAbarCsKt98MKkPi_Jqxgyy_uAIbp97yqE6Z1ETbHKSJhFFb1dO1T9mn9bHypym3E5a-36YZUe90Z67H79iBS-Giquvk72ZCRVVXXw0R_bEw8OTKkCWsYLXssbhtIlEzsnbQbSJqMzBD-enhT2N04KWN0CJG2ghXlvpvYtgqoD_SgfYh_fWqA=") #pastw string session 
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "musiczaidtelthon_bot")
    SUPPORT = os.environ.get("SUPPORT", "saewrtm") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "tesazmo") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6176759002")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True" #optional
