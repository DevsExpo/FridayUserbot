"""XKCD Search
Syntax: .xkcd <search>"""
from urllib.parse import quote

import requests
from uniborg.util import admin_cmd, edit_or_reply, sudo_cmd


@borg.on(admin_cmd(pattern="xkcd ?(.*)"))
@borg.on(sudo_cmd(pattern="xkcd ?(.*)", allow_sudo=True))
async def _(event):
    livinglegend = await edit_or_reply(event, "Oh SeD Pls Wait")
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    xkcd_id = None
    if input_str:
        if input_str.isdigit():
            xkcd_id = input_str
        else:
            xkcd_search_url = "https://relevantxkcd.appspot.com/process?"
            queryresult = requests.get(
                xkcd_search_url, params={"action": "xkcd", "query": quote(input_str)}
            ).text
            xkcd_id = queryresult.split(" ")[2].lstrip("\n")
    if xkcd_id is None:
        xkcd_url = "https://xkcd.com/info.0.json"
    else:
        xkcd_url = "https://xkcd.com/{}/info.0.json".format(xkcd_id)
    r = requests.get(xkcd_url)
    if r.ok:
        data = r.json()
        year = data.get("year")
        month = data["month"].zfill(2)
        day = data["day"].zfill(2)
        xkcd_link = "https://xkcd.com/{}".format(data.get("num"))
        safe_title = data.get("safe_title")
        data.get("transcript")
        alt = data.get("alt")
        img = data.get("img")
        data.get("title")
        output_str = """[\u2060]({})**{}**
[XKCD ]({})
Title: {}
Alt: {}
Day: {}
Month: {}
Year: {}""".format(
            img, input_str, xkcd_link, safe_title, alt, day, month, year
        )
        await livinglegend.edit(output_str, link_preview=True)
    else:
        await livinglegend.edit("xkcd n.{} not found!".format(xkcd_id))
