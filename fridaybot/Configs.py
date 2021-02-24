import os
import asyncio
import logging
import os
import sys
import time
from distutils.util import strtobool as sb
from telethon.tl.types import ChatBannedRights
import pylast
import wget
from dotenv import load_dotenv
from pylast import LastFMNetwork, md5

if os.path.exists('local.env'):
    load_dotenv('local.env')
    
class Config(object):
    LOGGER = True
    APP_ID = int(os.environ.get("APP_ID", 6))
    LANG = os.environ.get("LANG", "en")
    PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))
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
    WOLFRAM_ID = os.environ.get("WOLFRAM_ID", None)
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
    BOTLOG = sb(os.environ.get("BOTLOG", "False"))
    TZ = os.environ.get("TZ", "Asia/Kolkata")
    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    CLEAN_GROUPS = os.environ.get("CLEAN_GROUPS", False)
    ENABLE_HAREM = os.environ.get("ENABLE_HAREM", False)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", './fridaybot/DOWNLOADS/')
    LOGGER = True
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    # Here for later purposes
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    ALIVE_NAME = os.environ.get("ALIVE_NAME", "FridayUser")
    LESS_SPAMMY = os.environ.get("LESS_SPAMMY", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
    # Send .get_id in any channel to fill this value.
    PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", -100))
    NO_SONGS = bool(os.environ.get("NO_SONGS", False))
    PING_SERVERS = bool(os.environ.get("PING_SERVERS", False))
    DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
    if AUTH_TOKEN_DATA is not None:
        if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
            os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        t_file = open(TEMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    PRIVATE_GROUP_ID = int(os.environ.get("PRIVATE_GROUP_ID", False))
    NEWS_CHANNEL_ID = int(os.environ.get("NEWS_CHANNEL_ID", -100))
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
    ANTISPAM_SYSTEM = os.environ.get("ANTISPAM_SYSTEM", "DISABLE")
    WHITE_CHAT = set(int(x) for x in os.environ.get("WHITE_CHAT", "").split())
    # Get this value from my.telegram.org! Please do not steal
    LOCATION = os.environ.get("LOCATION", None)
    ALIVE_TEXT = os.environ.get("ALIVE_TEXT", None)
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    STRING_SESSION_2 = os.environ.get("STRING_SESSION_2", None)
    STRING_SESSION_3 = os.environ.get("STRING_SESSION_3", None)
    VIRUSTOTAL_API_KEY = os.environ.get("VIRUSTOTAL_API_KEY", None)
    GPLINKS_API_KEY = os.environ.get("GPLINKS_API_KEY", None)
    NSFW_FILTER_PM = os.environ.get("NSFW_FILTER_PM", True)
    SUPERHERO_API_KEY = os.environ.get("SUPERHERO_API_KEY", None)
    FOOTBALL_API_KEY = os.environ.get("FOOTBALL_API_KEY", None)
    SUB_TO_MSG_ASSISTANT = os.environ.get("SUB_TO_MSG_ASSISTANT", False)
    AUTO_SPELL_FIX = os.environ.get("AUTO_SPELL_FIX", False)
    # Get your own ACCESS_KEY from http://api.screenshotlayer.com/api/capture
    SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get(
        "SCREEN_SHOT_LAYER_ACCESS_KEY", None
    )
    # Send .get_id in any group to fill this value.
    # This is required for the modules involving the file system.
    TMP_DOWNLOAD_DIRECTORY = os.environ.get(
        "TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/"
    )
    # This is required for the speech to text module. Get your USERNAME from https://console.bluemix.net/docs/services/speech-to-text/getting-started.html
    IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
    IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
    # This is required for the hash to torrent file functionality to work.
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "Friday")
    # Get a Free API Key from OCR.Space
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    DEEP_API_KEY = os.environ.get("DEEP_API_KEY", None)
    PING_SERVER_EVERY_MINUTE_VALUE = int(os.environ.get("PING_SERVER_EVERY_MINUTE_VALUE", 30))
    DEEZER_ARL_TOKEN = os.environ.get("DEEZER_ARL_TOKEN", None)
    NOSPAMPLUS_TOKEN = os.environ.get("NOSPAMPLUS_TOKEN", None)
    # Send .get_id in any group with all your administration bots (added)
    G_BAN_LOGGER_GROUP = int(os.environ.get("G_BAN_LOGGER_GROUP", -1001198699233))
    # TG API limit. An album can have atmost 10 media!
    GOOGLE_SEARCH_COUNT_LIMIT = int(os.environ.get("GOOGLE_SEARCH_COUNT_LIMIT", 9))
    TG_GLOBAL_ALBUM_LIMIT = int(os.environ.get("TG_GLOBAL_ALBUM_LIMIT", 9))
    PRIVATE_GROUP_BOT_API_ID = int(
        os.environ.get("PRIVATE_GROUP_BOT_API_ID", False)
    )
    DISABLE_MARKDOWN = os.environ.get("DISABLE_MARKDOWN", False)
    # Load Spammy Plugins, Which can be harmful.
    LOAD_OTHER_PLUGINS = os.environ.get("LOAD_OTHER_PLUGINS", False)
    LOAD_OTHER_PLUGINS_CHNNL = os.environ.get("LOAD_OTHER_PLUGINS_CHNNL", "@fridayotherplugins")
    #
    # DO NOT EDIT BELOW THIS LINE IF YOU DO NOT KNOW WHAT YOU ARE DOING
    # TG API limit. A message can have maximum 4096 characters!
    MAX_MESSAGE_SIZE_LIMIT = 4095
    # set blacklist_chats where you do not want fridaybot's features
    UB_BLACK_LIST_CHAT = set(
        int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split()
    )
    # maximum number of messages for antiflood
    MAX_ANTI_FLOOD_MESSAGES = 10
    # warn mode for anti flood
    ANTI_FLOOD_WARN_MODE = ChatBannedRights(
        until_date=None, view_messages=None, send_messages=True
    )
    # chat ids or usernames, it is recommended to use chat ids,
    # providing usernames means an additional overhead for the user
    CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
    # Get your own API key from https://www.remove.bg/ or
    # feel free to use http://telegram.dog/Remove_BGBot
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    # Set to True if you want to block users that are spamming your PMs.
    SLAP_USERNAME = os.environ.get("SLAP_USERNAME", None)
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    NO_P_M_SPAM = bool(os.environ.get("NO_P_M_SPAM", False))
    # define "spam" in PMs
    NO_SONGS = bool(os.environ.get("NO_SONGS", False))
    MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
    # set to True if you want to log PMs to your PM_LOGGR_BOT_API_ID
    NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", False))
    # send .get_id in any channel to forward all your NEW PMs to this group
    PM_LOGGR_BOT_API_ID = os.environ.get("PM_LOGGR_BOT_API_ID", None)
    if PM_LOGGR_BOT_API_ID:
        PM_LOGGR_BOT_API_ID = int(PM_LOGGR_BOT_API_ID)
    # For Databases
    # can be None in which case modules requiring
    # DataBase would not work
    DB_URI = os.environ.get("DATABASE_URL", None)
    # number of rows of buttons to be displayed in .helpme command
    NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD = int(
        os.environ.get("NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD", 5)
    )
    # specify command handler that should be used for the modules
    # this should be a valid "regex" pattern
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "\.")
    SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", "\.")
    BOT_HANDLER = os.environ.get("BOT_HANDLER", "^/")
    # specify list of users allowed to use bot
    # WARNING: be careful who you grant access to your bot.
    # malicious users could do ".exec rm -rf /*"
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    WHITELIST_USERS = set(
        int(x) for x in os.environ.get("WHITELIST_USERS", "").split()
    )
    BLACKLIST_USERS = set(
        int(x) for x in os.environ.get("BLACKLIST_USERS", "").split()
    )
    DEVLOPERS = set(int(x) for x in os.environ.get("DEVLOPERS", "").split())
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "").split())
    SUPPORT_USERS = set(int(x) for x in os.environ.get("SUPPORT_USERS", "").split())
    # Very Stream
    VERY_STREAM_LOGIN = os.environ.get("VERY_STREAM_LOGIN", None)
    VERY_STREAM_KEY = os.environ.get("VERY_STREAM_KEY", None)
    GROUP_REG_SED_EX_BOT_S = os.environ.get(
        "GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot"
    )
    TEMP_DIR = os.environ.get("TEMP_DIR", None)
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    # Google Chrome Stuff
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/usr/bin/chromedriver")
    GOOGLE_CHROME_BIN = os.environ.get(
        "GOOGLE_CHROME_BIN", "/usr/bin/google-chrome"
    )
    # Google Drive ()
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    if AUTH_TOKEN_DATA != None:
        os.makedirs(TMP_DOWNLOAD_DIRECTORY)
        t_file = open(TMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    # MongoDB
    MONGO_URI = os.environ.get("MONGO_URI", None)
    # Lydia API
    LYDIA_API = os.environ.get("LYDIA_API", None)
    PRIVATE_GROUP_ID = int(os.environ.get("PRIVATE_GROUP_ID", False))
    PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", False))
    NEWS_CHANNEL_ID = int(os.environ.get("NEWS_CHANNEL_ID", False))
    JTM_CHANNEL_ID = int(os.environ.get("JTM_CHANNEL_ID", False))
    JTM_CHANNEL_USERNAME = os.environ.get("JTM_CHANNEL_USERNAME", None)
    FBAN_GROUP = int(os.environ.get("FBAN_GROUP", False))
    PM_DATA = os.environ.get("PM_DATA", "ENABLE")
    ENABLE_ASSISTANTBOT = os.environ.get("ENABLE_ASSISTANTBOT", "ENABLE")
    TAG_FEATURE = os.environ.get("TAG_FEATURE", "DISABLE")
    ANTISPAM_FEATURE = os.environ.get("ANTISPAM_FEATURE", "ENABLE")
    ASSISTANT_LOG = int(os.environ.get("ASSISTANT_LOG", False))
    UPSTREAM_REPO = os.environ.get(
        "UPSTREAM_REPO", "https://github.com/Starkgang/FridayUserbot"
    )
    ALIVE_IMAGE = os.environ.get(
        "ALIVE_IMAGE", "https://telegra.ph/file/22535f8051a58af113586.jpg"
    )
    ASSISTANT_START_PIC = os.environ.get(
        "ASSISTANT_START_PIC",
        "https://www.logolynx.com/images/logolynx/72/7257d2ac93b97c8a2c7308266052df13.png",
    )
    TESSDATA_PREFIX = os.environ.get(
        "TESSDATA_PREFIX", "/usr/share/tesseract-ocr/4.00/tessdata"
    )
