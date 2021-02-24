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


from apscheduler.schedulers.asyncio import AsyncIOScheduler 
from telethon import functions
from fridaybot.function import get_all_admin_chats, is_admin
from fridaybot.modules.sql_helper.night_mode_sql import add_nightmode, rmnightmode, get_all_chat_id, is_nightmode_indb
from telethon.tl.types import ChatBannedRights

hehes = ChatBannedRights(
    until_date=None,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    send_polls=True,
    invite_users=True,
    pin_messages=True,
    change_info=True,
)
openhehe = ChatBannedRights(
    until_date=None,
    send_messages=False,
    send_media=False,
    send_stickers=False,
    send_gifs=False,
    send_games=False,
    send_inline=False,
    send_polls=False,
    invite_users=True,
    pin_messages=True,
    change_info=True,
)
@friday.on(friday_on_cmd(pattern="scgrp$"))
async def close_ws(event):
    if not event.is_group:
        await event.edit("You Can Only Enable Night Mode in Groups.")
        return
    if not await is_admin(event, bot.uid): 
        await event.edit("`You Should Be Admin To Do This!`")
        return
    if is_nightmode_indb(str(event.chat_id)):
        await event.edit("This Chat is Has Already Enabled Night Mode.")
        return
    add_nightmode(str(event.chat_id))
    await event.edit(f"**Added Chat {event.chat.title} With Id {event.chat_id} To Database. This Group Will Be Closed On 12Am(IST) And Will Opened On 06Am(IST)**")

@friday.on(friday_on_cmd(pattern="rsgrp$"))
async def disable_ws(event):
    if not event.is_group:
        await event.edit("You Can Only Disable Night Mode in Groups.")
        return
    if not await is_admin(event, bot.uid): 
        await event.edit("`You Should Be Admin To Do This!`")
        return
    if not is_nightmode_indb(str(event.chat_id)):
        await event.edit("This Chat is Has Not Enabled Night Mode.")
        return
    rmnightmode(str(event.chat_id))
    await event.edit(f"**Removed Chat {event.chat.title} With Id {event.chat_id} From Database. This Group Will Be No Longer Closed On 12Am(IST) And Will Opened On 06Am(IST)**")


async def job_close():
    ws_chats = get_all_chat_id()
    if len(ws_chats) == 0:
        return
    for warner in ws_chats:
        try:
            await friday.send_message(
              int(warner.chat_id), "`12:00 Am, Group Is Closing Till 6 Am. Night Mode Started !` \n**Powered By @FRidayOT**"
            )
            await friday(
            functions.messages.EditChatDefaultBannedRightsRequest(
                peer=int(warner.chat_id), banned_rights=hehes
            )
            )
            if Config.CLEAN_GROUPS:
                async for user in friday.iter_participants(int(warner.chat_id)):
                    if user.deleted:
                        await friday.edit_permissions(int(warner.chat_id), user.id, view_messages=False)
        except Exception as e:
            logger.info(f"Unable To Close Group {warner} - {e}")

scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(job_close, trigger="cron", hour=23, minute=55)
scheduler.start()


async def job_open():
    ws_chats = get_all_chat_id()
    if len(ws_chats) == 0:
        return
    for warner in ws_chats:
        try:
            await friday.send_message(
              int(warner.chat_id), "`06:00 Am, Group Is Opening.`\n**Powered By @FRidayOT**"
            )
            await friday(
            functions.messages.EditChatDefaultBannedRightsRequest(
                peer=int(warner.chat_id), banned_rights=openhehe
            )
        )
        except Exception as e:
            logger.info(f"Unable To Open Group {warner.chat_id} - {e}")

# Run everyday at 06
scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(job_open, trigger="cron", hour=6, minute=10)
scheduler.start()
