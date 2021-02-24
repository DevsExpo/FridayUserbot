# Originally By @DeletedUser420
# Ported - @StarkxD

import asyncio
import os
import shlex
from typing import Tuple

from telegraph import Telegraph

from fridaybot import CMD_HELP
from fridaybot.Configs import Config
from fridaybot.utils import friday_on_cmd

telegraph = Telegraph()
tgnoob = telegraph.create_account(short_name="Friday 🇮🇳")


async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    """ run command in terminal """
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


@friday.on(friday_on_cmd(pattern="mediainfo$"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if reply_message is None:
        await event.edit("Reply To a Media.")
    await event.edit("`Processing...`")
    file_path = await borg.download_media(reply_message, Config.TMP_DOWNLOAD_DIRECTORY)
    out, err, ret, pid = await runcmd(f"mediainfo '{file_path}'")
    if not out:
        await event.edit("`Wtf, I Can't Determine This File Info`")
        return
    media_info = f"""
    <code>           
    {out}                  
    </code>"""
    title_of_page = "Media Info 🎬"
    ws = media_info.replace("\n", "<br>")
    response = telegraph.create_page(title_of_page, html_content=ws)
    km = response["path"]
    await event.edit(f"`This MediaInfo Can Be Found` [Here](https://telegra.ph/{km})")
    if os.path.exists(file_path):
        os.remove(file_path)


CMD_HELP.update(
    {
        "mediadata": "**Media Data**\
\n\n**Syntax : **`.mediainfo <reply to image>`\
\n**Usage :** Gives you information about the media."
    }
)
