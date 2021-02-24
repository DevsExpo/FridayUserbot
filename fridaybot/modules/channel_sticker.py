#    Copyright (C) Midhun KM 2020-2021
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

from telethon import events
from telethon.utils import pack_bot_file_id

from fridaybot.modules.sql_helper.channel_sticker_sql import (
    add_new_data_in_db,
    is_data_indb,
    remove_datas,
)
from fridaybot.utils import admin_cmd

lulstark = [".", ",", "!", "'"]


@friday.on(admin_cmd(pattern="scs$"))
async def _m(event):
    if event.fwd_from:
        return
    await event.edit("`Processing..`")
    id_s = event.chat_id
    lmao = await event.get_reply_message()
    if event.is_group:
        await event.edit("`No, LoL You Can't Set Channel Stickers In Groups, lol`")
        return
    if event.is_private:
        await event.edit(
            "`No, LoL You Can't Set Channel Stickers In Private Chats, lol`"
        )
        return
    if not lmao.sticker:
        await event.edit("`Only Sticker Allowded.`")
        return
    if is_data_indb(id_s):
        await event.edit(
            "`This Channel Sticker Data Is Already In Db, Remove First To Update it.`"
        )
        return
    if not is_data_indb(id_s):
        bot_api_file_id = pack_bot_file_id(lmao.media)
        add_new_data_in_db(id_s, bot_api_file_id)
        await event.edit(
            "`This Sticker Has Been Set As Channel Sticker For This Channel`"
        )


@friday.on(admin_cmd(pattern="rcs$"))
async def _m(event):
    if event.fwd_from:
        return
    await event.edit("`Processing..`")
    id_s = event.chat_id
    if is_data_indb(id_s):
        remove_datas(id_s)
        await event.edit("`Done, I have Removed This Channel From DB`")
    elif not is_data_indb(id_s):
        await event.edit("`You Need To Set Channel Sticker To Remove It`")


@friday.on(admin_cmd(pattern="ccs$"))
async def _m(event):
    if event.fwd_from:
        return
    await event.edit("`Processing..`")
    id_s = event.chat_id
    if is_data_indb(id_s):
        await event.edit(
            f"**Yes, Channel Sticker Has Been Set. Sticker ID :** `{is_data_indb(id_s)}`"
        )
    elif not is_data_indb(id_s):
        await event.edit("`No Channel Sticker Set For This Channel.`")


@bot.on(events.NewMessage)
async def lul(event):
    if event.fwd_from:
        return
    lsb = event.chat_id
    id_s = event.chat_id
    if is_data_indb(event.chat_id):
        if event.text.startswith(tuple(lulstark)):
            return
        try:
            await borg.send_file(event.chat_id, is_data_indb(event.chat_id))
        except:
            await borg.send_message(
                Config.PRIVATE_GROUP_ID,
                f"Failed, To Send Sticker in {lsb}, Probably Due To No Access, Or Channel Not Found.",
            )
            return
    elif not is_data_indb(id_s):
        return
