#   Copyright 2019 - 2020 DarkPrinc3

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import asyncio

import coffeehouse
from coffeehouse.lydia import LydiaAI
from telethon import events

from userbot import CMD_HELP

# Non-SQL Mode
ACC_LYDIA = {}
SESSION_ID = {}

if Var.LYDIA_API_KEY:
    api_key = Var.LYDIA_API_KEY
    api_client = coffeehouse.API(api_key)
    Lydia = LydiaAI(api_client)


@command(pattern="^.repcf", outgoing=True)
async def repcf(event):
    if event.fwd_from:
        return
    await event.edit("Processing...")
    try:
        session = Lydia.create_session()
        session_id = session.id
        reply = await event.get_reply_message()
        msg = reply.text
        text_rep = session.think_thought((session_id, msg))
        await event.edit(" {0}".format(text_rep))
    except Exception as e:
        await event.edit(str(e))


@command(pattern="^.addcf", outgoing=True)
async def addcf(event):
    if event.fwd_from:
        return
    await event.edit("Running on Non-SQL mode for now...")
    await asyncio.sleep(3)
    await event.edit("Processing...")
    reply_msg = await event.get_reply_message()
    if reply_msg:
        session = Lydia.create_session()
        session_id = session.id
        ACC_LYDIA.update({str(event.chat_id) + " " + str(reply_msg.from_id): session})
        SESSION_ID.update(
            {str(event.chat_id) + " " + str(reply_msg.from_id): session_id}
        )
        await event.edit(
            "Lydia successfully enabled for user: {} in chat: {}".format(
                str(reply_msg.from_id), str(event.chat_id)
            )
        )
    else:
        await event.edit("Reply to a user to activate Lydia AI on them")


@command(pattern="^.remcf", outgoing=True)
async def remcf(event):
    if event.fwd_from:
        return
    await event.edit("Running on Non-SQL mode for now...")
    await asyncio.sleep(3)
    await event.edit("Processing...")
    reply_msg = await event.get_reply_message()
    try:
        del ACC_LYDIA[str(event.chat_id) + " " + str(reply_msg.from_id)]
        del SESSION_ID[str(event.chat_id) + " " + str(reply_msg.from_id)]
        await event.edit(
            "Lydia successfully disabled for user: {} in chat: {}".format(
                str(reply_msg.from_id), str(event.chat_id)
            )
        )
    except KeyError:
        await event.edit("This person does not have Lydia activated on him/her.")


@bot.on(events.NewMessage(incoming=True))
async def user(event):
    event.text
    try:
        session = ACC_LYDIA[str(event.chat_id) + " " + str(event.from_id)]
        session_id = SESSION_ID[str(event.chat_id) + " " + str(event.from_id)]
        msg = event.text
        async with event.client.action(event.chat_id, "typing"):
            text_rep = session.think_thought((session_id, msg))
            wait_time = 0
            for i in range(len(text_rep)):
                wait_time = wait_time + 0.1
            await asyncio.sleep(wait_time)
            await event.reply(text_rep)
    except KeyError:
        return


CMD_HELP.update(
    {
        "lydia": "**Lydia**\
\n\n**Syntax : **`.addcf <reply to user>`\
\n**Usage :** Enables Lydia AI on the user.\
\n\n**Syntax : **`.remcf <reply to user>`\
\n**Usage :** Disables Lydia AI on the user."
    }
)
