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

from textblob import TextBlob

from fridaybot import CMD_HELP
from fridaybot.utils import admin_cmd


@friday.on(admin_cmd(pattern="spellcheck (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    a = input_str

    # print("original text: "+str(a))
    b = TextBlob(a)
    # print("corrected text: "+str(b.correct()))
    c = b.correct()
    await event.edit(
        f"<b><u>Check Completed</b></u> \n\n<b>Original Text</b>:-  <code>{a}</code> \n<b>Corrected Text:-</b> <code>{c}</code>",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "spellcheck": "**Spell Checker**\
\n\n**Syntax : **`.spellcheck <text to check>`\
\n**Usage :** Checks for spelling mistakes in given text."
    }
)
