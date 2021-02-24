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

"""command: .currency usd inr"""
from datetime import datetime

import requests
from uniborg.util import friday_on_cmd

from fridaybot import CMD_HELP


@friday.on(friday_on_cmd(pattern="currency (.*)"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    input_sgra = input_str.split(" ")
    if len(input_sgra) == 3:
        try:
            number = float(input_sgra[0])
            currency_from = input_sgra[1].upper()
            currency_to = input_sgra[2].upper()
            request_url = "https://api.exchangeratesapi.io/latest?base={}".format(
                currency_from
            )
            current_response = requests.get(request_url).json()
            if currency_to in current_response["rates"]:
                current_rate = float(current_response["rates"][currency_to])
                rebmun = round(number * current_rate, 2)
                await event.edit(
                    "**According to current rates,**\n {} **{}** = {} **{}**\n \n●▬▬▬▬▬ஜ۩❀۩ஜ▬▬▬▬▬●\n\n**Current Conversion Rates:**\n 1 **{}** = {} **{}**".format(
                        number,
                        currency_from,
                        rebmun,
                        currency_to,
                        currency_from,
                        current_rate,
                        currency_to,
                    )
                )
            else:
                await event.edit(
                    "Welp, Hate to tell yout this but this Currency isn't supported **yet**.\n__Try__ `.currencies` __for a list of supported currencies.__"
                )
        except e:
            await event.edit(str(e))
    else:
        await event.edit(
            "**Syntax:**\n.currency amount from to\n**Example:**\n`.currency 10 usd inr`"
        )
    end = datetime.now()
    (end - start).seconds


@friday.on(friday_on_cmd(pattern="currencies (.*)"))
async def list(ups):
    if ups.fwd_from:
        return
    request_url = "https://api.exchangeratesapi.io/latest?base=USD"
    current_response = requests.get(request_url).json()
    dil_wale_puch_de_na_chaaa = current_response["rates"]
    for key, value in dil_wale_puch_de_na_chaaa.items():
        await borg.send_message(
            ups.chat_id,
            "**List of currencies:**\n {}\n*Tip:** Use `.gs` currency_code for more details on the currency.".format(
                key
            ),
        )


CMD_HELP.update(
    {
        "currency": "**Currency**\
\n\n**Syntax : **`.currency <amount> <from> <to>`\
\n**Usage :** It converts given amount from one currency to another.\
\n\n**Syntax : **`.currencies`\
\n**Usage :** List all the currencies."
    }
)
