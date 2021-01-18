#    Copyright (C) Midhun KM 2020
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
import os

import requests
from telethon.tl.types import MessageMediaPhoto

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd, sudo_cmd, admin_cmd
from pornhub_api import PornhubApi
from uniborg.util import friday_on_cmd



@friday.on(friday_on_cmd(pattern=r"nsfw"))
@friday.on(sudo_cmd(pattern=r"nsfw", allow_sudo=True))
async def nsfw(event):
    url = "https://nsfw-categorize.it/api/upload"
    await event.edit("`Processing..`")
    sed = await event.get_reply_message()
    photo = None
    sedpath = "./fridaydevs/"
    if sed and sed.media:
        if isinstance(sed.media, MessageMediaPhoto):
            photo = await borg.download_media(sed.media, sedpath)
        elif "image" in sed.media.document.mime_type.split("/"):
            photo = await borg.download_media(sed.media, sedpath)
        else:
            await event.edit("Reply To Image")
            return
    if photo:
        files = {"image": (f"{photo}", open(f"{photo}", "rb"))}
        r = requests.post(url, files=files).json()
        if r["status"] == "OK":
            await event.edit(
                "This image is classified as " + str(r["data"]["classification"])
            )
        if os.path.exists(photo):
            os.remove(photo)
        else:
            await event.edit("Response UnsucessFull. Try Again.")
            if os.path.exists(photo):
                os.remove(photo)


@friday.on(admin_cmd(pattern="phs (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    api = PornhubApi()
    data = api.search.search(
    input_str,
    ordering="mostviewed"
    )
    ok = 1
    oik = ""
    for vid in data.videos:
      if ok<=5:
        oik +=(f"""
Video title:- {vid.title}
Video link:- https://www.pornhub.com/view_video.php?viewkey={vid.video_id}



        """)
        ok = ok+1
      else:
        pass
    
    oiko = "<b>Links Generated Successfully</b>"+"\n"+"Search Query:- "+input_str+"\n"+oik
    
    await borg.send_message(
        event.chat_id,
        oiko,
        parse_mode="HTML",
    )
    await event.delete()




CMD_HELP.update(
    {
        "nsfw": "**NSFW**\
\n\n**Syntax : **`.nsfw <reply to image>`\
\n**Usage :** Checks if the replyed image is nsfw or not.\
\n\n**Syntax : **`.phs <query>`\
\n**Usage :** Searches PornHub Website With Given Query."
    }
)
