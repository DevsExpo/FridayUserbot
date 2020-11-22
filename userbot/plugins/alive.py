"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# IMG CREDITS: @Hackintush
import time

from uniborg.util import friday_on_cmd, sudo_cmd

from userbot import ALIVE_NAME, CMD_HELP, Lastupdate
from userbot.Configs import Config
from userbot.modules import currentversion

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = (
    "https://filetolinktelegrambot.herokuapp.com/1996057911608/VID_20200723_004420.mp4"
)
pm_caption = "`➥ CɪᴘʜᴇʀX Super Technology Bot is:` **Online**\n\n"
pm_caption += "**➥ System Status**\n"
pm_caption += "`➥ Telethon Version:` **6.0.9**\n`Python:` **3.8.5**\n"
pm_caption += "`➥ Database Status:` **AWS Working Properly**\n"
pm_caption += "**➥ Current Branch** : `Master`\n"
pm_caption += "**➥ CɪᴘʜᴇʀX OS** : `Kali GNU/Linux Rolling x86_64`\n"
pm_caption += f"**➥ My Boss** : [CɪᴘʜᴇʀX](https://t.me/Hackintush)\n"
pm_caption += "**✨ CɪᴘʜᴇʀX is the best ✨**"
# @command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()
