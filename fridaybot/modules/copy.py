
from fridaybot import CMD_HELP

from ..utils import admin_cmd


@borg.on(admin_cmd(pattern="copy"))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.text
        event.reply_to_msg_id
        the_real_message = the_real_message.replace("*", "*")
        the_real_message = the_real_message.replace("_", "_")
        await event.edit(the_real_message)
    else:
        await event.edit("Reply to a  message .copy to copy nd paste ")


CMD_HELP.update({"copy": ".c <reply to any text> " "\nc that text nd redeliver it"})
