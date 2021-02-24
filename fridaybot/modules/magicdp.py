
import asyncio
import os
import random
import re
import urllib
import requests
from telethon.tl import functions
from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd

COLLECTION_STRING = [
    "umbreon-wallpaper",
    "broly-wallpapers",
    "gorillaz-backgrounds",
    "lecrae-wallpapers",
    "demonic-wallpapers",
]
async def magic():
    await friday.run_cmd("rm -rf donot.jpg")
    rnd = random.randint(0, len(COLLECTION_STRING) - 1)
    pack = COLLECTION_STRING[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    #print(fy)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")


@friday.on(friday_on_cmd(pattern="magicdp"))
@friday.on(sudo_cmd(pattern="magicdp", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    
    ommhg = await friday.edit_or_reply(event, "Starting Your Magic Dp")
    
    while True:
        await magic()

        file = await event.client.upload_file("donottouch.jpg")

        await event.client(functions.photos.UploadProfilePhotoRequest(file))

        await friday.run_cmd("rm -rf donottouch.jpg")

        await asyncio.sleep(400)

    
    
    
 

CMD_HELP.update(
    {
        "magicdp": "**Magic Dp**\
\n\n**Syntax : **`.magicdp`\
\n**Usage :** Changes Profile Picture."
    }
)