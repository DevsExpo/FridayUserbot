"""Emoji
Available Commands:
.support
"""
import asyncio

from userbot.utils import admin_cmd


@friday.on(admin_cmd("fridaybot"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "Read This Telegraph Whole info here":
    await event.edit("Thanks")
    animation_chars = [
        "Click here to Go to Telegraph",
        "[Click Here For Guide](https://telegra.ph/FRIDAY-06-15)",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
