

"""
.bye
"""
import time

from telethon.tl.functions.channels import LeaveChannelRequest

from userbot import CMD_HELP
from userbot.utils import friday_on_cmd, sudo_cmd


@friday.on(friday_on_cmd("bye"))
@friday.on(sudo_cmd("bye", allow_sudo=True))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        time.sleep(3)
        if e.is_group:
            await e.edit("`CɪᴘʜᴇʀX is leaving this chat...!`")
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit("`Boss, This is not a Chat`")


CMD_HELP.update(
    {
        "bye": "**Bye**\
\n\n**Syntax : **`.bye`\
\n**Usage :** use this plugin to leave a group."
    }
)
