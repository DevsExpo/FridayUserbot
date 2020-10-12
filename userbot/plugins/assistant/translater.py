# Copyright (C) Midhun KM
#
# Please Don't Kang Without Credits
# A Plugin For Assistant Bot
# x0x

from telethon import events, custom, Button
from telethon.tl.types import Channel, Chat, User

import emoji
from googletrans import Translator
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from telethon.utils import get_display_name
from userbot.utils import admin_cmd, sudo_cmd
from userbot.uniborgConfig import Config
from telethon import events
from userbot import bot
from datetime import datetime
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
import time
from userbot import Lastupdate


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
