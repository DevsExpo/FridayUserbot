import asyncio
import os
from datetime import datetime
from pathlib import Path

from userbot.utils import friday_friday_friday_sudo_cmd
from userbot.utils import friday_on_cmd
from userbot.utils import load_module
from userbot.utils import remove_plugin


@friday.on(friday_on_cmd(pattern="load ?(.*)", outgoing=True))
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


@friday.on(friday_on_cmd(pattern="unload ?(.*)", outgoing=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match.group(1)
    try:
        remove_plugin(shortname)
        await event.edit(f"Unloaded {shortname} successfully")
    except Exception as e:
        await event.edit("Successfully unload {shortname}\n{}".format(
            shortname, str(e)))
