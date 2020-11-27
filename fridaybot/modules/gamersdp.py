import asyncio
import os
import random
import re
import urllib

import requests
from telethon.tl import functions

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd

COLLECTION_STRINGZ = [
    "star-wars-wallpaper-1080p",
    "4k-sci-fi-wallpaper",
    "star-wars-iphone-6-wallpaper",
    "kylo-ren-wallpaper",
    "darth-vader-wallpaper",
]


async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRINGZ) - 1)

    pack = COLLECTION_STRINGZ[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile("/\w+/full.+.jpg")

    f = f.findall(pc)

    fy = "http://getwallpapers.com" + random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )

    urllib.request.urlretrieve(fy, "donottouch.jpg")


@friday.on(friday_on_cmd(pattern="gamerdp ?(.*)"))
async def main(event):

    await event.edit(
        "**Starting Gamer Profile Pic...\n\nDone !!! Check Your DP"
    )  # Owner @NihiNivi

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")

        await event.client(functions.photos.UploadProfilePhotoRequest(file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(3600)  # Edit this to your required needs


CMD_HELP.update(
    {
        "gamersdp": "**Gamersdp**\
\n\n**Syntax : **`.gamerdp`\
\n**Usage :** Use this plugin to automatically change your profile picture to gaming pictures"
    }
)
