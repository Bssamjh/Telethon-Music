mport os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5927637248:AAGOGeyIVRWoCyCi6Tqx11ZukA2lRFY5Zo4")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1sBuzJzWO9ddhU_SD4SQqi9maVLc-99wB69rAFnicvWWv04topmB4lilu_dxE6lavy_sRMTy9FkEDPwW8EhxxfZpU7dsjzofdRmTUWgFxX6w4LFtccBqIvQjrk5kHk7XGB5NqLzCcWPoy3Jktx8swgvbD4rpZ4XTlFzgx9EIqFeFN_qZdi7TLP7vpLmt2DE6MH2gLbS10Qsq1V6bZWA4MoxslEF2sGDFMVduVoognPLbTCi0cZq9VVYRtRx06Ik9vCMMSkh-uiqOPOSfeRpy51hk5WtKLIKwWdZ38aQwGnS2bA9wqBv__9SnnnHFeyOI1TZrJqP14RqkndjOp1zyuceKfs=") #pastw string session
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "uozatewcz453_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5702988220")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True" #optional 
