# MIDHUN K M
# (C) BY MIDHUN
# FOR FRIDAY
from userbot.plugins.sql_helper.fban_sql import add_fed_in_db
from userbot.plugins.sql_helper.fban_sql import already_added_fed
from userbot.plugins.sql_helper.fban_sql import get_all_fed
from userbot.plugins.sql_helper.fban_sql import remove_fed
from userbot.utils import admin_cmd
import asyncio


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
