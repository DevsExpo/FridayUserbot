# Ported from other Telegram UserBots for TeleBot//Made for TeleBot
# Kangers, don't remove this line 
# @its_xditya

#Usage .actressdp Im Not Responsible For Any Ban caused By This

import requests , re , random 

import urllib , os 

from telethon.tl import functions

from userbot.utils import admin_cmd

import asyncio

COLLECTION_STRING = [

  "indian-actress-wallpapers",

  "latest-bollywood-actress-wallpapers-2018-hd",

  "bollywood-actress-wallpaper",

  "hd-wallpapers-of-bollywood-actress",

  "new-bollywood-actress-wallpaper-2018"

]

async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)

    pack = COLLECTION_STRING[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile('/\w+/full.+.jpg')

    f = f.findall(pc)

    fy = "http://getwallpapers.com"+random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")

    urllib.request.urlretrieve(fy,"donottouch.jpg")

@borg.on(admin_cmd(pattern="actressdp ?(.*)"))

async def main(event):

    await event.edit("**Starting Actress Profile Pic...\n\nDone !!! Check Your DP in 5 seconds. \n By [TeleBot](https://github.com/xditya/TeleBot)**")

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(600) #Edit this to your required needs

