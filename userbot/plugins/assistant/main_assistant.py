#    Copyright (C) Midhun KM 2020
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import asyncio
import io
import os
import re

import telethon
from telethon import Button, custom, events, functions
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import pack_bot_file_id

from userbot import bot
from userbot.Configs import Config
from userbot.plugins.sql_helper.blacklist_assistant import (
    add_nibba_in_db,
    is_he_added,
    removenibba,
)
from userbot.plugins.sql_helper.botusers_sql import add_me_in_db, his_userid
from userbot.plugins.sql_helper.idadder_sql import (
    add_usersid_in_db,
    already_added,
    get_all_users,
)


@assistant_cmd("start", is_args=False)
async def start(event):
    starkbot = await tgbot.get_me()
    bot_id = starkbot.first_name
    bot_username = starkbot.username
    replied_user = await event.client(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    devlop = await bot.get_me()
    devlop.first_name
    vent = event.chat_id
    mypic = Config.ASSISTANT_START_PIC
    starttext = f"Hello, {firstname} ! Nice To Meet You, Well I'm {bot_id}, A Powerfull Assistant Bot.\n\nYou Can Talk/Contact with My Master Using This Bot.\n\nProgrammed and Powered By My Master the ➤ CɪᴘʜᴇʀX\n\n Please Join and Support Our Channel ➤ [Future Technology](https://t.me/FutureTechnologyGuard)"
    if event.sender_id == bot.uid:
        await tgbot.send_message(
            vent,
            message=f"Hi Master, It's Me {bot_id}, Your Assistant ! \nWhat You Wanna Do?",
            buttons=[
                [custom.Button.inline("Show Users 🔥", data="users")],
                [custom.Button.inline("Commands For Assistant", data="gibcmd")],
                [
                    Button.url(
                        "Add Me to Group 👥", f"t.me/{bot_username}?startgroup=true"
                    )
                ],
                [custom.Button.inline("⨵ Close Menu ⨵", data="seclose")],
            ],
        )
    else:
        if already_added(event.sender_id):
            pass
        elif not already_added(event.sender_id):
            add_usersid_in_db(event.sender_id)
        await tgbot.send_file(
            event.chat_id,
            file=mypic,
            caption=starttext,
            link_preview=False,
            buttons=[
                [custom.Button.inline("Commands For Assistant", data="usercmd")],
                [
                    Button.url(
                        "Add Me to Group 👥", f"t.me/{bot_username}?startgroup=true"
                    )
                ],
                [custom.Button.inline("⨵ Close Menu ⨵", data="seclose")],
            ],
        )
        if os.path.exists(mypic):
            os.remove(mypic)


# Data's


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"users")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        total_users = get_all_users()
        users_list = "List Of Total Users In Bot. \n\n"
        for starked in total_users:
            users_list += ("==> {} \n").format(int(starked.chat_id))
        with io.BytesIO(str.encode(users_list)) as tedt_file:
            tedt_file.name = "userlist.txt"
            await tgbot.send_file(
                event.chat_id,
                tedt_file,
                force_document=True,
                caption="Total Users In CɪᴘʜᴇʀX Bot.",
                allow_cache=False,
            )
    else:
        pass


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"seclose")))
async def users(event):
    await event.edit(
        "⨵ CɪᴘʜᴇʀX Bot Assitant Menu Closed ⨵",
        buttons=[custom.Button.inline("Re-open Menu", data="Creopen")],
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Creopen")))
async def megix(event):
    await event.delete()
    starkbot = await tgbot.get_me()
    starkbot.first_name
    bot_username = starkbot.username
    await event.client(GetFullUserRequest(event.sender_id))
    vent = event.chat_id
    mypic = Config.ASSISTANT_START_PIC
    starttext = f"≼≼≼CɪᴘʜᴇʀX Assistant Bot Menu Re-opened≽≽≽\n(c)CɪᴘʜᴇʀX Exclusive"
    if event.sender_id == bot.uid:
        await tgbot.send_message(
            vent,
            message=f"≼≼≼Menu Re-opened Master≽≽≽",
            buttons=[
                [custom.Button.inline("Show Users 🔥", data="users")],
                [custom.Button.inline("Commands For Assistant", data="gibcmd")],
                [
                    Button.url(
                        "Add Me to Group 👥", f"t.me/{bot_username}?startgroup=true"
                    )
                ],
                [custom.Button.inline("⨵ Close Menu ⨵", data="seclose")],
            ],
        )
    else:
        if already_added(event.sender_id):
            pass
        elif not already_added(event.sender_id):
            add_usersid_in_db(event.sender_id)
        await tgbot.send_file(
            event.chat_id,
            file=mypic,
            caption=starttext,
            link_preview=False,
            buttons=[
                [custom.Button.inline("Commands For Assistant", data="usercmd")],
                [
                    Button.url(
                        "Add Me to Group 👥", f"t.me/{bot_username}?startgroup=true"
                    )
                ],
                [custom.Button.inline("⨵ Close Menu ⨵", data="seclose")],
            ],
        )
        if os.path.exists(mypic):
            os.remove(mypic)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gibcmd")))
async def users(event):
    await event.delete()
    grabon = "Here Are Some Commands \n➤ /start - Check if I'm Alive \n➤ /ping - Pong! \n➤ /tr <lang-code> \n➤ /broadcast - Sends Message To all Users In Bot \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Am I Alive? \n➤ /bun - Works In Group , Bans A User. \n➤ /unbun - Unbans A User in Group \n➤ /prumote - Promotes A User \n➤ /demute - Demotes A User \n➤ /pin - Pins A Message \n➤ /stats - Shows Total Users In Bot"
    await tgbot.send_message(event.chat_id, grabon)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"usercmd")))
