#    Copyright (C) @chsaiujwal 2020
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

import pyjokes
from howdoi import howdoi

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd


@friday.on(friday_on_cmd(pattern=r"pjoke"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit(pyjokes.get_joke(category="all"))


@friday.on(friday_on_cmd(pattern="howdoi ?(.*)"))
async def __(event):
    query = event.pattern_match.group(1)
    if query == None:
        await event.edit("`Give Some Query First`")
        return
    output = howdoi.howdoi(query)
    lel = f"<b><u>Here is Your Answer</b></u> \n<code>{output}</code>"
    await event.edit(lel, parse_mode="HTML")


CMD_HELP.update(
    {
        "programmer_jokes": "**Programmer Jokes**\
\n\n**Syntax : **`.pjoke`\
\n**Usage :** Get programmer jokes.\
\n\n**Syntax : **`.howdoi <programming query>`\
\n**Usage :** Gives Answers For Given Programming Questions."
    }
)
