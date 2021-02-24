#    Copyright (C) @chsaiujwal 2020-2021
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

from uniborg.util import friday_on_cmd
import requests
from fridaybot import CMD_HELP
from fridaybot.utils import admin_cmd
from fridaybot.Configs import Config




@friday.on(admin_cmd(pattern="gplink (.*)"))
async def _(event):
    if event.fwd_from:
        return
    if Config.GPLINKS_API_KEY is None:
        await event.edit(
            "Need to get an API key from https://gplinks.in\nModule stopping!"
        )
        return
    input_str = event.pattern_match.group(1)
    wtf = input_str.split(" ",1)
    ok = (wtf[0])
    no = (wtf[1])
    
    
    r = requests.get(f"https://gplinks.in/api?api={Config.GPLINKS_API_KEY}&url={ok}&alias={no}")
    
    kk = r.json()
    if kk.get("status")=="error":
	    ko = kk.get("message")
	    ok= ko [0]
	    hel = "Error, Reason:-  "+ok
    elif kk.get("status")=="success":
      
      pop = kk.get("shortenedUrl")
      
      hel = f"""
 
 Link Generated Successfully

Given Link:- {ok}

Shortened Link:- {pop}"""
    
    
    
    await borg.send_message(
        event.chat_id,
        hel,
        parse_mode="HTML"
    )
    
    await event.delete()


CMD_HELP.update(
    {
        "gplinks": "**GPLinks**\
\n\n**Syntax : **`.gplink <link to sshorten> <alias>`\
\n**Usage :** Shortens Given Link In GPlinks.\
\n\n**Example : **`.gplink google.com fridaytesto12`\
\nThis above syntax gives:- https://go.gplinks.co/fridaytesto12"
    }
)





    
