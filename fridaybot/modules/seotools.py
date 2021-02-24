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

from seoanalyzer import analyze
import os

from uniborg.util import friday_on_cmd

from fridaybot import CMD_HELP
from fridaybot.utils import admin_cmd



@friday.on(admin_cmd(pattern="seo (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.edit("processing please wait ")
    site = input_str
    try:
      
      cmd = "seoanalyze " + site + " --output-format html > seo.html"
      await friday.run_cmd(cmd)
    
      await event.client.send_file(
        event.chat_id,
        "seo.html",
        caption=f"**Site SEO Analysed Successfully\n\nNote: Open This File With Chrome Or Any Browser\n\n\nSite Analysed By Friday\nGet Your Friday From** @FRIDAYCHAT",
      )
      com = "rm seo.html"
      await friday.run_cmd(com)
      await event.delete()
    except:
      await event.edit("Make Sure The Given Website URL is valid.")
    com = "rm seo.html"
    await friday.run_cmd(com)
    await event.delete()
    
    
    
    


CMD_HELP.update(
    {
        "seotools": "**Seo Tools**\
\n\n**Syntax : **`.seo <website URL>`\
\n**Usage :** Analyses SEO Of The Website.\
\n\n\n**Note : ** If The Website is too big, Userbot Crashes Because Of Insufficient Memory"
    }
)
