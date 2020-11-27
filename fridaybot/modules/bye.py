# For @UniBorg
# Courtesy @yasirsiddiqui

"""
.bye
"""
import time

from telethon.tl.functions.channels import LeaveChannelRequest

from fridaybot import CMD_HELP
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd


@friday.on(friday_on_cmd("bye", outgoing=True))
@friday.on(sudo_cmd("bye", allow_sudo=True))
async def leave(e):
    starkgang = await edit_or_reply(e, "Bye Kek")
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await starkgang.edit("`I am leaving this chat.....!`")
        time.sleep(3)
        if "-" in str(e.chat_id):
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await starkgang.edit("`Sir This is Not A Chat`")


CMD_HELP.update(
    {
        "bye": "**Bye**\
\n\n**Syntax : **`.bye`\
\n**Usage :** use this plugin to leave a group."
    }
)
