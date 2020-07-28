"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @Hackintush
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://filetolinktelegrambot.herokuapp.com/1996057911608/VID_20200723_004420.mp4"
pm_caption = "`CɪᴘʜᴇʀX Super Technology Bot is:` **Online**\n\n"
pm_caption += "**System Status**\n"
pm_caption += "`Telethon Version:` **6.0.9**\n`Python:` **3.7.4**\n"
pm_caption += "`Database Status:` **AWS Working Properly**\n"
pm_caption += "**Current Branch** : `Master`\n"
pm_caption += "**CɪᴘʜᴇʀX OS** : `3.14`\n"
pm_caption += f"**My Boss** : [CɪᴘʜᴇʀX](https://t.me/Hackintush)\n"
pm_caption += "**✨ CɪᴘʜᴇʀX is the best ✨**" 
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
    
