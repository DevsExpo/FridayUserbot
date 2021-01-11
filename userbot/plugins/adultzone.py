import asyncio
import os
import urllib

import requests

from userbot import *
from userbot.utils import *

sedpath = "./cipherx/"


@bot.on(admin_cmd("boobs$"))
@bot.on(sudo_cmd(pattern="boobs$", allow_sudo=True))
async def boobs(event):
    reply = await event.get_reply_message()
    if not os.path.isdir(sedpath):
        os.makedirs(sedpath)
    pic_loc = os.path.join(sedpath, "boobs.jpg")
    a = await event.reply("Finding some big boobs 🧐")
    await asyncio.sleep(0.5)
    await a.edit("Sending some big boobs🤪")
    nsfw = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(
        event.chat_id, pic_loc, force_document=False, reply_to=reply.id
    )
    os.remove(pic_loc)
    await event.delete()
    await a.delete()


@bot.on(admin_cmd("butts$"))
@bot.on(sudo_cmd(pattern="butts$", allow_sudo=True))
async def butts(event):
    reply = await event.get_reply_message()
    if not os.path.isdir(sedpath):
        os.makedirs(sedpath)
    pic_loc = os.path.join(sedpath, "butts.jpg")
    a = await event.reply("Finding some beautiful butts🧐")
    await asyncio.sleep(0.5)
    await a.edit("Sending some beautiful butts🤪")
    nsfw = requests.get("http://api.obutts.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.obutts.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(
        event.chat_id, pic_loc, force_document=False, reply_to=reply.id
    )
    os.remove(pic_loc)
    await event.delete()
    await a.delete()


CMD_HELP.update(
    {
        "adultzone": "**Plugin : **`adultzone`\
        \n\n**Syntax : **`.boobs`\
        \n**Usage :** Searchs and sends random B××Bs image\
        \n\n**Syntax :**`.butts`\
        \n**Usage :** Searchs and sends random Butts image\
        \n\n\n     __**WARNING!! 18+ MODULE**__"
    }
)
