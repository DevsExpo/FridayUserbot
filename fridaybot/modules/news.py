#    Copyright (C) Midhun Km 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import requests

from fridaybot import CMD_HELP
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd
from fridaybot.Configs import Config

newslog = Config.NEWS_CHANNEL_ID


@friday.on(friday_on_cmd("news (.*)"))
@friday.on(sudo_cmd("news (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if Config.NEWS_CHANNEL_ID is None:
        await friday.edit_or_reply(
            event, "`Please ADD NEWS_CHANNEL_ID For This Module To Work`"
        )
        return
    infintyvar = event.pattern_match.group(1)
    main_url = f"https://inshortsapi.vercel.app/news?category={infintyvar}"
    stuber = await friday.edit_or_reply(
        event,
        f"Ok ! Fectching {infintyvar} From inshortsapi Server And Sending To News Channel",
    )
    await stuber.edit("All News Has Been Sucessfully Send To News Channel")
    starknews = requests.get(main_url).json()
    for item in starknews["data"]:
        sedlyf = item["content"]
        img = item["imageUrl"]
        writter = item["author"]
        dateis = item["date"]
        readthis = item["readMoreUrl"]
        titles = item["title"]
        sed1 = img
        sedm = f"**Title : {titles}** \n{sedlyf} \nDate : {dateis} \nAuthor : {writter} \nReadMore : {readthis}"
        await borg.send_file(newslog, sed1, caption=sedm)


CMD_HELP.update(
    {
        "news": "**News**\
\n\n**Syntax : **`.news <type of news>`\
\n**Usage :** Get latest news instantly to your private group"
    }
)
