"""
Syntax : .gps <location name>
credits :@mrconfused
"""

# help from @sunda005 and @SpEcHIDe
# don't edit credits

from geopy.geocoders import Nominatim
from telethon.tl import types

from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd


@friday.on(friday_on_cmd(pattern="gps ?(.*)"))
@friday.on(sudo_cmd(pattern="gps ?(.*)", allow_sudo=True))
async def gps(event):
    starkislub = await edit_or_reply(event, "Processing")
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    input_str = event.pattern_match.group(1)

    if not input_str:
        return await starkislub.edit("what should i find give me location.")

    await starkislub.edit("finding")

    geolocator = Nominatim(user_agent="catfridaybot")
    geoloc = geolocator.geocode(input_str)

    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await reply_to_id.reply(
            input_str, file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon))
        )
        await event.delete()
    else:
        await starkislub.edit("i coudn't find it")
