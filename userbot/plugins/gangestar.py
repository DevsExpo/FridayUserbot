import asyncio

from userbot.utils import friday_on_cmd


@friday.on(friday_on_cmd("gangastar ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Everybody")
        await asyncio.sleep(0.3)
        await event.edit("was")
        await asyncio.sleep(0.2)
        await event.edit("Gangestar")
        await asyncio.sleep(0.5)
        await event.edit("Until ")
        await asyncio.sleep(0.2)
        await event.edit("I")
        await asyncio.sleep(0.3)
        await event.edit("Arrived")
        await asyncio.sleep(0.3)
        await event.edit("🔥🔥🔥")
        await asyncio.sleep(0.3)
        await event.edit("Everybody was Gangestar Until I Arrived 🔥🔥🔥")
