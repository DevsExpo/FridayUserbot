#    Copyright (C) @chsaiujwal 2020-2021
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

from textblob import TextBlob
from telethon import events
from fridaybot.Configs import Config
from fridaybot.utils import admin_cmd


@friday.on(events.NewMessage)
async def _(event):
    if event.fwd_from:
        return
    if Config.AUTO_SPELL_FIX != True:
        return
    input_str = event.pattern_match.group(1)
    if input_str.startwith(".", "!", "'", "/", ":", "*"):
        pass
    else:
        bm = TextBlob(input_str)
        await event.edit(bm)
