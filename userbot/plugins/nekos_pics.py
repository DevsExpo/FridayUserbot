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

@borg.on(admin_cmd("neko"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Neko Pic..```\n**It's Barely SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/neko")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("feet"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Feet Anime Pic..```\n**It's Barely SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/feet")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("yuri"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Yuri Pic..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/yuri")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("trap"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Trap Pic..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/trap")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("futanari"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Futanari Pic..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/futanari")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("hololewd"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Holo Lewd Pic..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/hololewd")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("lewdkemo"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Kemo Lewd  Pic..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/lewdkemo")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("erokemo"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Kemo Pic..```\n**It's Barely SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/erokemo")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("awallpaper"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Wallpaper..```\n**It's SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/wallpaper")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)

#By @WhySooSerious
@borg.on(admin_cmd("lewdk"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Kitsune Lewd  Pic..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/lewdk")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("lewdpic"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Lewd  Pic..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/lewd")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("eroyuri"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Ero-Yuri Pic..```\n**It's Barely SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/eroyuri")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("eron"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Ero-Neko  Pic..```\n**It's Barely SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/lewd")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("cumpic"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Cum  Pic..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/cum")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("bjpic"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Blow Job  Pic..```\n**WARNING : It's NSFW**")
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
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)

#By @WhySooSerious
@borg.on(admin_cmd("kemonomimi"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime KemonoMimi Pic..```\n**It's SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/kemonomimi")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("hentaipic"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai  Pic..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/hentai")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("erofeet"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Ero-Feet Pic..```\n**It's Barely SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/erofeet")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("holopic"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Holo Pic..```\n**It's SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/holo")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("titspic"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Tits Pic..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/tits")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("holoero"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Ero-Holo Pic..```\n**It's Barely SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/holoero")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("pussypic"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Pussy Pic..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/pussy")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("femdom"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai Femdom Pic..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/femdom")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await borg.send_file(event.chat_id, response.message.media)
#@WhySooSerious
@borg.on(admin_cmd("erok"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Ero-Kitsune Pic..```\n**It's Barely SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/erok")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("foxgirl"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Foxgirl Pic..```\n**It's Barely SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/foxgirl")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("eropic"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Ero Pic..```\n**It's Barely SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/ero")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("dva"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai D.V.A Source Pic..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/dva")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("nsolo"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Solo Neko  Pic..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/solo")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.edit("👇🏻**Done**👇🏻")
                await borg.send_file(event.chat_id, response.message.media)

#By @WhySooSerious
