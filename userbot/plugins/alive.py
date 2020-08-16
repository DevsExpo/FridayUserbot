#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/e4d5011aa1fd76b742649.png"
pm_caption = "`FRIDAY IS:` **ONLINE**\n\n"
pm_caption += "**SYSTEM STATUS**\n"
pm_caption += "`TELETHON VERSION:` **1.15.0**\n`Python:` **3.8.3**\n"
pm_caption += "`DATABASE STATUS:` **Functional**\n"
pm_caption += "**Current Branch** : `master`\n"
pm_caption += "**Friday OS** : `3.14`\n"
pm_caption += "**Current Sat** : `☣️🇦 🇵 🇽 🇩 ☣️Sat-6.96`\n"
pm_caption += f"**My Peru Owner** : {DEFAULTUSER} \n"
pm_caption += "**Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "**License** : [MIT Licence](github.com/APXD-git/FridayUserbot/blob/master/LICENSE)\n"
pm_caption += "Copyright : By [☣️🇦 🇵 🇽 🇩 ☣️@Github](github.com/APXD-git/FridayUserbot)\n"
pm_caption += " [Deploy FridayUserbot](https://telegra.ph/FRIDAY-06-15)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
    
