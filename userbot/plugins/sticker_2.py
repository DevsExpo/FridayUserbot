# Ported From https://github.com/eyaadh/stickerBot
# (C) @Eyaadh
# Ported By @StarkXD

import html
import itertools
import os
import secrets
from textwrap import TextWrapper

from PIL import Image, ImageChops, ImageDraw, ImageFont
from telethon.tl.functions.users import GetFullUserRequest

from userbot.utils import friday_on_cmd


async def get_y_and_heights(text_wrapped, dimensions, margin, font):
    _, descent = font.getmetrics()
    line_heights = [
        font.getmask(text_line).getbbox()[3] + descent + margin
        for text_line in text_wrapped
    ]
    line_heights[-1] -= margin
    height_text = sum(line_heights)
    y = (dimensions[1] - height_text) // 2
    return y, line_heights


async def crop_to_circle(im):
    bigsize = (im.size[0] * 3, im.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    ImageDraw.Draw(mask).ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(im.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, im.split()[-1])
    im.putalpha(mask)


async def rounded_rectangle(rectangle, xy, corner_radius, fill=None, outline=None):
    upper_left_point = xy[0]
    bottom_right_point = xy[1]

    rectangle.pieslice(
        [
            upper_left_point,
            (
                upper_left_point[0] + corner_radius * 2,
                upper_left_point[1] + corner_radius * 2,
            ),
        ],
        180,
        270,
        fill=fill,
        outline=outline,
    )
    rectangle.pieslice(
        [
            (
                bottom_right_point[0] - corner_radius * 2,
                bottom_right_point[1] - corner_radius * 2,
            ),
            bottom_right_point,
        ],
        0,
        90,
        fill=fill,
        outline=outline,
    )
    rectangle.pieslice(
        [
            (upper_left_point[0], bottom_right_point[1] - corner_radius * 2),
            (upper_left_point[0] + corner_radius * 2, bottom_right_point[1]),
        ],
        90,
        180,
        fill=fill,
        outline=outline,
    )
    rectangle.pieslice(
        [
            (bottom_right_point[0] - corner_radius * 2, upper_left_point[1]),
            (bottom_right_point[0], upper_left_point[1] + corner_radius * 2),
        ],
        270,
        360,
        fill=fill,
        outline=outline,
    )
    rectangle.rectangle(
        [
            (upper_left_point[0], upper_left_point[1] + corner_radius),
            (bottom_right_point[0], bottom_right_point[1] - corner_radius),
        ],
        fill=fill,
        outline=fill,
    )
    rectangle.rectangle(
        [
            (upper_left_point[0] + corner_radius, upper_left_point[1]),
            (bottom_right_point[0] - corner_radius, bottom_right_point[1]),
        ],
        fill=fill,
        outline=fill,
    )
    rectangle.line(
        [
            (upper_left_point[0] + corner_radius, upper_left_point[1]),
            (bottom_right_point[0] - corner_radius, upper_left_point[1]),
        ],
        fill=outline,
    )
    rectangle.line(
        [
            (upper_left_point[0] + corner_radius, bottom_right_point[1]),
            (bottom_right_point[0] - corner_radius, bottom_right_point[1]),
        ],
        fill=outline,
    )
    rectangle.line(
        [
            (upper_left_point[0], upper_left_point[1] + corner_radius),
            (upper_left_point[0], bottom_right_point[1] - corner_radius),
        ],
        fill=outline,
    )
    rectangle.line(
        [
            (bottom_right_point[0], upper_left_point[1] + corner_radius),
            (bottom_right_point[0], bottom_right_point[1] - corner_radius),
        ],
        fill=outline,
    )


@borg.on(friday_on_cmd(pattern="ghost ?(.*)"))
async def create_sticker(event):
    if not event.reply_to_msg_id:
        event.edit("Reply to message :/")
        return
    loln = await event.edit("`Processing...`")
    ps = await event.get_reply_message()
    this_nub = await borg(GetFullUserRequest(ps.sender_id))
    m = ps.text
    if len(m) < 100:
        body_font_size = 35
        wrap_size = 30
    elif len(m) < 200:
        body_font_size = 30
        wrap_size = 35
    elif len(m) < 500:
        body_font_size = 20
        wrap_size = 40
    elif len(m) < 1000:
        body_font_size = 12
        wrap_size = 80
    else:
        body_font_size = 8
        wrap_size = 100
    font = ImageFont.truetype("Fonts/Segan-Light.ttf", body_font_size)
    font_who = ImageFont.truetype("Fonts/TitilliumWeb-Bold.ttf", 24)
    img = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle = rounded_rectangle
    wrapper = TextWrapper(
        width=wrap_size, break_long_words=False, replace_whitespace=False
    )
    lines_list = [wrapper.wrap(i) for i in m.split("\n") if i != ""]
    text_lines = list(itertools.chain.from_iterable(lines_list))
    y, line_heights = await get_y_and_heights(text_lines, (512, 512), 10, font)
    in_y = y
    rec_y = (y + line_heights[0]) if wrap_size >= 40 else y
    for i, _ in enumerate(text_lines):
        rec_y += line_heights[i]

    await rounded_rectangle(
        draw, ((90, in_y), (512, rec_y + line_heights[-1])), 10, fill="#effcde"
    )

    first_name = html.escape(this_nub.user.first_name)
    # https://stackoverflow.com/a/5072031/4723940
    # Some Deleted Accounts do not have first_name
    if first_name is not None:
        # some weird people (like me) have more than 4096 characters in their names
        first_name = first_name.replace("\u2060", "")
    last_name = this_nub.user.last_name
    # last_name is not Manadatory in @Telegram
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
        last_name = "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"

    f_user = first_name + " " + last_name if last_name else first_name
    draw.text((100, y), f"{f_user}:", "#588237", font=font_who)
    y = (y + (line_heights[0] * (20 / 100))) if wrap_size >= 40 else y
    for i, line in enumerate(text_lines):
        x = 100
        y += line_heights[i]
        draw.text((x, y), line, "#030303", font=font)

    try:
        photo = await borg.download_profile_photo(
            this_nub.user.id, Config.TMP_DOWNLOAD_DIRECTORY
        )
    except Exception as e:
        photo = "resources/stcr/default.jpg"
        logger.info(e)
    im = Image.open(photo).convert("RGBA")
    im.thumbnail((60, 60))
    await crop_to_circle(im)
    img.paste(im, (20, in_y))
    sticker_file = f"{secrets.token_hex(2)}.webp"
    img.save(sticker_file)
    await loln.delete()
    await borg.send_file(event.chat_id, file=sticker_file)
    try:
        if os.path.isfile(sticker_file):
            os.remove(sticker_file)
        if os.path.isfile(photo) and (photo != "default.jpg"):
            os.remove(photo)
    except Exception as e:
        logger.info(e)
