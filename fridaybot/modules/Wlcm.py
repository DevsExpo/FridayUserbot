# Credit To @Helloji123bot . Keep credit if you are going to edit it.


import random
import re
from uniborg.util import admin_cmd
import asyncio
from telethon import events


@borg.on(admin_cmd(pattern="wlcm ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):

        await event.edit("**💛💚💙💜🖤❤️🧡\n💜💚welcome💙...\n💛💚💙💜🖤❤️🧡\n**")
        await asyncio.sleep(1.3)
        await event.edit("**💚💙💜🖤❤️🧡💛\n💚💙💜welcome...\n💚💙💜🖤❤️🧡💛\n**")

        await asyncio.sleep(2)
        await event.edit("**───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n───█▒▒░░░░░░░░░▒▒█───\n────█░░█░░░░░█░░█────\n─▄▄──█░░░▀█▀░░░█──▄▄─\n█░░█─▀▄░░░░░░░▄▀─█░░█\n█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n**")
