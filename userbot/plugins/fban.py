# MIDHUN K M
# (C) BY MIDHUN
# FOR FRIDAY
import asyncio

from userbot.plugins.sql_helper.fban_sql import (add_fed_in_db,
                                                 already_added_fed,
                                                 get_all_fed, remove_fed)
from userbot.utils import admin_cmd


@borg.on(admin_cmd("fadd ?(.*)"))
async def addfed(event):
    if event.fwd_from:
        return
    sedlyf = event.pattern_match.group(1)
    if already_added_fed(sedlyf):
        await event.edit("`Fed Already Added`")
        await asyncio.sleep(3)
        await event.delete()
    elif not already_added_fed(sedlyf):
        add_fed_in_db(sedlyf)
        await event.edit("`Fed Added`")
        await asyncio.sleep(3)
        await event.delete()
