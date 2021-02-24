# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""WikiPedia.ORG
Syntax: .wikipedia Query"""
import wikipedia
from uniborg.util import friday_on_cmd

from fridaybot import CMD_HELP


@friday.on(friday_on_cmd(pattern="wikipedia (.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Processing ...")
    input_str = event.pattern_match.group(1)
    result = ""
    results = wikipedia.search(input_str)
    for s in results:
        try:
           page = wikipedia.page(s)
           url = page.url
           result += f"> [{s}]({url}) \n"
        except:
           pass
    await event.edit(
        "WikiPedia **Search**: {} \n\n **Result**: \n\n{}".format(input_str, result)
    )


CMD_HELP.update(
    {
        "wikipedia": "**Wikipedia**\
\n\n**Syntax : **`.wikipedia <query>`\
\n**Usage :** get Wikipedia link instantly just with a query"
    }
)
