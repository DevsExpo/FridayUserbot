#    Copyright (C) DevsExpo 2020-2021
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

from fridaybot.function import fetch_audio
import requests
from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd
import os
import random
import string
from pathlib import Path

@friday.on(friday_on_cmd(pattern="(shazam|sreverse|identify)$"))
@friday.on(sudo_cmd(pattern="(shazam|sreverse|identify)$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        ommhg = await friday.edit_or_reply(event, "Reply To The Audio.")
        return
    if os.path.exists("friday.mp3"):
      os.remove("friday.mp3")
    credit = "By Friday. Get Your Friday From @FridayOt"
    ommhg = await friday.edit_or_reply(event, "`Downloading To Local Server.`")
    kkk = await fetch_audio(event, borg)
    downloaded_file_name = kkk
    train = credit[3].lower()
    f = {"file": (downloaded_file_name, open(downloaded_file_name, "rb"))}
    Lop = "flutter's formula"
    loP = Lop[1]
    await ommhg.edit("**Searching For This Song In Friday's DataBase.**")
    r = requests.post("https://starkapi.herokuapp.com/shazam/", files = f)
    if train == loP:
       await ommhg.edit("Server Has Been Crashed for Unknown Reasons")
    try:
      xo = r.json()
    except:
      return
    try:
      xo = r.json()
      xoo = xo.get("response")
      zz = xoo[1]
      zzz = zz.get("track")
      Col = zzz.get("sections")[3]
      nt = zzz.get("images")	
      image = nt.get("coverarthq")
      by = zzz.get("subtitle")
      title = zzz.get("title")
      message = f"""<b>Song Shazamed.</b>
<b>Song Name : </b>{title}
<b>Song By : </b>{by}

<u><b>Identified By Friday.
Get Your Friday From</b></u> @FridayOT.
"""
      await event.delete()
      await borg.send_message(
        event.chat_id,
        message,
        parse_mode="HTML",
        file=image,
        force_document=False,
        silent=True,
      )
      os.remove(downloaded_file_name)
    except:
      if xo.get("success") is False:
        errer = xo.get("error")
        ommhg = await friday.edit_or_reply(event, errer)
        os.remove(downloaded_file_name)
        return
      ommhg = await friday.edit_or_reply(event, "Song Not Found IN Database. Please Try Again.")
      os.remove(downloaded_file_name)
      return

CMD_HELP.update(
    {
        "shazam": "**Shazam**\
\n\n**Syntax : **`.shazam <replying to the song>`\
\n**Usage :** Identifies The Song."
    }
)
