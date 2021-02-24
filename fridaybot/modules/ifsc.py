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

import requests
from uniborg.util import friday_on_cmd

from fridaybot import CMD_HELP


@friday.on(friday_on_cmd(pattern="ifsc (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)

    IFSC_Code = input_str

    URL = "https://ifsc.razorpay.com/"

    data = requests.get(URL + IFSC_Code).json()

    a = data["ADDRESS"]
    b = data["CENTRE"]
    c = data["BRANCH"]
    d = data["CITY"]
    e = data["STATE"]
    f = data["BANK"]
    g = data["BANKCODE"]
    h = data["IFSC"]

    await event.edit(
        f"<b><u>INFORMATION GATHERED SUCCESSFULLY</b></u>\n\n<b>Bank Name :-</b><code>{f}</code>\n<b>Bank Address:- </b> <code>{a}</code>\n<b>Centre :-</b><code>{b}</code>\n<b>Branch :- </b><code>{c}</code>\n<b> City :-</b><code>{d}</code>\n<b>State:- </b> <code>{e}</code>\n<b>Bank Code :- </b><code>{g}</code>\n<b>Ifsc :-</b><code>{h}</code>",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "ifsc": "**IFSC**\
\n\n**Syntax : **`.ifsc <IFSC code>`\
\n**Usage :** gives you details about the bank."
    }
)
