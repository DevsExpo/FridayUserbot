# For UniBorg
# By Priyam Kalra
# Syntax (.hl <link>)
from userbot.utils import admin_cmd


@friday.on(admin_cmd(pattern="hl ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input = event.pattern_match.group(1)
    await event.edit("[ㅤㅤㅤㅤㅤㅤㅤ](" + input + ")")
