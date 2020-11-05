"""By STARKTM1
cmd : .plane"""
import asyncio

from telethon import events


@borg.on(events.NewMessage(pattern=r"\.plane", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("✈-------------")
    await event.edit("-✈------------")
    await event.edit("--✈-----------")
    await event.edit("---✈----------")
    await event.edit("----✈---------")
    await event.edit("-----✈--------")
    await event.edit("------✈-------")
    await event.edit("-------✈------")
    await event.edit("--------✈-----")
    await event.edit("---------✈----")
    await event.edit("----------✈---")
    await event.edit("-----------✈--")
    await event.edit("------------✈-")
    await event.edit("-------------✈")
    await asyncio.sleep(3)
    await event.delete()
