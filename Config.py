import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6136029860:AAE97ROhoZ8WzdnqvCqALzVLCTZ6FS9malI")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzUBu6UzutW8hD0gXzamYr62SW6R8DhL-Y8QaoIL6c0OR7vyPRgIdARzdFTD9wRyWwUB6027CXHpJhvSg7hwU8TywxM3sYotAOOvtoHngxUaKZ-uTpl5IcMHDk8lXUNLwTJAKh-U8-PH-bDpGLO9AmlIPY3Vldjf4lKEpp2_9pS7tX3gBLUQYm-r6dS3Eiyn1o4OW1EfmDBFnEB16AT9jJV2yL7VpGHqSKmvRHC7xOzEC7KXhLawLmGI9WLXltdnHx-E-f1QKZQPq34BYquTjqs981-1JwDYtLGZNgNJCUyFWdCQpTLSe3ynbfvO87Jf23nXzA--EGMUD-QfCP8gIop2kis=") #pastw string session 
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "groupmnoiurewas_bot")
    SUPPORT = os.environ.get("SUPPORT", "saewruzx") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "saewrtmo") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/ff3cb7f3cf126c248d9dd.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/90364215558428720a18a.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5476374386")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True" #optional
