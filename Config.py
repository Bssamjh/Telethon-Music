import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6052175393:AAGR2Vr_BbxhwmE0gh2kCKmqlO53dwXRdLw")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzMBu1PZ3bq8MUq1WlU2aDs6NVIFdC5kLg4FlYLsGg2zy-k1QMzggodgJcwG5Be1PcOn0qpWk_ducTwTT-k2EEgD3KJzj1hq3nFSqaZkHDs8L41ly436xB-4CpeN7W3Ifv7Yf-30Qo6glBKMElaGPcs-Q7IZdWi7yhbwIF9W2ZdMOlUxFkjSS-pM28dFL6WJcGRvo1hWZHcsxnH8zgMelUrvypcP9uvV7Xcbbt2UF7tEPCr5zi55yr6ORwrJZioaH23o2nz5hVmKPt4rU8qnUrOGE2vU29uRjBAuaSGj0Ck5tkl8VM31lc0U_q9OC8iELayQvW4WsTeoR07oAFmJtimRUek=") #pastw string session 
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "sawertwzxcsan_bot")
    SUPPORT = os.environ.get("SUPPORT", "tfsadfm") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "tsazxm") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6016219802")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True" #optional
