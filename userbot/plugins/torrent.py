from the_python_bay import tpb

from userbot import CMD_HELP
from userbot.utils import admin_cmd


@friday.on(admin_cmd(pattern="torrent (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)

    kk = input_str
    results = tpb.search(kk)

    for torrent in results:
        await event.edit(
            f"<b><u>Torrents successfully gathered</b></u>\n\n <b>Torrent name:- </b><code>{torrent.name}</code>\n\n<b>Torrent:- </b><code>{torrent.magnet}</code>,\n\n <b>seeders:- </b><code>{torrent.seeders}</code>\n\n",
            parse_mode="HTML",
        )
        exit()


CMD_HELP.update(
    {
        "torrent": "**Torrent Searcher**\
\n\n**Syntax : **`.torrent <movie/series/software name>`\
\n**Usage :** Searches for torrent with given name."
    }
)
