
from uniborg.util import friday_on_cmd

from fridaybot import CMD_HELP
from fridaybot.utils import register




@friday.on(friday_on_cmd(pattern=r"gdn$"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("""
        ｡♥️｡･ﾟ♡ﾟ･｡♥️｡･｡･｡･｡♥️｡･
    ╱╱╱╱╱╱╱╭╮╱╱╱╭╮╱╭╮╭╮
    ╭━┳━┳━┳╯┃╭━┳╋╋━┫╰┫╰╮
    ┃╋┃╋┃╋┃╋┃┃┃┃┃┃╋┃┃┃╭┫
    ┣╮┣━┻━┻━╯╰┻━┻╋╮┣┻┻━╯
    ╰━╯╱╱╱╱╱╱╱╱╱╱╰━╯
        ｡♥️｡･ﾟ♡ﾟ･｡♥️° ♥️｡･ﾟ♡ﾟ
        """)



CMD_HELP.update(
    {
        "good_Night": ".gdn \
\nUsage: Say Good Night"
    }
)
