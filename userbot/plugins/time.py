import asyncio
import os
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont

from userbot import CMD_HELP
from userbot.utils import friday_on_cmd

FONT_FILE_TO_USE = "Fonts/go3v2.ttf"


@friday.on(friday_on_cmd("time ?(.*)"))  # pylint:disable=E0602
async def _(event):
    reply = await event.get_reply_message()
    if event.fwd_from:
        return
    current_time = datetime.now().strftime(
        "CipherX Timezone \n  Time: %H:%M:%S \n  Date: %d.%m.%y"
    )
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    event.message.id
    if input_str:
        current_time = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        previous_message.id
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):  # pylint:disable=E0602
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)  # pylint:disable=E0602
    # pylint:disable=E0602
    required_file_name = (
        Config.TMP_DOWNLOAD_DIRECTORY + " " + str(datetime.now()) + ".webp"
    )
    img = Image.new("RGBA", (350, 220), color=(0, 0, 0, 115))
    fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
    drawn_text = ImageDraw.Draw(img)
    drawn_text.text((10, 10), current_time, font=fnt, fill=(255, 255, 255))
    img.save(required_file_name)
    await borg.send_file(  # pylint:disable=E0602
        event.chat_id,
        required_file_name,
        caption="Time",
        reply_to=reply.id,
    )
    os.remove(required_file_name)
    end = datetime.now()
    time_taken_ms = (end - start).seconds
    await event.edit("Created sticker in {} seconds".format(time_taken_ms))
    await asyncio.sleep(5)
    await event.delete()


@friday.on(friday_on_cmd("gtime (.*)"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    logger.info(input_str)  # pylint:disable=E0602


CMD_HELP.update(
    {
        "time": "**Time**\
\n\n**Syntax : **`.time`\
\n**Usage :** Creates a sticker with present time and date."
    }
)
