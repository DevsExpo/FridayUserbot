#    Copyright (C) @DevsExpo 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
import pytz
import asyncio
from datetime import datetime
from pathlib import Path
from sys import argv
import os
import telethon.utils
from telethon import TelegramClient
from telethon import __version__ as tv
import sys
import platform
from fridaybot import bot, client2, client3, friday_version
from fridaybot.Configs import Config
from telethon.tl.types import InputMessagesFilterDocument
from fridaybot.tr_engines.engine import tr_engine
from fridaybot.utils import load_module, start_assistant, load_module_dclient, edit_or_reply
from fridaybot.Configs import Config
from fridaybot.function import runcmd, convert_to_image
from fridaybot.function.FastTelethon import upload_file

fridaydevs = logging.getLogger("Friday")


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.tr_engine = tr_engine
    bot.upload_to_server = upload_file
    bot.cig = convert_to_image
    bot.edit_or_reply = edit_or_reply
    bot.run_cmd = runcmd
    bot.uid = telethon.utils.get_peer_id(bot.me)
   
        
# Bleck Megic         
async def check_inline_on_warner(ws):
    w_s = await ws.get_me()
    if not w_s.bot_inline_placeholder:
        fridaydevs.info("Warning : We Have Detected That You Have Not Turned On Inline Mode For Your Assistant Bot, Please Go To @BotFather And Enable This.")
    return

Lol = "folyl's Token"

async def lol_s(client):
    client.me = await client.get_me()
    client.upload_to_server = upload_file
    client.tr_engine = tr_engine
    client.cig = convert_to_image
    client.run_cmd = runcmd
    client.edit_or_reply = edit_or_reply
    client.uid = telethon.utils.get_peer_id(client.me)
    
def multiple_client():
    if client2:
        fridaydevs.info("Starting Client 2")
        try:
            warnerstark = None
            client2.start()
            client2.loop.run_until_complete(lol_s(client2))
        except:
            warnerstark = True
            fridaydevs.info("Client 2 Failed To Load. Check Your String.")
    if client3:
        fridaydevs.info("Starting Client 3")
        try:
            chsaiujwal = None
            cleint3.start
            client3.loop.run_until_complete(lol_s(client3))
        except:
            chsaiujwal = True
            fridaydevs.info("Client 3 Failed To Load.")
    if not client2:
        warnerstark = True
    if not client3:
        chsaiujwal = True
    return warnerstark, chsaiujwal    

async def get_other_plugins(Config, client_s, fridaydevs):
    try:
        a_plugins = await client_s.get_messages(
            entity=Config.LOAD_OTHER_PLUGINS_CHNNL,
            filter=InputMessagesFilterDocument,
            limit=None,
            search=".py",
        )
    except:
        fridaydevs.info("Failed To Other Modules :(")
        return
    for meisnub in a_plugins:
        hmm = meisnub.media.document.attributes[-1].file_name
        pathh = "fridaybot/modules/"
        if os.path.exists(os.path.join(pathh, hmm)):
            pass
        else:
            await client_s.download_media(meisnub.media, "fridaybot/modules/")
    fridaydevs.info("Extra Plugins Downloaded.")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Config.TG_BOT_TOKEN_BF_HER is not None:
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
        ).start(bot_token=Config.TG_BOT_TOKEN_BF_HER)
        failed2, failed3 = multiple_client()
        bot.loop.run_until_complete(add_bot("RnJpZGF5VXNlckJvdCBpcyBCZXN0"))
    else:
        bot.loop.run_until_complete(add_bot("RnJpZGF5VXNlckJvdCBpcyBCZXN0"))
        failed2, failed3 = multiple_client()

if Config.LOAD_OTHER_PLUGINS:
        bot.loop.run_until_complete(get_other_plugins(Config, bot, fridaydevs))
        
import glob

path = "fridaybot/modules/*.py"
files = glob.glob(path)
failed_warner = 0
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
            load_module(shortname.replace(".py", ""))    
        except Exception as e:
            failed_warner += 1
            fridaydevs.info("------------------------")
            fridaydevs.info("Failed To Load : " + str(shortname.replace(".py", "")) + f" Error : {str(e)}")
            fridaydevs.info("------------------------")   
        if failed2 is None:
            try:
                load_module_dclient(shortname.replace(".py", ""), client2)
            except:
                pass
        if failed3 is None:
            try:
                load_module_dclient(shortname.replace(".py", ""), client3)
            except:
                pass

if Config.ENABLE_ASSISTANTBOT == "ENABLE":
    path = "fridaybot/modules/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            start_assistant(shortname.replace(".py", ""))
    wsta = "Friday And Assistant Bot Have Been Installed / Restarted Successfully !"
else:
    wsta = "Friday Has Been Installed / Restarted Sucessfully"

total_clients = 1
if failed2 is None:
    total_clients += 1
if failed3 is None:
    total_clients += 1
    
if wsta[0].lower() != Lol[0]:
   sys.exit("Bug Detected ! // UserBot is Exiting.")

TZ = pytz.timezone(Config.TZ)
datetime_tz = datetime.now(TZ)
strk = datetime_tz.strftime(f"Date : %d/%m/%Y \nTime : %H:%M")
sarg = (f"""{wsta}
-------------------------------------------
Friday-Userbot Based On Telethon V{tv}
Python Version : {platform.python_version()}
Friday-Userbot Version : V{friday_version}
Support Chat : @FridayChat
Updates Channel : @FridaySupportOfficial
Total Clients : {total_clients}
{strk}
-------------------------------------------""")
fridaydevs.info(sarg)

async def restart_log(bot):
    try:
        await bot.send_message(Config.PRIVATE_GROUP_ID, sarg)
    except:
        logger.warning("Invalid LOG Group ID! Please Check Your Log Group Id. For Now Friday is Exiting, Bye!")
        exit(1)
    return    

bot.loop.run_until_complete(restart_log(bot))
bot.tgbot.loop.run_until_complete(check_inline_on_warner(bot.tgbot))

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
