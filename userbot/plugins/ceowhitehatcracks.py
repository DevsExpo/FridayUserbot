"""Emoji
Available Commands:
.ceowhitehatcracks
Credits to @CeoWhiteHatCracks
"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd


@borg.on(admin_cmd("ceowhitehatcracks"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.5
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "ceowhitehatcracks":
    await event.edit("@CeoWhiteHatCracks")
    animation_chars = [
            "@CeoWhiteHatCracks tera baap",
            "@CeoWhiteHatCracks is bot ka creator",
            "@CeoWhiteHatCracks bot ko jaan dene wala",
            "@CeoWhiteHatCracks owner of @Sensible_userbot ",
            "tujhe aur kya chaiye vo hai mere sath",
            "tera baap",
            "@CeoWhiteHatCracks"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
