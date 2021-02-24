# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from uniborg.util import friday_on_cmd

from fridaybot import CMD_HELP


@friday.on(friday_on_cmd(pattern="tagall(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    chat = await event.get_input_chat()
    mentions = ""
    sh = event.pattern_match.group(1) if event.pattern_match.group(1) else "Hi !"
    async for x in event.client.iter_participants(chat):
        mentions += f"[{x.first_name}](tg://user?id={x.id}) \n"
    await event.delete()
    n = 4096
    kk = [mentions[i:i+n] for i in range(0, len(mentions), n)]
    for i in kk:
        j = f"**{sh}** \n{i}"
        await event.client.send_message(event.chat_id, j)


CMD_HELP.update(
    {
        "tagall": "**Tagall**\
\n\n**Syntax : **`.tagall`\
\n**Usage :** tag everyone in a group"
    }
)
