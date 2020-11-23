# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2

from telethon.tl.types import ChannelParticipantsAdmins
from userbot import CMD_HELP
from userbot.utils import admin_cmd


# Added to TeleBot by @its_xditya
@borg.on(admin_cmd(pattern=r"administrator", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "Administrators in the chat : "
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


# Added to TeleBot by @its_xditya
@borg.on(admin_cmd(pattern=r"tag", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "All members tagged successfully. Honor CɪᴘʜᴇʀX!"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, 200):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()
    
CMD_HELP.update(
    {
        "tagall": "**Tagall**\
\n\n**Syntax : **`.tag`\
\n**Usage :** tag everyone in a group"
    }
)
