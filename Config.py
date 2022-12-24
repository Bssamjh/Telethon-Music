import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5917639432:AAHy9PssF3SvmkYeSQYg1yszMsLWkBt6qwA")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1wBuyT5-wcDrV3ryAhJJRuKX5FjNptUfYfYjDxEMGIxI9ZEEs5ecqnkZPZSTzWhmszuUN-lN802Q6qmPtRXeebOnYCAoYqd2jmaKLv4F6jLfu0K1fRwvJe8JD4OMWzk2yqfwO-M43tgpm5YywmvVOHI09miVYBg8_5giVQqahXGBx1tkv7msZLVQov9wjV5gvwEKBL80jjoUPxK7aoRfLuHUYTORZznljvCDaxGqL43RSDl3NIRTidgZxhnGSWOlEO9xh-o633GZbeWtU42k70nox941O9Ez3BmvljvtXBHh8hNAgH0edvOk_uxG0Wf2dD0B78_uTu91xk8L1MioZw_Uuc=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "eminemnmoix_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5610994282")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True". 
