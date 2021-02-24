# All 3 Clients
from telethon import TelegramClient
import logging
from telethon.sessions import StringSession
from fridaybot.Configs import Config

starky = logging.getLogger("ALERT")

if not Config.STRING_SESSION:
    starky.warning("String Session is Missing, UserBot is Quiting. Please Check ReadMe !")
    quit(1)

if not Config.APP_ID:
    starky.warning("Api ID is Missing, UserBot is Quiting. Please Check ReadMe !")
    quit(1)

if not Config.API_HASH:
    starky.warning("Api Hash is Missing, UserBot is Quiting. Please Check ReadMe !")
    quit(1)

if not Config.PRIVATE_GROUP_ID:
    starky.warning("Please Add Private Group ID For Proper Functioning Of UserBot.")
    quit(1)
    
if not Config.TG_BOT_TOKEN_BF_HER:
    starky.warning("Please Add Private Group ID For Proper Functioning Of UserBot.")
    quit(1)
    
if not Config.DB_URI:    
    starky.warning("Please Add Database Url For Proper Functioning Of UserBot.")
    quit(1)
    
if Config.STRING_SESSION:
    session_name = str(Config.STRING_SESSION)
    bot = TelegramClient(StringSession(session_name), Config.APP_ID, Config.API_HASH)
else:
    session_name = "startup"
    bot = TelegramClient(session_name, Config.APP_ID, Config.API_HASH)
if Config.STRING_SESSION_2:
    client2 =  TelegramClient(StringSession(Config.STRING_SESSION_2), Config.APP_ID, Config.API_HASH)
else:
    client2 = None
if Config.STRING_SESSION_3:
    client3 =  TelegramClient(StringSession(Config.STRING_SESSION_3), Config.APP_ID, Config.API_HASH)
else:
    client3 = None
