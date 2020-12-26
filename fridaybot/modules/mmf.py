#    Copyright (C) Midhun KM 2020
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

import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

from fridaybot.function import convert_to_image
from fridaybot.utils import friday_on_cmd

sedpath = Config.TMP_DOWNLOAD_DIRECTORY


@friday.on(friday_on_cmd(pattern="memify (.*)"))
async def starkmeme(event):
    hmm = event.pattern_match.group(1)
    if hmm == None:
        await event.edit("Give Some Text")
        return
    if not event.reply_to_msg_id:
        await event.edit("`PLease, Reply To A MsG`")
        return
    mryeast = await event.edit("Making Memes Until Praise MrBeast.")
    await event.get_reply_message()
    seds = await convert_to_image(event, borg)
    if ";" in hmm:
        stark = hmm.split(";", 1)
        first_txt = stark[0]
        second_txt = stark[1]
        top_text = first_txt
        bottom_text = second_txt
        generate_meme(seds, top_text=top_text, bottom_text=bottom_text)
        imgpath = sedpath + "/" + "memeimg.png"
        await borg.send_file(event.chat_id, imgpath)
        if os.path.exists(imgpath):
            os.remove(imgpath)
        await mryeast.delete()
    else:
        top_text = hmm
        bottom_text = ""
        generate_meme(seds, top_text=top_text, bottom_text=bottom_text)
        imgpath = sedpath + "/" + "memeimg.png"
        await borg.send_file(event.chat_id, imgpath)
        if os.path.exists(imgpath):
            os.remove(imgpath)
        await mryeast.delete()


def generate_meme(
    image_path, top_text, bottom_text="", font_path="Fonts/impact.ttf", font_size=11
):
    im = Image.open(image_path)
    draw = ImageDraw.Draw(im)
    image_width, image_height = im.size
    font = ImageFont.truetype(font=font_path, size=int(image_height * font_size) // 100)
    top_text = top_text.upper()
    bottom_text = bottom_text.upper()
    char_width, char_height = font.getsize("A")
    chars_per_line = image_width // char_width
    top_lines = textwrap.wrap(top_text, width=chars_per_line)
    bottom_lines = textwrap.wrap(bottom_text, width=chars_per_line)
    y = 9
    for line in top_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x - 2, y - 2), line, font=font, fill="black")
        draw.text((x + 2, y - 2), line, font=font, fill="black")
        draw.text((x + 2, y + 2), line, font=font, fill="black")
        draw.text((x - 2, y + 2), line, font=font, fill="black")
        draw.text((x, y), line, fill="white", font=font)
        y += line_height

    y = image_height - char_height * len(bottom_lines) - 14
    for line in bottom_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x - 2, y - 2), line, font=font, fill="black")
        draw.text((x + 2, y - 2), line, font=font, fill="black")
        draw.text((x + 2, y + 2), line, font=font, fill="black")
        draw.text((x - 2, y + 2), line, font=font, fill="black")
        draw.text((x, y), line, fill="white", font=font)
        y += line_height
    file_name = "memeimg.png"
    ok = sedpath + "/" + file_name
    im.save(ok, "PNG")
