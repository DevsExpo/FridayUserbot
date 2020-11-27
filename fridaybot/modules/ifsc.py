"""Query Indian Financial System Code to get address of the relevant bank or branch
Syntax: .ifsc rp <IFSC CODE>"""
import json

import requests
from uniborg.util import friday_on_cmd

from fridaybot import CMD_HELP


@friday.on(friday_on_cmd(pattern="ifsc(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    url = "https://ifsc.razorpay.com/{}".format(input_str)
    r = requests.get(url)
    if r.status_code == 200:
        b = r.json()
        a = json.dumps(b, sort_keys=True, indent=4)
        # https://stackoverflow.com/a/9105132/4723940
        await event.edit(str(a))
    else:
        await event.edit("`{}`: {}".format(input_str, r.text))


CMD_HELP.update(
    {
        "ifsc": "**IFSC**\
\n\n**Syntax : **`.ifsc <IFSC code>`\
\n**Usage :** gives you details about the bank."
    }
)
