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


from geopy.geocoders import Nominatim
from telethon.tl import types
import requests
import urllib.parse
from fridaybot import CMD_HELP
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd


@friday.on(friday_on_cmd(pattern="gps ?(.*)"))
@friday.on(sudo_cmd(pattern="gps ?(.*)", allow_sudo=True))
async def gps(event):
    if event.fwd_from:
        return
    starkislub = await friday.edit_or_reply(event, "Processing")
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    address = event.pattern_match.group(1)
    if not address:
        return await starkislub.edit("`Give Input Location.`")
    await starkislub.edit("`Searching..`")
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
    response = requests.get(url).json()
    try:
        lat = response[0]["lat"]
        lon = response[0]["lon"]
        await reply_to_id.reply(
            address, file=types.InputMediaGeoPoint(types.InputGeoPoint(float(lat), float(lon)))
        )
        await event.delete()
    except:
        await starkislub.edit("Location not found. Please try giving input with country.")


CMD_HELP.update(
    {
        "gps": "**Gps**\
\n\n**Syntax : **`.gps <location>`\
\n**Usage :** this plugin gives gps to the location."
    }
)
