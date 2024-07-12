
import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7193814472:AAE8tddcwjZL7SH4-Hwp10rXfe2vz5Rm7ic")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "24371796"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8121c78f4b8b31e88cc2623d1277338d")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002118745640"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1439890119"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://tsywhll151:tsywhll151@cluster0.zh9gbvw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1002034252225"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1002038915478"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<blockquote><b>Hello {mention}\n\nI can store private files in Specified Channel and other users can access it from special link.</b><blockquote>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1895952308 5629054374 5355745915 6283260043 1475732523 6228788487 5696112220 7162615398").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<blockquote><b>Hello {mention}\n\nYou need to join in my Channel to use me\nKindly Please join Channel</b></blockquote>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "True")

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/9f10cfb5ea93d4766357e.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/541d20525d6938d2fd77e.jpg")

HELP_TXT = "<blockquote>🍷🗿<b></b>
BOT_STATS_TEXT = "<b>BOT UPTIME {uptime}</b>"
USER_REPLY_TEXT = "<blockquote><b>Don't send me messages directly I'm only File Share bot! @Bot Developer @StupidBoi69</b></blockquote>"

ADMINS.append(OWNER_ID)
ADMINS.append(1895952308)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
