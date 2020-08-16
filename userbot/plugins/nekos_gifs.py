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

@borg.on(admin_cmd("sologif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Solo GIF..```\n**It's Barely SFW**")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
            await borg.send_message(chat, "/sologif")
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
@borg.on(admin_cmd("cumgif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Henti Cum GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
            await borg.send_message(chat, "/cumgif")
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
@borg.on(admin_cmd("ngif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Neko GIF..```\n**It's SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/ngif")
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
@borg.on(admin_cmd("tickle"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Tickle GIF..```\n**It's SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/tickle")
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
@borg.on(admin_cmd("feed"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Feeding GIF..```\n**It's SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/feed")
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
@borg.on(admin_cmd("bjgif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai Blow Job GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/bjgif")
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

@borg.on(admin_cmd("analgif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai Anal GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/bj")
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
@borg.on(admin_cmd("poke"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Poke GIF..```\n**Oh! It's SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/poke")
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
@borg.on(admin_cmd("pussygif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai Pussy GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/pussygif")
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

@borg.on(admin_cmd("hentaigif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/hentaigif")
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

@borg.on(admin_cmd("classic"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai Classic GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/classic")
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
@borg.on(admin_cmd("kuni"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai Pussy Lick GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/kuni")
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
@borg.on(admin_cmd("cuddle"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Cuddle GIF..```\n**WARNING : It's Really Kawaii**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/cuddle")
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
@borg.on(admin_cmd("titsgif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai Tits GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/titsgif")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#by @WhySooSerious
@borg.on(admin_cmd("smug"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Smug GIF..```\n**It's SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/smug")
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
@borg.on(admin_cmd("baka"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Baka GIF..```\n**It's SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/bj")
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

@borg.on(admin_cmd("lesbian"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an A Hentai Lesbian GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/lesbian")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious

@borg.on(admin_cmd("nsfwneko"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an A Hentai Neko GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/nekonsfw")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious

@borg.on(admin_cmd("kiss"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an an Anime Kissing GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/kiss")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
