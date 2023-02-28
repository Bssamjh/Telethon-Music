import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6032660543:AAHo3Ojxx78gYF_BlSXAJg-PHtENdND8z2U")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzsBu0bJhPSnLFkpF--UrZ4xInL9xZ-9DVg9sgMcfqs0RdbEZI3YPA_tchKuNDoREtAzXL8_cuC2LCfWwEvl7H_JGIDpraGjmrfEAbOYkD3MBNs1d3Bodmh6_WwTwoOmv56ioS5ne5fMuvsK90AB7-DxBrRVAf0x28o-MohUalnRTicFnOMYVj0LHPSyw4AjxM8fZFa1uNLicNYHKQd329er0KHzqh4eLjoCQwDHKicjdLduLVo1J-DsDnJUaoZ60HWSqaaACeL4HEzy0FqjYGMqDQb1Iw8NEXQiZ62oA8lr3mLrayVS68JEaznPNWsGMMDD1wAfoVszeTBiDM1vbTi2gMk=") #pastw string session 
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "musiczaidtelthon_bot")
    SUPPORT = os.environ.get("SUPPORT", "saewrtm") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "tesazmo") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6115381327")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True" #optional
