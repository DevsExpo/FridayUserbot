import pyjokes
from uniborg.util import friday_on_cmd

from userbot import CMD_HELP


@friday.on(friday_on_cmd(pattern=r"pjoke"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit(pyjokes.get_joke(category="all"))


CMD_HELP.update(
    {
        "programmer_jokes": "**Programmer Jokes**\
\n\n**Syntax : **`.pjoke`\
\n**Usage :** Get programmer jokes."
    }
)
