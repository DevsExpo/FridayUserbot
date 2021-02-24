"""
StartPage Search Plugin for Userbot . //Alternative to Google Search
cmd : .sch search_query 
By: @Zero_cool7870

"""

import json
import os

from uniborg.util import friday_on_cmd


@friday.on(friday_on_cmd(pattern="sch ?(.*)", allow_sudo=True))
async def sp_search(event):
    search_str = event.pattern_match.group(1)
    if event.fwd_from:
        return
    await event.edit("**Searching for " + search_str + " ...**")

    command = "sp --json " + search_str + " > out.json"

    await friday.run_cmd(command)

    f = open("out.json", "r").read()

    data = json.loads(str(f))

    msg = "**Search Query** \n`" + search_str + "`\n**Results**\n"

    for element in data:
        msg = msg + "⁍ [" + element["title"] + "](" + element["link"] + ")\n\n"

    await event.edit(msg)
