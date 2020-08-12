#python 3.7.1

import time
import os,sys
"""Available Commands:
.gay"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("(.*)"))

async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    input_str = event.pattern_match.group(1)
    if input_str == "gay":
        await event.edit(input_str)
        animation_chars = [
            "HI USER",
            "HI USER , WAIT",
            "HI USER , WAIT ARE YOU....",
            "HI USER , WAIT ARE YOU UMH...",
            "HI USRR , WAIT ARE YOU A GAY??😬"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i %5 ])