# For @UniBorg
# Courtesy @Hackintush

"""
.bye
"""
import time

from telethon.tl.functions.channels import LeaveChannelRequest

from userbot.utils import friday_on_cmd, edit_or_reply, sudo_cmd


@friday.on(friday_on_cmd("bye", outgoing=True))
@friday.on(sudo_cmd("bye", allow_sudo=True))
async def leave(e):
    starkgang = await edit_or_reply(e, "Bye")
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await starkgang.edit("`I am leaving this chat.....!`")
        time.sleep(3)
        if "-" in str(e.chat_id):
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await starkgang.edit("`Sir This is Not A Chat`")
