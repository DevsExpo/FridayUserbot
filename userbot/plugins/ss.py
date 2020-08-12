# By @xditya Copy with credits
#Thanks to @HEisenbergTheDanger
from telethon import events, errors, functions, types
from uniborg.util import admin_cmd

@borg.on(admin_cmd("ss"))
async def _(event):
    if event.fwd_from:
        return
    NO_OF_SCSS = int(event.text.split(" ", maxsplit=1)[1]) 
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
        
    for I in range(NO_OF_SCSS):
      await event.client(functions.messages.SendScreenshotNotificationRequest(peer=event.chat_id, reply_to_msg_id=42))
    await event.delete() 
