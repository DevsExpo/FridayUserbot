#    Copyright (C) Midhun KM 2020-2021
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

from fridaybot.Configs import Config
import time
from telethon import __version__ as tv
import sys
import platform
from git import Repo
from fridaybot import ALIVE_NAME
from fridaybot import bot
from fridaybot.modules import currentversion

# only Owner Can Use it
@assistant_cmd("alive", is_args=False)
@peru_only
async def friday(event):
    await event.reply(f"`Yo ! {bot.me.first_name} , I am Alive. Need Help ? Maybe You Should Pm Me.`")
