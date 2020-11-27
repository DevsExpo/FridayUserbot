"""Enable Seen Counter in any message,Credits To Xtra-Tg Owner 
to know how many users have seen your message
Syntax: .fwd as reply to any message"""
from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd


@friday.on(friday_on_cmd(pattern="frwd"))
async def _(event):
    if event.fwd_from:
        return
    if Config.PRIVATE_GROUP_ID is None:
        await event.edit(
            "Please set the required environment variable `PRIVATE_GROUP_ID` for this plugin to work"
        )
        return
    try:
        e = await borg.get_entity(Config.PRIVATE_GROUP_ID)
    except Exception as e:
        await event.edit(str(e))
    else:
        re_message = await event.get_reply_message()
        # https://t.me/telethonofftopic/78166
        fwd_message = await borg.forward_messages(e, re_message, silent=True)
        await borg.forward_messages(event.chat_id, fwd_message)
        await fwd_message.delete()
        await event.delete()


CMD_HELP.update(
    {
        "fwd": "**Fwd**\
\n\n**Syntax : **`.frwd <reply to a message>`\
\n**Usage :** Enable Seen Counter in any message."
    }
)
