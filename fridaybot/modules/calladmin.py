""".admin Plugin for @UniBorg"""
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import friday_on_cmd

from fridaybot import CMD_HELP


@friday.on(friday_on_cmd(pattern="admins"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "@admin: **Spam Spotted**"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f"[\u2063](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


CMD_HELP.update(
    {
        "calladmin": "**Calladmin**\
\n\n**Syntax : **`.admins`\
\n**Usage :** use this plugin to mention all the admins in a group."
    }
)
