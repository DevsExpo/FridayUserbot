#    Copyright (C) Midhun KM
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
import re
import time
from datetime import datetime
from math import ceil

import emoji
from googletrans import Translator
from telethon import Button
from telethon import custom
from telethon import events
from telethon.tl.types import Channel
from telethon.tl.types import Chat
from telethon.tl.types import User
from telethon.utils import get_display_name

from userbot import bot
from userbot import CMD_LIST
from userbot import Lastupdate
from userbot.plugins import inlinestats
from userbot.plugins.sql_helper.botusers_sql import add_user_to_db
from userbot.uniborgConfig import Config
from userbot.utils import admin_cmd
from userbot.utils import edit_or_reply
from userbot.utils import sudo_cmd


@tgbot.on(events.NewMessage(pattern="^/start"))
async def start(event):
    vent = event.chat_id
    starttext = "Hi! this is An Assistant Bot For My [Owner] "
    if event.from_id == bot.uid:
        await tgbot.send_message(
            vent,
            message="Hi Master, It's Me Your Assistant.",
            buttons=[
                [custom.Button.inline("Broadcast 🔥", data="mebroadcast")],
                [Button.url("Repo?", "https://github.com/StarkGang/FridayUserbot")],
                [Button.url("Join Channel 📃", "t.me/Fridayot")],
            ],
        )
    else:
        await tgbot.send_message(
            event.chat_id,
            message=starttext,
            link_preview=False,
            buttons=[
                [custom.Button.inline("Deploy your Friday 🇮🇳", data="deploy")],
                [Button.url("Help Me ❓", "t.me/Fridayot")],
            ],
        )


# Data's


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"deploy")))
async def help(event):
    await event.delete()
    if event.query.user_id is not bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message="You Can Deploy Friday In Heroku By Following Steps Bellow, You Can See Some Quick Guides On Support Channel Or On Your Own Assistant Bot. \nThank You For Contacting Me.",
            buttons=[
                [Button.url("Deploy Tutorial 📺", "https://youtu.be/xfHcm_e92eQ")],
                [Button.url("Need Help ❓", "t.me/FridaySupportOfficial")],
            ],
        )


# Bot Permit.
@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def all_messages_catcher(event):
    ignore = ["/start", "/tr", "/ping", "fuck", "madarchod"]
    sedlyfvro = event.raw_text
    if any(a in event.raw_text for a in ignore):
        pass
    elif event.chat_id == bot.uid:
        pass
    else:
        sender = await event.get_sender()
        chat_id = event.chat_id
        sed = await event.forward_to(bot.uid)

        # Add User To Database ,Later For Broadcast Purpose
        # (C) @SpecHide
        add_user_to_db(sed.id, event.sender_id, event.from_id)


# Test
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"mebroadcast")))
@tgbot.on(events.NewMessage)
async def sed(event):
    replied = event.raw_text
    tgbot.send_message(event.chat_id, replied)
    await tgbot.send_message("Ok, Broadcasting This Message")
