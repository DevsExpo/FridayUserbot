# Credits ;- @mrconfused
from geopy.geocoders import Nominatim
from userbot.utils import admin_cmd
from telethon.tl import types
from userbot import CMD_HELP 


@borg.on(admin_cmd(pattern="gps ?(.*)"))
async def gps(event):
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    input_str = event.pattern_match.group(1)

    if not input_str:
        return await event.edit("Boss ! Give A Place To Search 😔 !.")

    await event.edit("Finding This Location In Maps Server.....")

    geolocator = Nominatim(user_agent="F.R.I.D.A.Y USERBOT")
    geoloc = geolocator.geocode(input_str)

    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await reply_to_id.reply(
            input_str,
            file=types.InputMediaGeoPoint(
                types.InputGeoPoint(
                    lat, lon
                )
            )
        )
        await event.delete()
    else:
        await event.edit("i coudn't find it")


CMD_HELP.update({"gps": "`.gps` <location name> :\
      \nUSAGE: Sends you the given location name\
      "
})
