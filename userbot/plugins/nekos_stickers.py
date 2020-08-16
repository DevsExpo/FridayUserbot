# Made for TeleBot
# Re-written by @its_xditya 
# Kangers kwwp the credits

#Made by @WhySooSerious
#From Nekos API

import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd



@borg.on(admin_cmd("alewd"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai Avatar Lewd Sticker..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
            await borg.send_message(chat, "/avatarlewd")
            response = await response
        except YouBlockedUserError:
              await event.reply("```Please unblock @KeikoSDbot and try again```")
              return
        if response.text.startswith("Forward"):
             await event.edit("```can you kindly disable your forward privacy settings for good?```")
        else:
            await event.delete()
            await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("gasm"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Random Orgasm Sticker..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
            await borg.send_message(chat, "/gasm")
            response = await response
        except YouBlockedUserError:
              await event.reply("```Please unblock @KeikoSDbot and try again```")
              return
        if response.text.startswith("Forward"):
             await event.edit("```can you kindly disable your forward privacy settings for good?```")
        else:
            await event.delete()
            await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("avatar"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai Avatar Sticker..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
            await borg.send_message(chat, "/avatar")
            response = await response
        except YouBlockedUserError:
              await event.reply("```Please unblock @KeikoSDbot and try again```")
              return
        if response.text.startswith("Forward"):
             await event.edit("```can you kindly disable your forward privacy settings for good?```")
        else:
            await event.delete()
            await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("waifu"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Waifu Sticker..```\n**Yay, It's SFW**")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
            await borg.send_message(chat, "/waifu")
            response = await response
        except YouBlockedUserError:
              await event.reply("```Please unblock @KeikoSDbot and try again```")
              return
        if response.text.startswith("Forward"):
             await event.edit("```can you kindly disable your forward privacy settings for good?```")
        else:
            await event.delete()
            await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
