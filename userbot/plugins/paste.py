"""IX.IO pastebin like site
Syntax: .paste
From Pornhub"""
import logging
import os
from datetime import datetime

import requests
from uniborg.util import admin_cmd, sudo_cmd

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)


def progress(current, total):
    logger.info(
        "Downloaded {} of {}\nCompleted {}".format(
            current, total, (current / total) * 100
        )
    )


@borg.on(admin_cmd("paste ?(.*)"))
@borg.on(sudo_cmd("paste ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    datetime.now()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    input_str = event.pattern_match.group(1)
    if input_str:
        message = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            downloaded_file_name = await borg.download_media(
                previous_message,
                Config.TMP_DOWNLOAD_DIRECTORY,
                progress_callback=progress,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                # message += m.decode("UTF-8") + "\r\n"
                message += m.decode("UTF-8")
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message
    else:
        await event.edit("Give Some Text Or File To Paste")
    py_file = ""
    name = "ok"
    if previous_message.media:
        name = await borg.download_media(
            previous_message, Config.TMP_DOWNLOAD_DIRECTORY, progress_callback=progress
        )
    downloaded_file_name = name
    if downloaded_file_name.endswith(".py"):
        py_file += ".py"
        data = message
        key = (
            requests.post("https://nekobin.com/api/documents", json={"content": data})
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}{py_file}"
        raw = f"https://nekobin.com/raw/{key}{py_file}"
        reply_text = f"Pasted Text [neko]({url})\n Raw ? [View Raw]({raw})"
        await event.edit(reply_text)
    else:
        data = message
        key = (
            requests.post("https://nekobin.com/api/documents", json={"content": data})
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        raw = f"https://nekobin.com/raw/{key}"
        reply_text = f"Pasted Text [neko]({url})\n Raw ? [View Raw]({raw})"
        await event.edit(reply_text)
