""" It does not do to dwell on dreams and forget to live
Syntax: .getime"""

import asyncio
import os
from datetime import datetime
import time
from PIL import Image, ImageDraw, ImageFont
import pytz 
from fridaybot import ALIVE_NAME, CMD_HELP, Lastupdate, friday_version
from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd

FONT_FILE_TO_USE = "Fonts/DroidSansMono.ttf"

IST = pytz.timezone(Config.TZ) 

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@friday.on(friday_on_cmd("time$"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    uptime = get_readable_time((time.time() - Lastupdate))
    TZ = pytz.timezone(Config.TZ)
    current_time = datetime.now(TZ).strftime(
        f"Time Zone : {Config.TZ} \n\nDate : %Y/%m/%d \nTime : %H:%M:%S \nUptime : {uptime} \nFriday - Version : {friday_version}"
    )
    start = datetime.now()
    reply_msg_id = event.message.id
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        reply_msg_id = previous_message.id
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):  
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    required_file_name = (
        Config.TMP_DOWNLOAD_DIRECTORY + " " + str(datetime.now()) + ".webp"
    )
    img = Image.new("RGBA", (600, 400), color=(0, 0, 0, 115))
    fnt = ImageFont.truetype(FONT_FILE_TO_USE, 35)
    drawn_text = ImageDraw.Draw(img)
    drawn_text.text((10, 10), current_time, font=fnt, fill=(255, 255, 255))
    img.save(required_file_name)
    await borg.send_file(  
        event.chat_id,
        required_file_name,
        reply_to=reply_msg_id,
    )
    os.remove(required_file_name)
    await event.delete()

    
@friday.on(friday_on_cmd("(ctime|timenow)$"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    TZ = pytz.timezone(Config.TZ)
    datetime_tz = datetime.now(TZ)
    oof = datetime_tz.strftime(f"**Time Zone :** `{Config.TZ}` \n\n**Date :** `%Y/%m/%d` \n**Time :** `%H:%M:%S`")
    await event.edit(oof)

CMD_HELP.update(
    {
        "time": "**Time**\
\n\n**Syntax : **`.time`\
\n**Usage :** Creates a sticker with present time and date."
    }
)
