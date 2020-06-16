import requests , re , random 

import urllib , os 

from telethon.tl import functions

from datetime import datetime

from PIL import Image, ImageDraw, ImageFont

from userbot.utils import admin_cmd

import asyncio

from time import sleep

COLLECTION_STRINGZ = [

  "4K Deadpool Wallpaper",

  "Batman HD Wallpapers 1080p", 

  "The Flash 4K Wallpaper", 

  "Deathstroke Wallpapers HD", 

  "Joker iPhone 6 Wallpaper", 
  
  "Green Lantern Logo Wallpaper", 
  
  "Batman Christmas Wallpaper", 
  
  "Funny Deadpool Wallpapers", 
  
  "The Riddler Wallpaper HD",
  
  "Batman Symbol Wallpaper HD", 
  
  "Cw Flash iPhone Wallpaper", 
  
  "DC Raven Wallpaper", 
  
  "Swamp Thing Wallpaper", 
  
  "Superman HD Wallpapers 1080p", 
  
  "New 52 Batman Wallpaper", 
  
  "Avengers HD Wallpapers 1080p", 
  
  "Green Arrow Wallpaper HD", 
  
  "Agents of Shield Wallpaper", 
  
  "DC Comics HD Wallpaper", 
  
  "Joker Harley Quinn Wallpaper", 
  
  
]



async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRINGZ) - 1)

    pack = COLLECTION_STRINGZ[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile('/\w+/full.+.jpg')

    f = f.findall(pc)

    fy = "http://getwallpapers.com"+random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")

    urllib.request.urlretrieve(fy,"donottouch.jpg")

@borg.on(admin_cmd(pattern="wallpaper ?(.*)"))

async def main(event):

    await event.edit("**Starting Gamer Profile Pic...\n\nDone !!! Check Your DP") #Owner MarioDevs

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(3600) #Edit this to your required needs
