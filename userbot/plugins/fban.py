# MIDHUN K M
# (C) BY MIDHUN
# FOR FRIDAY
from userbot.plugins.sql_helper.fban_sql import add_fed_in_db
from userbot.plugins.sql_helper.fban_sql import already_added_fed
from userbot.plugins.sql_helper.fban_sql import get_all_fed
from userbot.plugins.sql_helper.fban_sql import remove_fed
from userbot.utils import admin_cmd


@borg.on(admin_cmd("fadd ?(.*)"))
async def addfed(event):
    if event.fwd_from:
        return
    sedlyf = event.pattern_match.group(1)
    if not already_added_fed(sedlyf):
        add_fed_in_db(sedlyf)
        await edit_or_reply("`Added Fed Successfuly To List`")
        await asyncio.sleep(3)
        await event.delete()
    elif already_added_fed(sedlyf):
        await event.edit("`Fed is already is database!`")
        await asyncio.sleep(3)
        await event.delete()
