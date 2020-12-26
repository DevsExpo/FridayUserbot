from telethon import events

from fridaybot.modules.sql_helper.PostAppender_sql import (
    add_new_datas_in_db,
    is_data_indbs,
    is_footer,
    remove_dataz,
)
from fridaybot.utils import admin_cmd

lulstark = [".", ",", "!", "'"]


@friday.on(admin_cmd(pattern="spf (.*)"))
async def mstark(event):
    await event.edit("`Processing..`")
    lul_id = event.chat_id
    append_text = event.pattern_match.group(1)
    is_foot = True
    if event.is_group:
        await event.edit("`No, LoL You Can't Set Channel Post Appender In Groups, lol`")
        return
    if event.is_private:
        await event.edit(
            "`No, LoL You Can't Set Channel Post Appender In Private Chats, lol`"
        )
        return
    if is_data_indbs(lul_id):
        await event.edit("`Please Remove Old Data, To Add New One`")
    elif not is_data_indbs(lul_id):
        add_new_datas_in_db(lul_id, append_text, is_foot)
        await event.edit(
            f"Sucessfully, Saved This Text. Every New Message's Footer Will Be Edited To `{append_text}`"
        )


@friday.on(admin_cmd(pattern="sph (.*)"))
async def _starky(event):
    await event.edit("`Processing..`")
    lul_id = event.chat_id
    append_text = event.pattern_match.group(1)
    is_foot = False
    if event.is_group:
        await event.edit("`No, LoL You Can't Set Channel Append System In Groups, lol`")
        return
    if event.is_private:
        await event.edit(
            "`No, LoL You Can't Set Channel Append System In Private Chats, lol`"
        )
        return
    if is_data_indbs(lul_id):
        await event.edit("`Please Remove Old Data, To Add New One`")
    elif not is_data_indbs(lul_id):
        add_new_datas_in_db(lul_id, append_text, is_foot)
        await event.edit(
            f"Sucessfully, Saved This Text. Every New Message's Header Will Be Edited To `{append_text}`"
        )


@friday.on(admin_cmd(pattern="rpd$"))
async def _m(event):
    await event.edit("`Processing..`")
    id_s = event.chat_id
    if is_data_indbs(id_s):
        remove_dataz(id_s)
        await event.edit("`Done, I have Removed This Channel From DB`")
    elif not is_data_indbs(id_s):
        await event.edit("`You Need To Set Channel Append System To Remove It`")


@bot.on(events.NewMessage)
async def luli(event):
    event.chat_id
    event.chat_id
    lol_text = event.text
    if is_data_indbs(event.chat_id):
        if event.text.startswith(tuple(lulstark)):
            return
        if is_footer(event.chat_id):
            await event.edit(f"{lol_text} \n{is_data_indbs(event.chat_id)}")
        elif not is_footer(event.chat_id):
            await event.edit(f"{is_data_indbs(event.chat_id)} \n{lol_text}")
    elif not is_data_indbs(event.chat_id):
        return


@friday.on(admin_cmd(pattern="spad$"))
async def _m(event):
    await event.edit("`Processing..`")
    id_s = event.chat_id
    if is_data_indbs(id_s):
        await event.edit(
            f"`Channel ID : {id_s} \nIs Foot: {is_footer(event.chat_id)} \nText: {is_data_indbs(event.chat_id)}`"
        )
    elif not is_data_indbs(id_s):
        await event.edit("`You Need To Set Channel Append System To Check It`")
