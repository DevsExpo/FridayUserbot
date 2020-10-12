# Copyright (C) Midhun KM
#
# Please Don't Kang Without Credits
# A Plugin For Assistant Bot
# x0x
import time
from datetime import datetime

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
from userbot import Lastupdate
from userbot.uniborgConfig import Config
from userbot.utils import admin_cmd
from userbot.utils import edit_or_reply
from userbot.utils import sudo_cmd


@tgbot.on(events.NewMessage(pattern="^/tr ?(.*)"))
async def _(event):
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "gu"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await tgbot.send_message(
            event.chat_id, "`.tr LanguageCode` as reply to a message"
        )
        return
    text = emoji.demojize(text.strip())
    lan = lan.strip()
    translator = Translator()
    translated = translator.translate(text, dest=lan)
    after_tr_text = translated.text
    output_str = (
        f"**Translated By Friday Assistant Bot** \n"
        f"Source {translated.src} \nTranslation {lan} \nWhat I Can Translate From This {after_tr_text}"
    )
    try:
        await tgbot.send_message(event.chat_id, output_str)
    except Exception as exc:
        await tgbot.send_message(event.chat_id, "Something Went Wrong 🤔")
