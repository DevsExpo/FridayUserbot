''' Whatever Plugin by Noobs of Telegram i.e. @TeleBotComms
    custom cmd: .hi2
'''

from telethon import events
import asyncio
import os
import sys
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern=r"hi2"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("🌺✨✨🌺✨🌺🌺🌺\n🌺✨✨🌺✨✨🌺✨\n🌺🌺🌺🌺✨✨🌺✨\n🌺✨✨🌺✨✨🌺✨\n🌺✨✨🌺✨🌺🌺🌺\n☁☁☁☁☁☁☁☁")
