from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("whoami"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0,36)
    await event.edit("Hello ")
    animation_chars = [
            "I",
            "am",
            "Ramandeep Singh",
            "I am [Ramandeep Singh](http://t.me/ramanveerji).
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])