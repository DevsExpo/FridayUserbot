# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""Filters
Available Commands:
.textblacklist
.listblacklist
.rmblacklist"""
import re

from telethon import events

import fridaybot.modules.sql_helper.blacklist_sql as sql
from fridaybot import CMD_HELP
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd


@friday.on(events.NewMessage(incoming=True))
async def on_new_message(event):
    # TODO: exempt admins from locks
    name = event.raw_text
    snips = sql.get_chat_blacklist(event.chat_id)
    for snip in snips:
        pattern = r"( |^|[^\w])" + re.escape(snip) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            try:
                await event.delete()
            except Exception:
                await event.reply("I do not have DELETE permission in this chat")
                sql.rm_from_blacklist(event.chat_id, snip.lower())
            break


@friday.on(friday_on_cmd("textblacklist ((.|\n)*)"))
@friday.on(sudo_cmd("textblacklist ((.|\n)*)", allow_sudo=True))
async def on_add_black_list(event):
    starksayxd = await edit_or_reply(event, "Trying To Set This Text As Blacklist xD")
    text = event.pattern_match.group(1)
    to_blacklist = list(
        set(trigger.strip() for trigger in text.split("\n") if trigger.strip())
    )
    for trigger in to_blacklist:
        sql.add_to_blacklist(event.chat_id, trigger.lower())
    await starksayxd.edit(
        "Added {} triggers to the blacklist in the current chat".format(
            len(to_blacklist)
        )
    )


@friday.on(friday_on_cmd("listblacklist"))
@friday.on(sudo_cmd("listblacklist", allow_sudo=True))
async def on_view_blacklist(event):
    sensibleleecher = await edit_or_reply(event, "Listing Blacklist xD")
    all_blacklisted = sql.get_chat_blacklist(event.chat_id)
    OUT_STR = "Blacklists in the Current Chat:\n"
    if len(all_blacklisted) > 0:
        for trigger in all_blacklisted:
            OUT_STR += f"👉 {trigger} \n"
    else:
        OUT_STR = "No BlackLists. Start Saving using `.textblacklist`"
    if len(OUT_STR) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "blacklist.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="BlackLists in the Current Chat",
                reply_to=event,
            )
            await event.delete()
    else:
        await sensibleleecher.edit(OUT_STR)


@friday.on(friday_on_cmd("rmblacklist ((.|\n)*)"))
@friday.on(sudo_cmd("rmblacklist ((.|\n)*)", allow_sudo=True))
async def on_delete_blacklist(event):
    sensibleisleecher = await edit_or_reply(event, "Ok Removing This Blacklist xD")
    text = event.pattern_match.group(1)
    to_unblacklist = list(
        set(trigger.strip() for trigger in text.split("\n") if trigger.strip())
    )
    successful = 0
    for trigger in to_unblacklist:
        if sql.rm_from_blacklist(event.chat_id, trigger.lower()):
            successful += 1
    await sensibleisleecher.edit(
        f"Removed {successful} / {len(to_unblacklist)} from the blacklist"
    )


CMD_HELP.update(
    {
        "blacklist": "**Blacklist**\
\n\n**Syntax : **`.textblacklist <text to blacklist>`\
\n**Usage :** Mentioned text is blacklisted in current chat.\
\n\n**Syntax : **`.listblacklist`\
\n**Usage :** Blacklisted text is shown.\
\n\n**Syntax : **`.rmblacklist <text to remove from blacklist>`\
\n**Usage :** Mentioned text is removed from blacklist."
    }
)
