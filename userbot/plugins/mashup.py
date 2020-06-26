# created by @Mr_Hops
"""
video meme mashup:
Syntax: .mashup <text>
"""
import asyncio
import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd
from userbot import CMD_HELP



from userbot import CMD_HELP
@borg.on(admin_cmd(pattern="mashup ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    input_str = event.pattern_match.group(1)
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    chat = "@vixtbot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=285336877))
              await event.client.send_message(chat, "{}".format(input_str))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Unblock @vixtbot")
              return
          if response.text.startswith("I can't find that"):
             await event.edit("sorry i can't find it")
          else: 
             await event.delete()
             await borg.send_file(event.chat_id, response.message, reply_to=reply_to_id)

@borg.on(admin_cmd(pattern="mash ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    input_str = event.pattern_match.group(1)
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    chat = "@vixtbot"
    await event.delete()
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=285336877))
              await event.client.send_message(chat, "{}".format(input_str))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Unblock @vixtbot")
              return
          if response.text.startswith("I can't find that"):
             await event.reply("sorry i can't find it")
          else: 
             await event.delete()
             await borg.send_file(event.chat_id, response.message, reply_to=reply_to_id)

CMD_HELP.update({"mashup": "`.mashup` <text> :\
      \n**USAGE:** Send you the related video message of given text . "
}) 
