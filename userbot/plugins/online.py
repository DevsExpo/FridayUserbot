# Copyright TeleBot
# For @TeleBotHelp coded by @xditya
# Kangers keep credits else I'll take down 🧐

import sys
from telethon import events, functions, version, __version__
import random
from userbot.utils import register
from userbot import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet, check pinned in @TeleBotHelp"

ONLINESTR = [
	"█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ \n█░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░█  █░║║║╠─║─║─║║║║║╠─░█ \n█░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░█ \n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█ \n\n**TeleBot is online.**\n\n**All systems functioning normally !** \n\n**Bot by** [☣️🇦 🇵 🇽 🇩 ☣️](https://t.me/AP_XD) \n\n**More help -** @TeleBotHelpChat \n\n           [🚧 GitHub Repository 🚧](https://github.com/xditya/TeleBot)",
	f"╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗\n║║║╠─║─║─║║║║║╠─\n╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝\n              **Welcome to TeleBot**\n\n**Hey master! I'm alive. All systems online and functioning normally ✅**\n\n**✔️ Telethon version:** `{version.__version__}` \n\n**✔️ Python:** `{sys.version}` \n\n✔️ More info: @TeleBotHelpChat \n\n✔️ Created by: [Aditya 🇮🇳](tg://user?id=719195224) \n\n**✔️ Database status:** All ok 👌 \n\n**✔️ My master:** {DEFAULTUSER} \n\n        [🌟 Github repository 🌟](https://github.com/xditya/TeleBot)"
]

@register(outgoing=True, pattern="^.online$")
async def online(event):
    """ Greet everyone! """
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(random.choice(ONLINESTR))
