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


from quote import quote

from fridaybot import CMD_HELP
from fridaybot.utils import admin_cmd


@friday.on(admin_cmd(pattern="qs (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    result = quote(input_str, limit=3)
    sed = ""

    for quotes in result:
        sed += str(quotes["quote"]) + "\n\n"

    await event.edit(
        f"<b><u>Quotes Successfully Gathered for given word </b></u><code>{input_str}</code>\n\n\n<code>{sed}</code>",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "quotes": "**Quotes**\
\n\n**Syntax : **`.qs <text>`\
\n**Usage :** Automatically gets quotes for given plugin."
    }
)
