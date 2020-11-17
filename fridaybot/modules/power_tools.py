"""Restart or Terminate the bot from any chat
Available Commands:
.restart
.shutdown"""
import os
import sys

from fridaybot.utils import friday_on_cmd


@friday.on(friday_on_cmd("restart"))
async def _(event):
    if event.fwd_from:
        return
    # await asyncio.sleep(2)
    # await event.edit("Restarting [░░░] ...\n`.ping` me or `.help` to check if I am online after a lil bit.")
    # await asyncio.sleep(2)
    # await event.edit("Restarting [█░░] ...\n`.ping` me or `.help` to check if I am online after a lil bit.")
    # await asyncio.sleep(2)
    # await event.edit("Restarting [██░] ...\n`.ping` me or `.help` to check if I am online after a lil bit.")
    # await asyncio.sleep(2)
    # await event.edit("Restarting [███]...\n`.ping` me or `.help` to check if I am online after a lil bit.")
    # await asyncio.sleep(2)
    await event.edit("Restarted! `.ping` me or `.helpme` to check if I am online")
    await borg.disconnect()
    # https://archive.is/im3rt
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@friday.on(friday_on_cmd("shutdown"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Turning Off... Manually Turn Me On Later")
    await borg.disconnect()
