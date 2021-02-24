#   Copyright 2019 - 2020-2021 DarkPrinc3

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import asyncio, coffeehouse

from coffeehouse.lydia import LydiaAI
from telethon import events
from fridaybot.utils import admin_cmd
from fridaybot import CMD_HELP
from fridaybot.Configs import Config

# Non-SQL Mode
ACC_LYDIA = {}
SESSION_ID = {}

if Config.LYDIA_API_KEY:
    api_key = Config.LYDIA_API_KEY
    lydia = LydiaAI(api_key)


@borg.on(admin_cmd(pattern='rcf$'))
async def repcf(event):
    if event.fwd_from:
        return
    await event.edit("Processing...")
    try:
        session = lydia.create_session()
        session_id = session.id
        reply = await event.get_reply_message()
        msg = reply.text
        text_rep = session.think_thought((session_id, msg))
        await event.edit("💫 {0}".format(text_rep))
    except Exception as e:
        await event.edit(str(e))


@borg.on(admin_cmd(pattern='addcf$'))
async def addcf(event):
    if event.fwd_from:
        return
    await event.edit("Running on Non-SQL mode for now...")
    await asyncio.sleep(3)
    await event.edit("Processing...")
    reply_msg = await event.get_reply_message()
    if reply_msg:
        session = lydia.create_session()
        session_id = session.id
        if reply_msg.sender_id is None:
            return await event.edit("Invalid user type.")
        ACC_LYDIA.update({str(event.chat_id) + " " + str(reply_msg.sender_id): session})
        SESSION_ID.update(
            {str(event.chat_id) + " " + str(reply_msg.sender_id): session_id}
        )
        await event.edit(
            "Lydia successfully (re)enabled for user: {} in chat: {}".format(
                str(reply_msg.sender_id), str(event.chat_id)
            )
        )
    else:
        await event.edit("Reply to a user to activate Lydia AI on them")


@borg.on(admin_cmd(pattern='remcf$'))
async def remcf(event):
    if event.fwd_from:
        return
    await event.edit("Running on Non-SQL mode for now...")
    await asyncio.sleep(3)
    await event.edit("Processing...")
    reply_msg = await event.get_reply_message()
    try:
        del ACC_LYDIA[str(event.chat_id) + " " + str(reply_msg.sender_id)]
        del SESSION_ID[str(event.chat_id) + " " + str(reply_msg.sender_id)]
        await event.edit(
            "Lydia successfully disabled for user: {} in chat: {}".format(
                str(reply_msg.sender_id), str(event.chat_id)
            )
        )
    except Exception:
        await event.edit("This person does not have Lydia activated on him/her.")


@bot.on(events.NewMessage(incoming=True))
async def user(event):
    event.text
    try:
        session = ACC_LYDIA[str(event.chat_id) + " " + str(event.sender_id)]
        session_id = SESSION_ID[str(event.chat_id) + " " + str(event.sender_id)]
        msg = event.text
        async with event.client.action(event.chat_id, "typing"):
            text_rep = session.think_thought((session_id, msg))
            wait_time = 0
            for i in range(len(text_rep)):
                wait_time = wait_time + 0.1
            await asyncio.sleep(wait_time)
            await event.reply(text_rep)
    except (KeyError, TypeError):
        return


CMD_HELP.update(
    {
        "lydia": "**Lydia**\
\n\n**Syntax : **`.addcf <reply to user>`\
\n**Usage :** Enables Lydia ai on the user.\
\n\n**Syntax : **`.remcf <reply to user>`\
\n**Usage :** Disables AI Lydia on the user.\
\n\n**Syntax : **`.repcf <reply to user>`\
\n**Usage :** Auto reply on the user."
    }
)
