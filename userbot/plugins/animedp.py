#Made By @TeleBotHelp Keep Credits If You Are Goanna Kang This Lol

#And Thanks To The Creator Of Autopic This Script Was Made from Snippets From That Script

#Usage .actressdp Im Not Responsible For Any Ban caused By This

import requests , re , random 

import urllib , os 

from telethon.tl import functions

from userbot.utils import admin_cmd

import asyncio

COLLECTION_STRING = [

  "cute-anime-wallpapers-hd",

  "anime-christmas-wallpaper-hd",

  "anime-samurai-girl-wallpaper",

  "4k-anime-wallpapers",

  "2560-x-1440-wallpaper-anime"

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

@borg.on(admin_cmd(pattern="animedp ?(.*)"))

async def main(event):

    await event.edit("**Starting Anime Profile Pic...\n\nDone !!! Check Your DP in 5 seconds. By [TeleBot](https://github.com/xditya/TeleBot)**")

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(600) #Edit this to your required needs

