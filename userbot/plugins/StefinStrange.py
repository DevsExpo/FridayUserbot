import requests , re , random 

import urllib , os 

from telethon.tl import functions

from datetime import datetime

from PIL import Image, ImageDraw, ImageFont

from userbot.utils import admin_cmd

import asyncio

from time import sleep

COLLECTION_STRINGZ = [

  "http://getwallpapers.com/collection/batman-hd-wallpapers-1080p", 

  "http://getwallpapers.com/collection/the-flash-4k-wallpaper", 

  "http://getwallpapers.com/collection/4k-deadpool-wallpaper", 
  
  "http://getwallpapers.com/collection/deathstroke-wallpapers-hd", 
  
  "http://getwallpapers.com/collection/joker-iphone-6-wallpaper", 

  "http://getwallpapers.com/collection/green-lantern-logo-wallpaper", 
  
  "http://getwallpapers.com/collection/batman-christmas-wallpaper", 

  "http://getwallpapers.com/collection/attack-on-titan-iphone-wallpaper", 

  "http://getwallpapers.com/collection/silver-surfer-wallpaper-hd", 

  "http://getwallpapers.com/collection/anti-venom-wallpaper", 

  "http://getwallpapers.com/collection/green-lantern-logo-wallpaper", 

  "http://getwallpapers.com/collection/batman-christmas-wallpaper", 

  "http://getwallpapers.com/collection/attack-on-titan-iphone-wallpaper", 

  "http://getwallpapers.com/collection/funny-deadpool-wallpapers", 

  "http://getwallpapers.com/collection/the-riddler-wallpaper-hd", 

  "http://getwallpapers.com/collection/batman-symbol-wallpaper-hd", 

  "http://getwallpapers.com/collection/sasuke-uchiha-hd-wallpaper", 

  "http://getwallpapers.com/collection/cw-flash-iphone-wallpaper", 

  "http://getwallpapers.com/collection/dc-raven-wallpaper", 

  "http://getwallpapers.com/collection/swamp-thing-wallpaper", 

  "http://getwallpapers.com/collection/superman-hd-wallpapers-1080p", 

  "http://getwallpapers.com/collection/dragon-pokemon-wallpapers", 

  "http://getwallpapers.com/collection/new-52-batman-wallpaper", 
  
  "http://getwallpapers.com/collection/avengers-hd-wallpapers-1080p", 
  
  "http://getwallpapers.com/collection/green-arrow-wallpaper-hd", 
  
  "http://getwallpapers.com/collection/agents-of-shield-wallpaper", 
 
  "http://getwallpapers.com/collection/dc-comics-hd-wallpaper", 
  
  "http://getwallpapers.com/collection/green-arrow-wallpaper-1920x1080", 
  
  "http://getwallpapers.com/collection/pokemon-super-mystery-dungeon-wallpaper", 
  
  "http://getwallpapers.com/collection/original-pokemon-wallpaper", 
  
  "http://getwallpapers.com/collection/batman-wallpaper-and-screensaver", 
  
  "http://getwallpapers.com/collection/spider-man-2099-hd-wallpaper", 
  
  "http://getwallpapers.com/collection/joker-harley-quinn-wallpaper", 
  
  "http://getwallpapers.com/collection/minimalist-marvel-wallpaper", 
  
  "http://getwallpapers.com/collection/darkseid-hd-wallpaper", 
  
  "http://getwallpapers.com/collection/thanos-wallpaper-hd", 
  
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

@borg.on(admin_cmd(pattern="wallpaperdp ?(.*)"))

async def main(event):

    await event.edit("**Starting Gamer Profile Pic...\n\nDone !!! Check Your DP") #Owner MarioDevs

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(3600) #Edit this to your required needs
