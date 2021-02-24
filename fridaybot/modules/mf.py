import sys

from telethon import __version__, functions

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd

@friday.on(friday_on_cmd(pattern="dc"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetNearestDcRequest())  # pylint:disable=E0602
    await event.edit(result.stringify())


@friday.on(friday_on_cmd(pattern="config"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602
    result = result.stringify()
    logger.info(result)  # pylint:disable=E0602
    await event.edit("""Telethon UserBot powered by @UniBorg""")


CMD_HELP.update(
    {
        "mf": "**Mf**\
\n\n**Syntax : **`.mf`\
\n**Usage :** funny plugin.\
\n\n**Syntax : **`.dc`\
\n**Usage :** shows nearest Dc."
    }
)
