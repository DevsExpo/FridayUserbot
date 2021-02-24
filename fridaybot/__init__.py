import asyncio
import logging
import os
import sys
import time
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger
from fridaybot.clients import bot, client2, client3
import pylast
import wget
from nospamplus.connect import Connect
from dotenv import load_dotenv
from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from requests import get
from telegraph import Telegraph, exceptions, upload_file
from telethon import TelegramClient
from telethon.sessions import StringSession

from fridaybot.Configs import Config

if os.path.exists('local.env'):
    load_dotenv('local.env')

Lastupdate = time.time()
sedprint = logging.getLogger("WARNING")


basicConfig(
format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=INFO
)
LOGS = getLogger(__name__)
BOTLOG_CHATID = os.environ.get("BOTLOG_CHATID", None)
BOTLOG = sb(os.environ.get("BOTLOG", "False"))
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))
DB_URI = os.environ.get("DATABASE_URL", None)
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/usr/bin/chromedriver")
GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", "/usr/bin/google-chrome")
HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
HELP_EMOJI = os.environ.get("HELP_EMOJI", None)
AUTONAME = os.environ.get("AUTONAME", None)
CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
PRIVATE_GROUP_BOT_API_ID = os.environ.get("PRIVATE_GROUP_BOT_API_ID", None)
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
LESS_SPAMMY = os.environ.get("LESS_SPAMMY", True)
COUNTRY = str(os.environ.get("COUNTRY", ""))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
ANTISPAM_SYSTEM = os.environ.get("ANTISPAM_SYSTEM", "DISABLE")
WHITE_CHAT = PRIVATE_GROUP_ID = int(os.environ.get("WHITE_CHAT", False))
BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = pylast.md5(LASTFM_PASSWORD_PLAIN)
if not LASTFM_USERNAME == "None":
    lastfm = pylast.LastFMNetwork(
    api_key=LASTFM_API,
    api_secret=LASTFM_SECRET,
    username=LASTFM_USERNAME,
    password_hash=LASTFM_PASS,
    )
else:
    lastfm = None
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./downloads")
CMD_LIST = {}
INT_PLUG = ""
LOAD_PLUG = {}
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
SUDO_LIST = {}
CMD_HELP = {}
CUSTOM_PMPERMIT_MSG = {}
CUSTOM_BOTSTART = {}
ISAFK = False
AFKREASON = None
link = "https://people.eecs.berkeley.edu/~rich.zhang/projects/2016_colorization/files/demo_v2/colorization_release_v2.caffemodel"
km = "./resources/imgcolour/colorization_release_v2.caffemodel"
pathz = "./resources/imgcolour/"
if os.path.exists(km):
    pass
else:
    try:
        sedlyf = wget.download(link, out=pathz)
    except:
        sedprint.info("I Wasn't Able To Download Cafee Model. Skipping.")
if Config.NOSPAMPLUS_TOKEN == None:
    sclient = None
    sedprint.info("[Warning] - NoSpamPlusToken is None")
else:
    try:
        sclient = Connect(Config.NOSPAMPLUS_TOKEN)
    except Exception as e:
        sclient = None
        sedprint.info("[Warning] - " + str(e))    
try:
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
except:
    pass
friday_version = "7.0"
friday_name = "FridayUserBot V7.0"
