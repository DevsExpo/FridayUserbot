import time
from datetime import datetime

import emoji
from googletrans import Translator
from telethon import Button
from telethon import custom
from telethon import events
from telethon import utils
from telethon.tl import types
from telethon.tl.types import Channel
from telethon.tl.types import Chat
from telethon.tl.types import User
from telethon.utils import get_display_name

from userbot import bot
from userbot import Lastupdate
from userbot.plugins.sql_helper.snips_sql import add_snip
from userbot.plugins.sql_helper.snips_sql import get_all_snips
from userbot.plugins.sql_helper.snips_sql import get_snips
from userbot.plugins.sql_helper.snips_sql import remove_snip
from userbot.uniborgConfig import Config
from userbot.utils import admin_cmd
from userbot.utils import edit_or_reply
from userbot.utils import sudo_cmd

TYPE_TEXT = 0
TYPE_PHOTO = 1
TYPE_DOCUMENT = 2


@tgbot.on(events.NewMessage(pattern=r"\?(\S+)"))
async def on_snip(event):
    name = event.pattern_match.group(1)
    snip = get_snips(name)
    if snip:
        if snip.snip_type == TYPE_PHOTO:
            media = types.InputPhoto(
                int(snip.media_id),
                int(snip.media_access_hash),
                snip.media_file_reference,
            )
        elif snip.snip_type == TYPE_DOCUMENT:
            media = types.InputDocument(
                int(snip.media_id),
                int(snip.media_access_hash),
                snip.media_file_reference,
            )
        else:
            media = None
        message_id = event.message.id
        if event.reply_to_msg_id:
            message_id = event.reply_to_msg_id
        await tgbot.send_message(event.chat_id,
                                 snip.reply,
                                 reply_to=message_id,
                                 file=media)


@tgbot.on(
    events.NewMessage(pattern="^/addnote ?(.*)",
                      func=lambda e: e.sender_id == bot.uid))
async def _(event):
    name = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if msg:
        snip = {"type": TYPE_TEXT, "text": msg.message or ""}
        if msg.media:
            media = None
            if isinstance(msg.media, types.MessageMediaPhoto):
                media = utils.get_input_photo(msg.media.photo)
                snip["type"] = TYPE_PHOTO
            elif isinstance(msg.media, types.MessageMediaDocument):
                media = utils.get_input_document(msg.media.document)
                snip["type"] = TYPE_DOCUMENT
            if media:
                snip["id"] = media.id
                snip["hash"] = media.access_hash
                snip["fr"] = media.file_reference
        add_snip(
            name,
            snip["text"],
            snip["type"],
            snip.get("id"),
            snip.get("hash"),
            snip.get("fr"),
        )
        await event.reply(
            "Note {name} saved successfully. Get it with ?{name}".format(
                name=name))
    else:
        await event.reply(
            "Reply to a message with `snips keyword` to save the snip")


@tgbot.on(events.NewMessage(pattern="^/notes"))
async def on_snip_list(event):
    all_snips = get_all_snips()
    OUT_STR = "Available Snips:\n"
    if len(all_snips) > 0:
        for a_snip in all_snips:
            OUT_STR += f"➤ `?{a_snip.snip}` \n"
    else:
        OUT_STR = "No Snips. Start Saving using `/addnote`"
    if len(OUT_STR) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "snips.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="Available Snips",
                reply_to=event,
            )
    else:
        await event.reply(OUT_STR)


@tgbot.on(
    events.NewMessage(pattern=r"^/rmnote (\S+)",
                      func=lambda e: e.sender_id == bot.uid))
async def on_snip_delete(event):
    name = event.pattern_match.group(1)
    remove_snip(name)
    await event.reply("Note ?{} deleted successfully".format(name))
