"""Restart or Terminate the bot from any chat
Available Commands:
.restart
.shutdown"""
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
import os
import sys
from fridaybot.function.heroku_helper import HerokuHelper
from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd
import heroku3
import requests
Heroku = heroku3.from_key(Config.HEROKU_API_KEY)

@friday.on(friday_on_cmd("restart$"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("**Restarted ! If You Want To Check If I am Alive, Do** `.ping` !")
    try:
        herokuHelper = HerokuHelper(Config.HEROKU_APP_NAME, Config.HEROKU_API_KEY)
        herokuHelper.restart()
    except:
        await borg.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)


@friday.on(friday_on_cmd("shutdown$"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Turning off ...Manually turn me on later")
    if Config.HEROKU_API_KEY:
        app = Heroku.app(Config.HEROKU_APP_NAME)
        app.dynos['worker.1'].kill()
    else:
        await bot.disconnect()
        sys.exit(0)


CMD_HELP.update(
    {
        "power_tools": "**Power Tools**\
\n\n**Syntax : **`.restart`\
\n**Usage :** restarts your Friday userbot.\
\n\n**Syntax : **`.shutdown`\
\n**Usage :** Shuts down your Friday userbot."
    }
)
