from quote import quote

from userbot import CMD_HELP
from userbot.utils import admin_cmd


@friday.on(admin_cmd(pattern="quote (.*)"))
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
\n\n**Syntax : **`.quote <text>`\
\n**Usage :** Automatically gets quotes for given plugin."
    }
)
