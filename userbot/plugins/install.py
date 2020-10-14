import asyncio
import os
from datetime import datetime
from pathlib import Path

from userbot.utils import admin_cmd
from userbot.utils import edit_or_reply
from userbot.utils import load_module
from userbot.utils import remove_plugin
from userbot.utils import sudo_cmd

DELETE_TIMEOUT = 5


@borg.on(admin_cmd(pattern="install", outgoing=True))
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "userbot/plugins/",  # pylint:disable=E0602
                ))
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await event.edit(
                    "Friday Has Installed `{}` Sucessfully.".format(
                        os.path.basename(downloaded_file_name)))
            else:
                os.remove(downloaded_file_name)
                await event.edit(
                    "Errors! This plugin is already installed/pre-installed.")
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()