async def users(event):
    await event.delete()
    userbon = "Here are Some Commands Which You Can Use in Groups \n➤ /start - Check if I'm Alive \n➤ /ping - Pong! \n➤ /tr <lang-code> \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Am I Alive? \n➤ /bun - Works In Group , Bans A User. \n➤ /unbun - Unbans A User in Group \n➤ /prumote - Promotes A User \n➤ /demute - Demotes A User \n➤ /pin - Pins A Message"
    await tgbot.send_message(event.chat_id, userbon)


# Bot Permit.
@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def all_messages_catcher(event):
    if is_he_added(event.sender_id):
        return
    if event.sender_id == bot.uid:
        return
    if event.raw_text.startswith("/"):
        return
    if Config.SUB_TO_MSG_ASSISTANT:
        try:
            result = await tgbot(
                functions.channels.GetParticipantRequest(
                    channel=Config.JTM_CHANNEL_ID, user_id=event.sender_id
                )
            )
        except telethon.errors.rpcerrorlist.UserNotParticipantError:
            await event.reply(
                f"**Please Join My Channel First And Then Try Again!**",
                buttons=[
                    Button.url("≼≼≼ Join Channel ≽≽≽", Config.JTM_CHANNEL_USERNAME)
                ],
            )
            return
    await event.get_sender()
    sed = await event.forward_to(bot.uid)
    add_me_in_db(sed.id, event.sender_id, event.id)


@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def sed(event):
    msg = await event.get_reply_message()
    if msg is None:
        return
    msg.id
    msg_s = event.raw_text
    user_id, reply_message_id = his_userid(msg.id)
    if event.sender_id != bot.uid:
        return
    elif event.raw_text.startswith("/"):
        return
    elif event.text is not None and event.media:
        bot_api_file_id = pack_bot_file_id(event.media)
        await tgbot.send_file(
            user_id,
            file=bot_api_file_id,
            caption=event.text,
            reply_to=reply_message_id,
        )
    else:
        msg_s = event.raw_text
        await tgbot.send_message(
            user_id,
            msg_s,
            reply_to=reply_message_id,
        )


@assistant_cmd("broadcast", is_args=True)
@god_only
async def sedlyfsir(event):
    msgtobroadcast = event.pattern_match.group(1)
    userstobc = get_all_users()
    error_count = 0
    sent_count = 0
    if msgtobroadcast == None:
        await event.reply("`Wait. What? Broadcast None?`")
        return
    elif msgtobroadcast == " ":
        await event.reply("`Wait. What? Broadcast None?`")
        return
    for starkcast in userstobc:
        try:
            sent_count += 1
            await tgbot.send_message(int(starkcast.chat_id), msgtobroadcast)
            await asyncio.sleep(0.2)
        except:
            error_count += 1
    await tgbot.send_message(
        event.chat_id,
        f"Broadcast Done in {sent_count} Group/Users and I got {error_count} Error and Total Number Was {len(userstobc)}",
    )


@assistant_cmd("stats", is_args=False)
@peru_only
async def starkisnoob(event):
    starkisnoob = get_all_users()
    await event.reply(
        f"**Stats Of Your Bot** \nTotal Users In Bot => {len(starkisnoob)}"
    )


@assistant_cmd("help", is_args=False)
@peru_only
async def starkislub(event):
    grabonx = "Here are Some Commands \n➤ /start - Check if I am Alive \n➤ /ping - Pong! \n➤ /tr <lang-code> \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Am I Alive? \n➤ /bun - Works In Group , Bans A User. \n➤ /unbun - Unbans A User in Group \n➤ /prumote - Promotes A User \n➤ /demute - Demotes A User \n➤ /pin - Pins A Message"
    await event.reply(grabonx)


@assistant_cmd("block", is_args=False)
@god_only
async def starkisnoob(event):
    if event.sender_id == bot.uid:
        msg = await event.get_reply_message()
        user_id, reply_message_id = his_userid(msg.id)
    if is_he_added(user_id):
        await event.reply("Already Blacklisted")
    elif not is_he_added(user_id):
        add_nibba_in_db(user_id)
        await event.reply("Blacklisted This Dumb Person")
        await tgbot.send_message(
            user_id, "You Have Been Blacklisted And You Can't Message My Master Now."
        )


@assistant_cmd("unblock", is_args=False)
@god_only
async def starkisnoob(event):
    if event.sender_id == bot.uid:
        msg = await event.get_reply_message()
        msg.id
        event.raw_text
        user_id, reply_message_id = his_userid(msg.id)
    if not is_he_added(user_id):
        await event.reply("Not Even Blacklisted 🚶")
    elif is_he_added(user_id):
        removenibba(user_id)
        await event.reply("Unblacklisted This Dumb Person")
        await tgbot.send_message(
            user_id, "Congragulation! You Have Been Unblacklisted By My Master."
        )
