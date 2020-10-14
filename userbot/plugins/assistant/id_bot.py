import asyncio
import io
import re
import time
from datetime import datetime
from math import ceil

import emoji
from googletrans import Translator
from telethon import Button
from telethon import custom
from telethon import events
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import Channel
from telethon.tl.types import Chat
from telethon.tl.types import User
from telethon.utils import get_display_name
from telethon.utils import pack_bot_file_id

from userbot import bot
from userbot import CMD_LIST
from userbot import Lastupdate
from userbot.plugins import inlinestats
from userbot.plugins.sql_helper.botusers_sql import add_me_in_db
from userbot.plugins.sql_helper.botusers_sql import his_userid
from userbot.plugins.sql_helper.idadder_sql import add_usersid_in_db
from userbot.plugins.sql_helper.idadder_sql import get_all_users
from userbot.uniborgConfig import Config
from userbot.utils import admin_cmd
from userbot.utils import edit_or_reply
from userbot.utils import sudo_cmd


@tgbot.on(events.NewMessage(pattern="^/id"))
async def _(event):
    if event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await tgbot.send_message(
                event.chat_id,
                "Current Chat ID: `{}`\nFrom User ID: `{}`\nBot API File ID: `{}`"
                .format(str(event.chat_id), str(r_msg.from_id),
                        bot_api_file_id),
            )
        else:
            await tgbot.send_message(
                event.chat_id,
                "Current Chat ID: `{}`\nFrom User ID: `{}`".format(
                    str(event.chat_id), str(r_msg.from_id)),
            )
    else:
        await tgbot.send_message(
            event.chat_id, "Current Chat ID: `{}`".format(str(event.chat_id)))
