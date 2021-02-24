#    Copyright (C) DevsExpo 2020-2021
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

from telethon import Button, custom, events, functions
from fridaybot.function import get_all_admin_chats, is_admin, is_nsfw
import requests
import string 
import random 
from fridaybot.modules.sql_helper.nsfw_watch_sql import add_nsfwatch, rmnsfwatch, get_all_nsfw_enabled_chat, is_nsfwatch_indb
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChatAdminRights,
    ChatBannedRights,
    MessageEntityMentionName,
    MessageMediaPhoto,
)
from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditBannedRequest,
    EditPhotoRequest,
)
MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)

@friday.on(friday_on_cmd(pattern="anw$"))
async def nsfw_watch(event):
    if not event.is_group:
        await event.edit("You Can Only Nsfw Watch in Groups.")
        return
    if not await is_admin(event, bot.uid): 
        await event.edit("`You Should Be Admin To Do This!`")
        return
    if is_nsfwatch_indb(str(event.chat_id)):
        await event.edit("`This Chat Has Already Enabled Nsfw Watch.`")
        return
    add_nsfwatch(str(event.chat_id))
    await event.edit(f"**Added Chat {event.chat.title} With Id {event.chat_id} To Database. This Groups Nsfw Contents Will Be Deleted And Logged in Logging Group**")

@friday.on(friday_on_cmd(pattern="rmnw$"))
async def disable_nsfw(event):
    if not event.is_group:
        await event.edit("You Can Only Disable Nsfw Mode in Groups.")
        return
    if not await is_admin(event, bot.uid): 
        await event.edit("`You Should Be Admin To Do This!`")
        return
    if not is_nsfwatch_indb(str(event.chat_id)):
        await event.edit("This Chat Has Not Enabled Nsfw Watch.")
        return
    rmnsfwatch(str(event.chat_id))
    await event.edit(f"**Removed Chat {event.chat.title} With Id {event.chat_id} From Nsfw Watch**")
    
@bot.on(events.NewMessage())        
async def ws(event):
    warner_starkz = get_all_nsfw_enabled_chat()
    if len(warner_starkz) == 0:
        return
    if not is_nsfwatch_indb(str(event.chat_id)):
        return
    if not event.media:
        return
    if not (event.gif or event.video or event.video_note or event.photo or event.sticker):
        return
    if not await is_admin(event, bot.uid):
        return
    hmmstark = await is_nsfw(event)
    his_id = event.sender_id
    if hmmstark is True:
        try:
            await event.delete()
            await event.client(EditBannedRequest(event.chat_id, his_id, MUTE_RIGHTS))
        except:
            pass
        lolchat = await event.get_chat()
        ctitle = event.chat.title
        if lolchat.username:
            hehe = lolchat.username
        else:
            hehe = event.chat_id
        wstark = await event.client.get_entity(his_id)
        if wstark.username:
            ujwal = wstark.username
        else:
            ujwal = wstark.id
        try:
            await borg.send_message(Config.PRIVATE_GROUP_ID, f"**#NSFW_WATCH** \n**Chat :** `{hehe}` \n**Nsfw Sender - User / Bot :** `{ujwal}` \n**Chat Title:** `{ctitle}`")  
            return
        except:
            return
