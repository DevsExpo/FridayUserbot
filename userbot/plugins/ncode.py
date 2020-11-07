# Credits @Hackintush
# This software is a part of https://github.com/buddhhu/Plus
#
# Portedt by @Hackintush
#

import os

import pygments
from pygments.formatters import ImageFormatter
from pygments.lexers import Python3Lexer

from userbot.utils import friday_on_cmd


@friday.on(friday_on_cmd(pattern="ncode ?(.*)", allow_sudo=True))
async def coder_print(event):
    a = await event.client.download_media(
        await event.get_reply_message(), Var.TEMP_DOWNLOAD_DIRECTORY
    )
    s = open(a, "r")
    c = s.read()
    s.close()
    pygments.highlight(
        f"{c}",
        Python3Lexer(),
        ImageFormatter(font_name="DejaVu Sans Mono", line_numbers=True),
        "result.png",
    )
    res = await event.client.send_message(
        event.chat_id,
        "**Pasting this code on my page...**",
        reply_to=event.reply_to_msg_id,
    )
    await event.client.send_file(
        event.chat_id, "result.png", force_document=True, reply_to=event.reply_to_msg_id
    )
    # await event.client.send_file(event.chat_id, "resuly.png",
    # force_document=False, reply_to=event.reply_to_msg_id)
    await res.delete()
    await event.delete()
    os.remove(a)
    os.remove("result.png")
