"""Reply to an image/sticker with .mmf` 'text on top' ; 'text on bottom
base by: @r4v4n4
created by: @A_Dark_Princ3
"""

import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import MessageMediaPhoto
from uniborg.util import friday_on_cmd

from fridaybot import CMD_HELP

thumb_image_path = Config.TMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"


@friday.on(friday_on_cmd("mmf ?(.*)"))
async def _(event):
    hmm = event.chat_id
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Syntax: reply to an image with .mmf And Text `")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("```reply to a image/sticker/gif```")
        return
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    else:
        await event.edit(
            "```Transfiguration Time! Mwahaha memifying this image! (」ﾟﾛﾟ)｣ ```"
        )
    await borg.download_file(reply_message.media)

    async with borg.conversation("@TgMemeRobot") as conv:
        try:
            kekbruh = event.pattern_match.group(1)
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("/create")
            await asyncio.sleep(1)
            await conv.send_file(reply_message.media)
            await asyncio.sleep(3)
            await conv.send_message(kekbruh)
            response = await conv.get_response()
            await conv.mark_read(message=response)
            den = response.media
            await borg.send_file(hmm, den)
        except YouBlockedUserError:
            await event.reply("```Please unblock @TgMemeRobot and try again```")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good nibba?```"
            )
        if "This is" in response.text:
            await event.edit(
                "```🤨 NANI?! This is not an image! This will take sum tym to convert to image owo 🧐```"
            )


def is_message_image(message):
    if message.media:
        if isinstance(message.media, MessageMediaPhoto):
            return True
        if message.media.document:
            if message.media.document.mime_type.split("/")[0] == "image":
                return True
        return False
    return False


CMD_HELP.update(
    {
        "memify": "**Memify**\
\n\n**Syntax : **`.mmf <Reply to an image/sticker and mention uppertext;lowertext>`\
\n**Usage :** create memes easily with this plugin."
    }
)
