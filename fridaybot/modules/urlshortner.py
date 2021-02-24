#    Copyright (C) Midhun Km 2020-2021
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

import pyshorteners

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd, sudo_cmd


@friday.on(friday_on_cmd(pattern="urlshort (.*)"))
@friday.on(sudo_cmd(pattern="urlshort (.*)", allow_sudo=True))
async def vom(event):
    if event.fwd_from:
        return
    try:
        link = event.pattern_match.group(1)
        sed = pyshorteners.Shortener()
        kek = sed.tinyurl.short(link)
        bestisbest = (
            f"<b>Url Shortened</b> \n<b><u>Given Link</u></b> ➠ {link}\n"
            f"<b><u>Shortened Link</u></b> ➠ {kek}"
        )
        await event.edit(bestisbest, parse_mode="HTML")
    except Exception as e:
        await event.edit("SomeThing Went Wrong. \nError : " + e)


CMD_HELP.update(
    {
        "urlshortner": "**URL shortner**\
\n\n**Syntax : **`.urlshort <url link>`\
\n**Usage :** Shortens the given URL."
    }
)
