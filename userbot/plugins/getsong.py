# Downloads songs from Spotify
# Keep credits if gonna kang...do not remove/edit this line..
# Else gay..

from telethon import events
import subprocess
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
import io
import asyncio
import time
from userbot.utils import admin_cmd
import glob
import os
import spotdl
import subprocess

@borg.on(admin_cmd(pattern="getsong ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("**Getting Your Music it may take a few seconds to fetch the song and download it...**")
    DELAY_BETWEEN_EDITS = 0.1
    PROCESS_RUN_TIME = 100
    cmd = event.pattern_match.group(1)
    cmnd = f"{cmd}"
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    subprocess.run(["spotdl", "-s", cmnd, "-q", "best"])
    subprocess.run(
        'for f in *.opus; do      mv -- "$f" "${f%.opus}.mp3"; done',
        shell=True)
    l = glob.glob("*.mp3")
    loa = l[0]
    await event.edit("`Yeah, I found the song..🎶`")
    await event.client.send_file(
        event.chat_id,
        loa,
        force_document=False,
        allow_cache=False,
        supports_streaming=True,
        caption='Uploaded successfully',
        reply_to=reply_to_id,
    )
    subprocess.run("rm -rf *.mp3", shell=True)
