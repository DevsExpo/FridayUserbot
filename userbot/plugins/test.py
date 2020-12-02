from uniborg.util import friday_on_cmd

from userbot import CMD_HELP


@friday.on(friday_on_cmd(pattern=r"test"))
async def test(event):
    if event.fwd_from:
        return
    await event.edit("⚜ Test Successfull Boss ⚜")


CMD_HELP.update(
    {
        "test": "**Test**\
\n\n**Syntax : **`.test`\
\n**Usage :** Just a test plugin."
    }
)
