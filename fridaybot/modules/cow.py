""".cowsay, .tuxsay, .milksay, .kisssay, .wwwsay, .defaultsay, .bunnysay,
.moosesay, .sheepsay, .rensay, .cheesesay, .ghostbusterssay, .skeletonsay,
and may cmd would be added soon."""


from cowpy import cow
from telethon import events

from fridaybot import CMD_HELP


@friday.on(friday_on_cmd(pattern=r"(\w+)say (.*)"))
async def univsaye(cowmsg):
    if cowmsg.fwd_from:
        return
    """ For .cowsay module, uniborg wrapper for cow which says things. """
    if not cowmsg.text[0].isalpha() and cowmsg.text[0] not in ("/", "#", "@", "!"):
        arg = cowmsg.pattern_match.group(1).lower()
        text = cowmsg.pattern_match.group(2)

        if arg == "cow":
            arg = "default"
        if arg not in cow.COWACTERS:
            return
        cheese = cow.get_cow(arg)
        cheese = cheese()

        await cowmsg.edit(f"`{cheese.milk(text).replace('`', '´')}`")


CMD_HELP.update(
    {
        "cow": "**Cow**\
        \n\n**Syntax : **`.cowsay <text>`\
        \n\n**Syntax : **`.tuxsay <text>`\
        \n\n**Syntax : **`.milksay <text>`\
        \n\n**Syntax : **`.kisssay <text>`\
        \n\n**Syntax : **`.wwwsay <text>`\
        \n\n**Syntax : **`.defaultsay <text>`\
        \n\n**Syntax : **`.bunnysay <text>`\
        \n\n**Syntax : **`.moosesay <text>`\
        \n\n**Syntax : **`.sheepsay <text>`\
        \n\n**Syntax : **`.rensay <text>`\
        \n\n**Syntax : **`.cheesesay <text>`\
        \n\n**Syntax : **`.ghostbusterssay <text>`\
        \n\n**Syntax : **`.skeletonsay text>`\
        \n\n**Usage :** A fun plugin to get ur texts look like its being said by different characters"
    }
)
