import asyncio
import time

from telethon.tl.functions.channels import LeaveChannelRequest

from fridaybot import CMD_HELP, bot
from fridaybot.utils import friday_on_cmd


@friday.on(friday_on_cmd("leave$"))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`My Boss is Leaving This Basterd Chat!`")
        time.sleep(3)
        if "-" in str(e.chat_id):
            await bot(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit("`But, Boss! This is Not A Chat`")
