# Modded from dagd.py
"""
Animate How To Google
Command .ggl Search Query
By @Hackintush
"""

import requests
from userbot import CMD_HELP
from userbot.utils import friday_on_cmd


@friday.on(friday_on_cmd("ggl (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://lmgtfy.com/?q={}%26iie=1".format(
        input_str.replace(" ", "+")
    )
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit(
            "[{}]({})\n`Thank's to [CɪᴘʜᴇʀX](https://t.me/Hackintush) 🙃` ".format(
                input_str, response_api.rstrip()
            )
        )
    else:
        await event.edit("something is wrong. please try again later.")
        
CMD_HELP.update(
    {
        "howtogoogle": "**How To Google**\
\n\n**Syntax : **`.ggl <search query>`\
\n**Usage :** Animates how to Google with search query."
    }
)
