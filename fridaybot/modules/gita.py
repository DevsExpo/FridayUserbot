# Author: Shubhendra Kushwaha (@TheShubhendra)
# Email: shubhendrakushwaha94@gmail.com
import pygita

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd

CLIENT_ID = Var.GITA_CLIENT_ID
CLIENT_SECRET = Var.GITA_CLIENT_SECRET
""" Get API crendentials from https://bhagavadgita.io . """


@friday.on(friday_on_cmd(pattern="gita +(.*) +(.*)$"))
async def gita(event):
    """ To get a specific verse from a specific chapter in English. """
    if CLIENT_ID is None or CLIENT_SECRET is None:
        await event.edit(
            event,
            "`Please add required GITA_CLIENT_SECRET and GITA_CLIENT_ID env var`",
            10,
        )
        return
    pygita.auth(CLIENT_ID, CLIENT_SECRET)
    try:
        chapter_number = int(event.pattern_match.group(1))
        verse_number = int(event.pattern_match.group(2))
    except ValueError:
        return
    verse = pygita.get_verse(chapter_number, verse_number, language="en")
    await event.edit(f"**{verse.text}** {verse.meaning}")


@friday.on(friday_on_cmd(pattern="gita +(.*) +(.*) hi$"))
async def gita(event):
    """ To get a specific verse from a specific chapter in Hindi. """
    if CLIENT_ID is None or CLIENT_SECRET is None:
        await event.edit(
            event,
            "`Please add required GITA_CLIENT_SECRET and GITA_CLIENT_ID env var`",
            10,
        )
        return
    pygita.auth(CLIENT_ID, CLIENT_SECRET)
    chapter_number = int(event.pattern_match.group(1))
    verse_number = int(event.pattern_match.group(2))
    verse = pygita.get_verse(chapter_number, verse_number, language="hi")
    await event.edit(f"**{verse.text}** {verse.meaning}")

CMD_HELP.update(
    {
        "gita": "**gita**\
\n\n**Syntax : **`.verse <chapter_number> <verse_number>`\
\n**Usage :** Get a specific verse from a particular chapter\
\n\n**Syntax : **`.verse <chapter_number> <verse_number> hi`\
\n**Usage :** Get a specific verse from a particular chapter in hindi.\n"
    }
)
