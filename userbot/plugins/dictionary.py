"""Syntax: .meaning <word>"""

from PyDictionary import PyDictionary
from uniborg.util import edit_or_reply, friday_on_cmd, sudo_cmd

from userbot import CMD_HELP


@friday.on(friday_on_cmd("meaning (.*)"))
@friday.on(sudo_cmd("meaning (.*)", allow_sudo=True))
async def _(event):
    omg = await edit_or_reply(event, "Finding Meaning...")
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    dictionary = PyDictionary()
    a = dictionary.meaning(input_str)
    try:

        b = a.get("Noun")
    except:
        await omg.edit("Couldn't Find Meaning of Given Word")
    messi = ""
    for x in b:
        chsaiujwal += x + "\n"
    await omg.edit(
        f"<b> meaning of {input_str} is:-</b>\n {messi}",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "dictionary": "**Dictionary**\
\n\n**Syntax : **`.meaning <word>`\
\n**Usage :** Get meaning and pronunciation of a word."
    }
)
