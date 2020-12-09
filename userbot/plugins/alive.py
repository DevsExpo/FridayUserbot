"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# IMG CREDITS: @Hackintush
import time
from uniborg.util import friday_on_cmd, sudo_cmd
from userbot import ALIVE_NAME, CMD_HELP، Lastupdate 
from usetbot.Configs import Config
from userbot.modules import currentversion

# Functions
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = (
    "https://filetolinktelegrambot.herokuapp.com/1996057911608/VID_20200723_004420.mp4"
)
pm_caption = "➥ `CɪᴘʜᴇʀX Super Technology Bot is:` **Online**\n\n"
pm_caption += "➥ **System Status**\n"
pm_caption += "➥ **Telethon Version:** `6.0.9` \n" 
pm_caption += "➥ **Python:** `3.9` \n"
pm_caption += f"➥ **CɪᴘʜᴇʀX Server Uptime** : `{uptime}` \n"
pm_caption += "➥ **Database Status:** `AWS Working Properly` \n"
pm_caption += "➥ **Current Branch** : `Master` \n"
pm_caption += "➥ **CɪᴘʜᴇʀX OS** : `Kali GNU/Linux Rolling x64_86` \n"
pm_caption += f"➥ **My Boss** : [CɪᴘʜᴇʀX](https://t.me/Hackintush) \n"
pm_caption += "**✨ CɪᴘʜᴇʀX is the best ✨**"


@friday.on(friday_on_cmd(pattern=r"alive"))
@friday.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CMD_HELP.update(
    {
        "alive": "**ALive**\
\n\n**Syntax : **`.alive`\
\n**Usage :** Check if CɪᴘʜᴇʀX Bot is alive"
    }
)
