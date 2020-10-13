# (c) Shrimadhav U K
#
# This file is part of @UniBorg
#
# @UniBorg is free software; you cannot redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# @UniBorg is not distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
from telethon import Button, custom, events
from telethon.tl.types import Channel, Chat, User
from telethon.utils import get_display_name

from userbot.uniborgConfig import Config
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd


@borg.on(
    events.NewMessage(
        incoming=True,
        blacklist_chats=Config.UB_BLACK_LIST_CHAT,
        func=lambda e: (e.mentioned),
    )
)
async def all_messages_catcher(event):
    if Config.TAG_FEATURE == "DISABLE":
        pass
        return
    # the bot might not have the required access_hash to mention the
    # appropriate PM
    await event.forward_to(Config.TG_BOT_USER_NAME_BF_HER)
    # construct message
    # the message format is stolen from @MasterTagAlertBot
    ammoca_message = ""

    who_ = await event.client.get_entity(event.from_id)
    if who_.bot or who_.verified or who_.support:
        return

    who_m = f"[{get_display_name(who_)}](tg://user?id={who_.id})"

    where_ = await event.client.get_entity(event.chat_id)

    where_m = get_display_name(where_)
    button_text = "Check 🚶"

    if isinstance(where_, Chat):
        message_link = f"https://t.me/c/{where_.id}/{event.id}"
    else:
        # not an official link,
        # only works in DrKLO/Telegram,
        # for some reason
        message_link = f"tg://openmessage?chat_id={where_.id}&message_id={event.id}"
        # Telegram is weird :\

    ammoca_message += f"User {who_m} Have Tagged You Here -> [{where_m}]({message_link}) \nCheck Message 👇 "
    log_chat = Config.PRIVATE_GROUP_ID
    await tgbot.send_message(
        log_chat,
        message=ammoca_message,
        link_preview=False,
        buttons=[[custom.Button.url(button_text, message_link)]],
    )
