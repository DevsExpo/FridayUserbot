import asyncio
import os
from datetime import datetime
from pathlib import Path

from userbot.utils import admin_cmd
from userbot.utils import load_module
from userbot.utils import remove_plugin
from userbot.utils import sudo_cmd


@borg.on(admin_cmd(pattern="load ?(.*)", outgoing=True))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match.group(1)
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        await event.edit(f"Successfully loaded {shortname}")
    except Exception as e:
        await event.edit(
            f"Could not load {shortname} because of the following error.\n{str(e)}"
        )


@borg.on(admin_cmd(pattern="unload ?(.*)", outgoing=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match.group(1)
    try:
        remove_plugin(shortname)
        await event.edit(f"Unloaded {shortname} successfully")
    except Exception as e:
        await event.edit(
            "Successfully unload {shortname}\n{}".format(shortname, str(e))
        )
