# Originally Made by @Hackintush
""" Userbot module containing userid, chatid and log commands"""

from time import sleep

from telethon.tl.functions.channels import LeaveChannelRequest

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot.events import register

@register(outgoing=True, pattern="^.userid$")
async def useridgetter(target):
    """ For .userid command, returns the ID of the target user. """
    message = await target.get_reply_message()
    if message:
        if not message.forward:
            user_id = message.sender.id
            if message.sender.username:
                name = "@" + message.sender.username
            else:
                name = "**" + message.sender.first_name + "**"

        else:
            user_id = message.forward.sender.id
            if message.forward.sender.username:
                name = "@" + message.forward.sender.username
            else:
                name = "*" + message.forward.sender.first_name + "*"
        await target.edit("**Name:** {} \n**User ID:** `{}`".format(
            name, user_id))


@register(outgoing=True, pattern="^.chatid$")
async def chatidgetter(chat):
    """ For .chatid, returns the ID of the chat you are in at that moment. """
    await chat.edit("**Chat ID:**\n`" + str(chat.chat_id) + "`")
    
CMD_HELP.update(
    {
        "user": "**User**\
        \n\n**Syntax : **`.userid`\
        \n**Usage :** Checks the userid of a message.\ 
        \n\n**Syntax : **`.chatid`\
        \n**Usage :** Checks the chatid of a chat." 
    }
)
