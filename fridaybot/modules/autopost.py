#    Copyright (C) @DevsExpo 2020-2021
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

from fridaybot.modules.sql_helper.auto_post_sql import add_new_post_data_in_db, get_all_post_data, is_post_data_in_db, remove_post_data
from telethon import events

@bot.on(admin_cmd(pattern="autopost ?(.*)"))
async def lol(event):
    if (event.is_private or event.is_group):
        await event.edit("`Only Channels Can Use THis Feature.`")
        return
    sed = event.pattern_match.group(1)
    if str(sed).startswith("-100"):
        kk = str(sed).replace("-100", "")
    else:
        kk = sed
    if not kk.isdigit():
        await event.edit("`Channel ID Should be Integers`")
        return
    if is_post_data_in_db(kk , event.chat_id):
        await event.edit("Ah, This Channel Is Already DB")
        return
    add_new_post_data_in_db(kk, event.chat_id)
    await event.edit(f"`Added AutoPosting To This Chat From {sed}`")

@bot.on(admin_cmd(pattern="rmautopost ?(.*)"))
async def lol(event):
    if (event.is_private or event.is_group):
        await event.edit("`Only Channels Can Use THis Feature.`")
        return
    sed = event.pattern_match.group(1)
    if str(sed).startswith("-100"):
        kk = str(sed).replace("-100", "")
    else:
        kk = sed
    if not kk.isdigit():
        await event.edit("`Channel ID Should be Integers`")
        return
    if not is_post_data_in_db(kk, event.chat_id):
        await event.edit("Ah, This Channel Is Not In DB")
        return
    remove_post_data(kk, event.chat_id)
    await event.edit(f"`Oh, Okay I will Stop Posting From {sed}.`")

@bot.on(events.NewMessage())
async def what(event):
    if event.is_private:
        return
    chat_id = str(event.chat_id).replace("-100", "")
    channels_set  = get_all_post_data(chat_id)
    if channels_set == []:
        return
    for chat in channels_set:
        if event.media:
            await event.client.send_file(int(chat), event.media, caption=event.text)
        elif not event.media:
            await event.client.send_message(int(chat), event.message)
