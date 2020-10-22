from telethon.utils import pack_bot_file_id
from userbot.utils import friday_on_cmd, edit_or_reply, sudo_cmd
from userbot import bot
from telethon import events, custom, Button
from telethon.tl.types import (
    Channel,
    Chat,
    User
)

import emoji
import asyncio
from googletrans import Translator
import re
import io
from math import ceil
from userbot.plugins import inlinestats
from telethon import custom, events, Button
from userbot import CMD_LIST
from userbot.utils import friday_on_cmd, edit_or_reply, sudo_cmd
from telethon.utils import get_display_name
from userbot.utils import friday_on_cmd, sudo_cmd
from userbot.uniborgConfig import Config
from telethon import events
from datetime import datetime
from userbot.utils import friday_on_cmd, edit_or_reply, sudo_cmd
import time
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from userbot import Lastupdate, bot
from userbot.plugins.sql_helper.botusers_sql import add_me_in_db, his_userid
from userbot.plugins.sql_helper.idadder_sql import add_usersid_in_db, get_all_users
import time
from uniborg.util import friday_on_cmd, sudo_cmd
from userbot import ALIVE_NAME
from datetime import datetime
from userbot import Lastupdate
from userbot.plugins import currentversion

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://filetolinktelegrambot.herokuapp.com/1996057911608/VID_20200723_004420.mp4"
pm_caption = "`➥ CɪᴘʜᴇʀX Super Technology Assistant Bot is:` **Online**\n\n"
pm_caption += "➥ **System Status**\n"
pm_caption += "`➥ Telethon Version:` **6.0.9**\n`Python:` **3.8.5**\n"
pm_caption += "`➥ Database Status:` **AWS Working Properly**\n"
pm_caption += "**➥ Current Branch** : `Master`\n"
pm_caption += "**➥ CɪᴘʜᴇʀX OS** : `Kali GNU/Linux Rolling x86_64`\n"
pm_caption += f"**➥ My Boss** : [CɪᴘʜᴇʀX](https://t.me/Hackintush)\n"
pm_caption += "**✨ CɪᴘʜᴇʀX is the best ✨**" 

# only Owner Can Use it 
@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def friday(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
