from fridaybot import ALIVE_NAME
from fridaybot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/43e6a780c8191c8e45982.mp4"
pm_caption = "**MARSHMELLOW ONLINE**!\n"

pm_caption += f"**M̴y̴ ̴B̴o̴s̴s̴** cum bhagwan : {DEFAULTUSER}\n"

pm_caption += "Dicsussion group    : [ᴊᴏɪɴ](https://t.me/pycodingwithayush)\n"

pm_caption += "PLUGIN CHANNEL        : [ᴊᴏɪɴ](https://t.me/pyfilesayush)\n"

pm_caption += " [───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n───█▒▒░░░░░░░░░▒▒█───\n────█░░█░░░░░█░░█────\n─▄▄──█░░░▀█▀░░░█──▄▄─\n█░░█─▀▄░░░░░░░▄▀─█░░█\n█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n](https://t.me/pycodingwithayush)"


# @command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"zinda"))
async def amireallyalive(alive):
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()
