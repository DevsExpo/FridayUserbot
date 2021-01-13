#By @shado_hackers for FRIDAY 
#If you steal this without credits You will be the geyest gey ever in the world that you will suck cat's dick.
from telethon import events
import asyncio
from ..utils import admin_cmd
from .. import ALIVE_NAME
from .. import CMD_HELP
import importlib.util

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"

@borg.on(admin_cmd(pattern="hbty$"))

async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 16)
    await event.edit("Starting...")
    animation_chars = [          
              "**Hello!**",
              "**How Are You?**",
              "[.](http://2.bp.blogspot.com/-WGLaIVbpK6U/WT4sr0LG2TI/AAAAAAAAVX0/1t0F3gECRh4okN6zJzq6fMwQ7dA4Qw8AwCLcB/s1600/happy-birthday-to-you.png)",
              "**Wishing you a day filled with happiness and a year filled with joy.**",
              "**Sending you smiles for every moment of your special day.**",
              "**Have a wonderful time and a very happy birthday!**",
              "**Count your life by smiles, not tears. Count your age by friends, not years. Happy birthday!**",
              "**I hope all your birthday wishes and dreams come true.**",
              "**Another adventure filled year awaits you. Welcome it by celebrating your birthday with pomp and splendor. Wishing you a very happy and fun-filled birthday!**",
              "**Happy birthday to someone who is smart, gorgeous, funny and reminds me a lot of myself… from one fabulous chick to another!**",
              "[.](http://www.handletheheat.com/wp-content/uploads/2015/03/Best-Birthday-Cake-with-milk-chocolate-buttercream-SQUARE.jpg)",
              "[.](http://i.pinimg.com/originals/49/d2/e3/49d2e318a2705cbd300e21023392ff6f.jpg)",
              "Here is also Gifts from me.",
              "[.](http://5.imimg.com/data5/KE/IK/MY-15644577/antique-gold-gift-box-luxury-rigid-box02-250x250.jpg)",
              "[.](http://i.pinimg.com/originals/10/b8/fb/10b8fb15270d8db1f6ff967e7026d2de.gif)",
              "[.](http://www.lovethispic.com/uploaded_images/367867-Starry-Happy-Birthday-Gif.gif)",
          ]
    for i in animation_ttl:#By @shado_hackers for FRIDAY
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i %16 ], link_preview=True)#By @NOOB_GUY_OP for Dark CObra
