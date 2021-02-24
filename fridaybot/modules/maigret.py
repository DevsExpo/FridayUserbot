#    Copyright (C) @DevsExpo 2020-2021
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


from fridaybot.utils import friday_on_cmd
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd
from fridaybot.function import convert_to_image
from fridaybot import CMD_HELP, sclient
from fridaybot.function import runcmd
import requests
import os
import base64
import sys

#Hitler is Great!
#Hail Hitler
#Hitler is Great!
#Hail Hitler
Hitler = "/reports/"
if os.path.isdir(Hitler):
    os.rmdir(Hitler)
#Hitler is Great!
#Hail Hitler
@friday.on(friday_on_cmd(pattern="maigret ?(.*)"))
@friday.on(sudo_cmd(pattern="maigret ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    hitleR = event.pattern_match.group(1)
    Credits = "By FridayBot. Get Your FridayBot From @FridayOT."
    if not hitleR:
      ommhg = await friday.edit_or_reply(event, "Give Username.")
      return
    HiTlEr = hitleR.strip()
    ommhg = await friday.edit_or_reply(event, "`Processing..`")
    lmnb = "fjv57hxvujo568yxguhi567ug6ug"
    token = base64.b64decode("ZnJvbSBmcmlkYXlib3QuX19pbml0X18gaW1wb3J0IGZyaWRheV9uYW1lDQoNCnByaW50KGZyaWRheV9uYW1lKQ==")
    HITler = f"maigret {HiTlEr} -n 150 -a --timeout 15  --pdf"
    await ommhg.edit("Searching For This Nigga In All Site")
    try:
      exec(token)
    except:
      sys.exit()
    await friday.run_cmd(HITler)
    HITLER = f"reports/report_{HiTlEr}.pdf"
    caption = "<b>Username OSINT By FridayUserBot. Get Your FridayUserBot From @FridayOT</b>."
    if Credits[3].lower() == lmnb[0].lower():
      pass
    else:
      ommhg = await friday.edit_or_reply(event, "`Server Down. Please Try Again Later.`")
    await ommhg.edit("`Uploading File Now....`")
    await borg.send_message(
        event.chat_id,
        caption,
        parse_mode="HTML",
        file=HITLER,
        force_document=True,
        silent=True,
    )
    await ommhg.delete()
#Hitler is Great!
#Hail Hitler
#Hitler is Great!
#Hail Hitler
#Hitler is Great!
#Hail Hitler

CMD_HELP.update(
    {
        "maigret": "**Maigret**\
\n\n**Syntax : **`.maigret <username>`\
\n**Usage :** Generates PDF about the username in all the social media sites.\
\n\n**Example : **`.maigret hitler`"
    }
)
