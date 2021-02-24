#    Copyright (C) DevsExpo 2020-2021
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
import wget
from shutil import rmtree
import cv2
import cv2 as cv
import random
import numpy as np
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont, ImageColor
import pytz 
import asyncio
import requests
from PIL import Image, ImageDraw, ImageFont
from telegraph import upload_file
from fridaybot import CMD_HELP
from fridaybot.function import convert_to_image, crop_vid, runcmd, tgs_to_gif, progress, humanbytes, time_formatter, is_nsfw
import os
from glitch_this import ImageGlitcher
from telethon.tl.types import MessageMediaPhoto
from pygifsicle import optimize
from fridaybot import CMD_HELP
import asyncio
import math
import os
import time
import time
from fridaybot.function.FastTelethon import upload_file as uf
from fridaybot.utils import friday_on_cmd, sudo_cmd, edit_or_reply
import html
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
import os
import base64
import sys
from telethon.utils import get_input_location
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

sedpath = "./starkgangz/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)
    
glitcher = ImageGlitcher()
DURATION = 200
LOOP = 0


@friday.on(friday_on_cmd(pattern=r"cit"))
@friday.on(sudo_cmd(pattern=r"cit", allow_sudo=True))
async def hmm(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    hmmu = await event.edit("Colourzing..")
    await event.get_reply_message()
    img = await convert_to_image(event, borg)
    net = cv2.dnn.readNetFromCaffe(
        "./resources/imgcolour/colouregex.prototxt",
        "./resources/imgcolour/colorization_release_v2.caffemodel",
    )
    
    pts = np.load("./resources/imgcolour/pts_in_hull.npy")
    class8 = net.getLayerId("class8_ab")
    conv8 = net.getLayerId("conv8_313_rh")
    pts = pts.transpose().reshape(2, 313, 1, 1)
    net.getLayer(class8).blobs = [pts.astype("float32")]
    net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]
    image = cv2.imread(img)
    scaled = image.astype("float32") / 255.0
    lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)
    resized = cv2.resize(lab, (224, 224))
    L = cv2.split(resized)[0]
    L -= 50
    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0, :, :, :].transpose((1, 2, 0))
    ab = cv2.resize(ab, (image.shape[1], image.shape[0]))
    L = cv2.split(lab)[0]
    colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
    colorized = np.clip(colorized, 0, 1)
    colorized = (255 * colorized).astype("uint8")
    file_name = "Colour.png"
    ok = sedpath + "/" + file_name
    cv2.imwrite(ok, colorized)
    await borg.send_file(event.chat_id, ok)
    await hmmu.delete()
    for files in (ok, img):
        if files and os.path.exists(files):
            os.remove(files)
            
@friday.on(friday_on_cmd(pattern=r"(getthumb|ethumb|gethumb)$"))
async def thumbnailer(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Reply to any Media File. I will Send You Its Thumb.`")
        return
    is_reply = await event.get_reply_message()
    try:
        thumbstark = await event.client.download_media(is_reply.media, thumb=-1)
    except:
        await event.edit("`Well, My Eyes Couldn't Find Any Thumb. :/`")
        return
    await event.delete()
    await event.client.send_file(event.chat_id, thumbstark, reply_to=is_reply)

# Firstly Released By @DELETEDUSER420
@friday.on(friday_on_cmd(pattern=r"nst"))
@friday.on(sudo_cmd(pattern=r"nst", allow_sudo=True))
async def hmm(event):
    if event.fwd_from:
        return
    life = Config.DEEP_API_KEY
    if life == None:
        life = "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"
        await event.edit("No Api Key Found, Please Add it. For Now Using Local Key")
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    headers = {"api-key": life}
    hmm = await event.edit("Colourzing..")
    await event.get_reply_message()
    img = await convert_to_image(event, borg)
    img_file = {
        "image": open(img, "rb"),
    }
    url = "https://api.deepai.org/api/nsfw-detector"
    r = requests.post(url=url, files=img_file, headers=headers).json()
    sedcopy = r["output"]
    hmmyes = sedcopy["detections"]
    game = sedcopy["nsfw_score"]
    final = f"**IMG RESULT** \n**Detections :** `{hmmyes}` \n**NSFW SCORE :** `{game}`"
    await borg.send_message(event.chat_id, final)
    await hmm.delete()
    if os.path.exists(img):
        os.remove(img)

@friday.on(friday_on_cmd(pattern="(nsfw|checknsfw|nsfwdetect)$"))
@friday.on(sudo_cmd(pattern="nsfw$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await friday.edit_or_reply(event, "Reply To Any Image Idiot.")
        return
    reply_message = await event.get_reply_message()
    kok = await friday.edit_or_reply(event, "`Processing...`")
    IdkWtf = await is_nsfw(reply_message)
    if IdkWtf is False:
      await kok.edit("**IMAGE-RESULT** \n**NSFW :** `False`")
      return
    elif IdkWtf is True:
      await kok.edit("**IMAGE-RESULT** \n**NSFW :** `True`")
      return 
    
@friday.on(friday_on_cmd(pattern="color (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
    if input_str.startswith("#"):
        try:
            usercolor = ImageColor.getrgb(input_str)
        except Exception as e:
            await event.edit(str(e))
            return False
        else:
            im = Image.new(mode="RGB", size=(1280, 720), color=usercolor)
            im.save("@Colour.png", "PNG")
            input_str = input_str.replace("#", "#COLOR_")
            await borg.send_file(
                event.chat_id,
                "@Colour.png",
                force_document=False,
                caption=input_str,
                reply_to=message_id,
            )
            os.remove("@Colour.png")
            await event.delete()
    else:
        await event.edit("Syntax: `.color <color_code>`")
        

        
@friday.on(friday_on_cmd(pattern="picgen"))
@friday.on(sudo_cmd(pattern="picgen", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    
    url = "https://thispersondoesnotexist.com/image"
    response = requests.get(url)
    poppy = await friday.edit_or_reply(event, "Creating a fake face for you... 🌚")
    if response.status_code == 200:
      with open("FRIDAYOT.jpg", 'wb') as f:
        f.write(response.content)
    
    captin = f"Fake Image By Friday.\nGet Your Own Friday From @FRIDAYCHAT."
    fole = "FRIDAYOT.jpg"
    await borg.send_file(event.chat_id, fole, caption=captin)
    await poppy.delete()
    await friday.run_cmd("rm /root/fridaybot/FRIDAYOT.jpg ")
    
@friday.on(friday_on_cmd(pattern=r"thug"))
@friday.on(sudo_cmd(pattern=r"thug", allow_sudo=True))
async def iamthug(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    hmm = await event.edit("`Converting To thug Image..`")
    await event.get_reply_message()
    img = await convert_to_image(event, borg)
    imagePath = img
    maskPath = "./resources/thuglife/mask.png"
    cascPath = "./resources/thuglife/face_regex.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.15)
    background = Image.open(imagePath)
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
    file_name = "fridaythug.png"
    ok = sedpath + "/" + file_name
    background.save(ok, "PNG")
    await borg.send_file(event.chat_id, ok)
    await hmm.delete()
    for files in (ok, img):
        if files and os.path.exists(files):
            os.remove(files)

@friday.on(friday_on_cmd(pattern=r"msk ?(.*)"))
async def iamnone(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    hmm = await event.edit("`Converting To Masked Image..`")
    await event.get_reply_message()
    img = await convert_to_image(event, borg)
    imagePath = img
    wget_s = wget.download(event.pattern_match.group(1), out=Config.TMP_DOWNLOAD_DIRECTORY)
    maskPath = wget_s
    cascPath = "./resources/thuglife/face_regex.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.15)
    background = Image.open(imagePath)
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
    file_name = "masked_img.png"
    ok = sedpath + "/" + file_name
    background.save(ok, "PNG")
    await borg.send_file(event.chat_id, ok)
    await hmm.delete()
    for files in (ok, img, maskPath):
        if files and os.path.exists(files):
            os.remove(files)
            
            
@friday.on(friday_on_cmd(pattern=r"tni"))
@friday.on(sudo_cmd(pattern=r"tni", allow_sudo=True))
async def toony(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    hmmu = await event.edit("`Converting Toonized Image..`")
    await event.get_reply_message()
    img = await convert_to_image(event, borg)
    imagez = cv2.imread(img)
    cartoon_image_style_2 = cv2.stylization(
        imagez, sigma_s=60, sigma_r=0.5
    )  ## Cartoonify process.
    # Save it
    file_name = "Tooned.png"
    ok = sedpath + "/" + file_name
    cv2.imwrite(ok, cartoon_image_style_2)
    # Upload it
    await borg.send_file(event.chat_id, ok)
    await hmmu.delete()
    # Remove all Files
    for files in (ok, img):
        if files and os.path.exists(files):
            os.remove(files)


@friday.on(friday_on_cmd(pattern=r"tig"))
@friday.on(sudo_cmd(pattern=r"tig", allow_sudo=True))
async def lolmetrg(event):
    if event.fwd_from:
        return
    await event.edit("`Triggered This Image`")
    sed = await event.get_reply_message()
    img = await convert_to_image(event, borg)
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/triggered?avatar={imglink}"
    r = requests.get(lolul)
    open("triggered.gif", "wb").write(r.content)
    lolbruh = "triggered.gif"
    await borg.send_file(
        event.chat_id, lolbruh, caption="You got triggered....", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)
            
@friday.on(friday_on_cmd(pattern=r"geyuser"))
@friday.on(sudo_cmd(pattern=r"geyuser", allow_sudo=True))
async def lolmetrg(event):
    if event.fwd_from:
        return
    await event.edit("`Meking This Guy Gey.`")
    sed = await event.get_reply_message()
    img = await convert_to_image(event, borg)
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/gay?avatar={imglink}"
    r = requests.get(lolul)
    open("geys.png", "wb").write(r.content)
    lolbruh = "geys.png"
    await borg.send_file(
        event.chat_id, lolbruh, caption="`You iz Gey.`", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)
            
@friday.on(friday_on_cmd(pattern=r"pix"))
@friday.on(sudo_cmd(pattern=r"pix", allow_sudo=True))
async def lolmetrg(event):
    if event.fwd_from:
        return
    await event.edit("`Pixing This Image.`")
    sed = await event.get_reply_message()
    img = await convert_to_image(event, borg)
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/pixelate?avatar={imglink}"
    r = requests.get(lolul)
    open("pix.png", "wb").write(r.content)
    lolbruh = "pix.png"
    await borg.send_file(
        event.chat_id, lolbruh, caption="`Pixeled This Image.`", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)

@friday.on(friday_on_cmd(pattern=r"ytc"))
@friday.on(sudo_cmd(pattern=r"ytc", allow_sudo=True))
async def lolmetrg(event):
    if event.fwd_from:
        return
    await event.edit("`Making Comment`")
    sed = await event.get_reply_message()
    hmm_s = await event.client(GetFullUserRequest(sed.sender_id))
    if not hmm_s.profile_photo:
        imglink = 'https://telegra.ph/file/b9684cda357dfbe6f5748.jpg'
    elif hmm_s.profile_photo:
        img = await borg.download_media(hmm_s.profile_photo, sedpath)
        url_s = upload_file(img)
        imglink = f"https://telegra.ph{url_s[0]}"
    first_name = html.escape(hmm_s.user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    if sed.text is None:
        comment = 'Give Some Text'
    else:
        comment = sed.raw_text
    lolul = f"https://some-random-api.ml/canvas/youtube-comment?avatar={imglink}&username={first_name}&comment={comment}"
    r = requests.get(lolul)
    open("ytc.png", "wb").write(r.content)
    lolbruh = "ytc.png"
    await event.delete()
    await borg.send_file(
        event.chat_id, lolbruh, caption="`Hmm Nice.`", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)

@friday.on(friday_on_cmd(pattern=r"jail"))
@friday.on(sudo_cmd(pattern=r"jail", allow_sudo=True))
async def hmm(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    hmmu = await event.reply("hmm... Sending him to jail...🚶")
    await event.get_reply_message()
    img = await convert_to_image(event, borg)
    sed = await event.get_reply_message()
    img = await convert_to_image(event, borg)
    mon = "./resources/jail/hmm.png"
    foreground = Image.open(mon).convert("RGBA")
    background = Image.open(img).convert("RGB")
    with Image.open(img) as img:
        width, height = img.size
    fg_resized = foreground.resize((width, height))
    background.paste(fg_resized, box=(0, 0), mask=fg_resized)

    background.save("./starkgangz/testing.png")

    file_name = "testing.png"
    ok = "./starkgangz/" + file_name
    await borg.send_file(event.chat_id, ok)
    await hmmu.delete()
    for files in (ok, img):
        if files and os.path.exists(files):
            os.remove(files)


@friday.on(friday_on_cmd(pattern=r"greyscale"))
@friday.on(sudo_cmd(pattern=r"greyscale", allow_sudo=True))
async def hmm(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    hmmu = await event.edit("hmm.. Creating a black&White image...")
    await event.get_reply_message()
    img = await convert_to_image(event, borg)
    img1 = cv2.imread(img)

    gray_img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    cv2.imwrite("./starkgangz/testing.png", gray_img)
    file_name = "testing.png"
    ok = "./starkgangz/" + file_name
    await borg.send_file(event.chat_id, ok)
    await hmmu.delete()
    for files in (ok, img):
        if files and os.path.exists(files):
            os.remove(files)


# Plugin By - XlayerCharon[XCB]
# TG ~>>//@CharonCB21
# @code-rgb
@friday.on(friday_on_cmd(pattern=r"fgs ?(.*)"))
@friday.on(sudo_cmd(pattern=r"fgs ?(.*)", allow_sudo=True))
async def img(event):
    if event.fwd_from:
        return
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("No input found!")
        return
    if ";" in text:
        search, result = text.split(";", 1)
    else:
        event.edit("Invalid Input! Check help for more info!")
        return
    photo = Image.open("resources/dummy_image/fgs.jpg")
    drawing = ImageDraw.Draw(photo)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    font1 = ImageFont.truetype("Fonts/ProductSans-BoldItalic.ttf", 20)
    font2 = ImageFont.truetype("Fonts/ProductSans-Light.ttf", 23)
    drawing.text((450, 258), result, fill=blue, font=font1)
    drawing.text((270, 37), search, fill=black, font=font2)
    file_name = "fgs.jpg"
    ok = sedpath + "/" + file_name
    photo.save(ok)
    await event.delete()
    await friday.send_file(event.chat_id, ok)
    if os.path.exists(ok):
        os.remove(ok)


@friday.on(friday_on_cmd(pattern=r"lg"))
@friday.on(sudo_cmd(pattern=r"lg", allow_sudo=True))
async def lottiepie(event):
    if event.fwd_from:
        return
    await event.edit("`Prooooooccccesssssssinggggg.....`")
    message = await event.get_reply_message()
    if message.media and message.media.document:
        mime_type = message.media.document.mime_type
        if not "tgsticker" in mime_type:
            await event.edit("Not Supported Yet.")
            return
        await message.download_media("tgs.tgs")
        await runcmd("lottie_convert.py tgs.tgs json.json")
        json = open("json.json", "r")
        jsn = json.read()
        json.close()
        jsn = (
            jsn.replace("[1]", "[2]")
            .replace("[2]", "[3]")
            .replace("[3]", "[4]")
            .replace("[4]", "[5]")
            .replace("[5]", "[6]")
        )
        open("json.json", "w").write(jsn)
        await event.delete()
        await friday.run_cmd(f"lottie_convert.py json.json tgs.tgs")
        await borg.send_file(event.chat_id, file="tgs.tgs", force_document=False)
        os.remove("json.json")
        os.remove("tgs.tgs")


@friday.on(friday_on_cmd(pattern=r"ph ?(.*)"))
@friday.on(sudo_cmd(pattern=r"ph ?(.*)", allow_sudo=True))
async def img(event):
    if event.fwd_from:
        return
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("No input found!  --__--")
        return
    if ":" in text:
        username, texto = text.split(":", 1)
    else:
        event.edit("Invalid Input! Check help for more info!")
        return
    img = Image.open("./resources/pb/pb.jpg")
    d1 = ImageDraw.Draw(img)

    myFont = ImageFont.truetype("./resources/pb/font.TTF", 100)

    d1.text((300, 700), username, font=myFont, fill=(135, 98, 87))

    d1.text((12, 1000), texto, font=myFont, fill=(203, 202, 202))

    img.save("./starkgangz/testpb.jpg")
    file_name = "testpb.jpg"
    ok = "./starkgangz/" + file_name
    await borg.send_file(event.chat_id, ok)
    os.remove(files)
    for files in (ok, img):
        if files and os.path.exists(files):
            os.remove(files)
        event.delete()
        
# Credits To These :
# https://github.com/midnightmadwalk [TG: @MidnightMadwalk]
# https://github.com/code-rgb [TG: @DeletedUser420]
# Ported By  https://github.com/STARKGANG [TG: @STARKXD]


@friday.on(friday_on_cmd(pattern=r"spin ?(.*)"))
@friday.on(sudo_cmd(pattern=r"spin ?(.*)", allow_sudo=True))
async def spinshit(message):
    if message.fwd_from:
        return
    reply = await message.get_reply_message()
    lmaodict = {"1": 1, "2": 3, "3": 6, "4": 12, "5": 24, "6": 60}
    lolshit = message.pattern_match.group(1)
    if not lolshit.isdigit():
        await message.edit("`Only Speed from 1-6 Is Allowded !`")
        return
    if int(lolshit) > 6:
        await message.edit("`Only Speed from 1-6 Is Allowded !`")
        return
    keke = str(lolshit)
    if not reply:
        await message.edit("`Reply To Media First !`")
        return
    else:
        if lolshit:
            step = lmaodict.get(keke)
        else:
            step = 1
    pic_loc = await convert_to_image(message, borg)
    if not pic_loc:
        await message.edit("`Reply to a valid media first.`")
        return
    await message.edit("🌀 `Tighten your seatbelts, sh*t is about to get wild ...`")
    spin_dir = 1
    path = "resources/rotate-disc/"
    if os.path.exists(path):
        rmtree(path, ignore_errors=True)
    os.mkdir(path)
    im = Image.open(pic_loc)
    if im.mode != "RGB":
        im = im.convert("RGB")
    # Rotating pic by given angle and saving
    for k, nums in enumerate(range(1, 360, step), start=0):
        y = im.rotate(nums * spin_dir)
        y.save(os.path.join(path, "spinx%s.jpg" % k))
    output_vid = os.path.join(path, "out.mp4")
    # ;__; Maths lol, y = mx + c
    frate = int(((90 / 59) * step) + (1680 / 59))
    # https://stackoverflow.com/questions/20847674/ffmpeg-libx264-height-not-divisible-by-2
    await friday.run_cmd(
        f'ffmpeg -framerate {frate} -i {path}spinx%d.jpg -c:v libx264 -preset ultrafast -vf "crop=trunc(iw/2)*2:trunc(ih/2)*2" -pix_fmt yuv420p {output_vid}'
    )
    if os.path.exists(output_vid):
        round_vid = os.path.join(path, "out_round.mp4")
        await crop_vid(output_vid, round_vid)
        await borg.send_file(
            message.chat_id, round_vid, video_note=True, reply_to=reply.id
        )
        await message.delete()
    os.remove(pic_loc)
    rmtree(path, ignore_errors=True)



@friday.on(friday_on_cmd(pattern=r"lnews ?(.*)"))
@friday.on(sudo_cmd(pattern=r"lnews ?(.*)", allow_sudo=True))
async def hmm(event):
    if event.fwd_from:
        return
    text = event.pattern_match.group(1)
    if not text:
        await event.reply("No input found!  --__--")
        return
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    hmmu = await event.reply("hmm... Starting Live News Stream...🚶")
    await event.get_reply_message()
    img = await convert_to_image(event, borg)
    sed = await event.get_reply_message()
    img = await convert_to_image(event, borg)
    background = Image.open(img)
    newss = "./resources/live/news.png"
    foreground = Image.open(newss)
    im = background.resize((2800, 1500))
    im.paste(foreground, (0,0), mask = foreground)
    d1 = ImageDraw.Draw(im)
    myFont = ImageFont.truetype("./resources/live/font.ttf", 165)
    d1.text((7, 1251), text, font=myFont, fill =(0, 0, 0))

    im.save("./starkgangz/livenews.png")
    file_name = "livenews.png"
    ok = "./starkgangz/" + file_name
    await borg.send_file(event.chat_id, ok)
    await hmmu.delete()
    for files in (ok, img):
        if files and os.path.exists(files):
            os.remove(files)
            
@friday.on(friday_on_cmd(pattern="(genca|gencertificate) ?(.*)"))
async def holastark2(event):
    if event.fwd_from:
        return
    famous_people = ['Modi', 'Trump', 'Albert', 'Tony-stark', 'Stark-Gang', 'Gandhi']
    await event.edit("`Processing..`")
    text = event.pattern_match.group(2)
    img = Image.open('./resources/CERTIFICATE_TEMPLATE_IMAGE.png')
    d1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('Fonts/impact.ttf', 200)
    myFont2 = ImageFont.truetype('Fonts/impact.ttf', 70)
    myFont3 = ImageFont.truetype('Fonts/Streamster.ttf', 50)
    d1.text((1433, 1345), text, font=myFont, fill=(51, 51, 51))
    TZ = pytz.timezone(Config.TZ)
    datetime_tz = datetime.now(TZ)
    oof = datetime_tz.strftime(f"%Y/%m/%d")
    d1.text((961, 2185), oof, font=myFont2, fill=(51, 51, 51))
    d1.text((2441, 2113), random.choice(famous_people), font=myFont3, fill=(51, 51, 51))
    file_name = "certificate.png"
    await event.delete()
    ok = sedpath + "/" + file_name
    img.save(ok, "PNG")
    await borg.send_file(event.chat_id, ok)
    if os.path.exists(ok):
        os.remove(ok)
        

@friday.on(friday_on_cmd(pattern="(slogo|sl) ?(.*)"))
async def slogo(event):
    if event.fwd_from:
        return
    await event.edit("`Processing..`")
    text = event.pattern_match.group(2)
    img = Image.open('./resources/star/20201125_094030.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "white"
    shadowcolor = "black"
    font = ImageFont.truetype("./resources/star/Chopsic.otf", 380)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= (image_heightz-h)/2
    draw.text((x, y), text, font=font, fill="white", stroke_width=30, stroke_fill="black")
    fname2 = "LogoBy@FRIDAYOT.png"
    img.save(fname2, "png")
    await borg.send_file(event.chat_id, fname2, caption="Made By @FridayOT")
    if os.path.exists(fname2):
            os.remove(fname2)



@friday.on(friday_on_cmd(pattern="(adityalogo|blacklogo) ?(.*)"))
async def yufytf(event):
    if event.fwd_from:
        return
    await event.edit("`Processing..`")
    text = event.pattern_match.group(2)
    img = Image.open('./resources/Blankmeisnub.jpg')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('Fonts/Streamster.ttf', 220)
    image_widthz, image_heightz = img.size
    w,h = draw.textsize(text, font=font)
    h += int(h*0.21)
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 0))
    file_name = "LogoBy@MeisNub.png"
    await event.delete()
    ok = sedpath + "/" + file_name
    img.save(ok, "PNG")
    await borg.send_file(event.chat_id, ok, caption="Made By @FridayOT")
    if os.path.exists(ok):
        os.remove(ok)
    
    
    
@friday.on(friday_on_cmd(pattern="(certificategen|cg) ?(.*)"))
async def holastark(event):
    if event.fwd_from:
        return
    await event.edit("`Processing..`")
    text = event.pattern_match.group(2)
    font_size = 3.6
    font_color = (51, 51, 51)
    coordinate_y_adjustment = -120
    coordinate_x_adjustment = 7
    img = cv2.imread('./resources/CERTIFICATE_TEMPLATE_IMAGE.png')
    font = cv2.FONT_HERSHEY_SIMPLEX
    textsize = cv2.getTextSize(text, font, font_size, 10)[0]
    text_x = (img.shape[1] - textsize[0]) / 2 \
            + coordinate_x_adjustment
    text_y = (img.shape[0] + textsize[1]) / 2 \
            - coordinate_y_adjustment
    text_x = int(text_x)
    text_y = int(text_y)
    cv2.putText(
            img,
            text,
            (text_x, text_y),
            font,
            font_size,
            font_color,
            10,
        )
    file_name = "CertificateGenBy@FridayOt.png"
    ok = sedpath + "/" + file_name
    cv2.imwrite(ok, img)
    await event.delete()
    await borg.send_file(event.chat_id, file=ok, caption="Powered By @FridayOT")
    if os.path.exists(ok):
        os.remove(ok)
    
    
@friday.on(friday_on_cmd(pattern="(flip|blur|tresh|hsv|lab|sketch)"))
async def warnerstark_s(event):
    if event.fwd_from:
        return
    ws = event.pattern_match.group(1)
    img = await convert_to_image(event, borg)
    image = cv2.imread(img)
    await event.edit("`Processing..`")
    if ws == "flip":
        flipped = cv2.flip(image, 0)
        file_name = "Flipped.webp"
        ok = sedpath + "/" + file_name
        cv2.imwrite(ok, flipped)
        warnerstark = "Hehe, Flipped"
    elif ws == "blur":
        blurred = cv2.blur(image, (8,8))
        file_name = "Blurred.webp"
        ok = sedpath + "/" + file_name
        cv2.imwrite(ok, blurred)
        warnerstark = "Hehe, Blurred"
    elif ws == "tresh":
        treshold, fridaydevs = cv2.threshold(image, 150, 225, cv2.THRESH_BINARY)
        file_name = "Tresh.webp"
        ok = sedpath + "/" + file_name
        cv2.imwrite(ok, fridaydevs)
        warnerstark = "Hehe, TreshHolded."
    elif ws == "hsv":
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        file_name = "Hsv.webp"
        ok = sedpath + "/" + file_name
        cv2.imwrite(ok, hsv)
        warnerstark = "Hehe, Hsv"
    elif ws == "lab":
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        file_name = "Lab.webp"
        ok = sedpath + "/" + file_name
        cv2.imwrite(ok, lab)
        warnerstark = "Hehe, Lab"
    elif ws == "sketch":
        scale_percent = 0.60
        width = int(image.shape[1] * scale_percent)
        height = int(image.shape[0] * scale_percent)
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        kernel_sharpening = np.array([[-1, -1, -1],
                              [-1, 9, -1],
                              [-1, -1, -1]])
        sharpened = cv2.filter2D(resized, -1, kernel_sharpening)
        gray = cv2.cvtColor(sharpened, cv2.COLOR_BGR2GRAY)
        inv = 255 - gray
        gauss = cv2.GaussianBlur(inv, ksize=(15, 15), sigmaX=0, sigmaY=0)
        pencil_image = dodgeV2(gray, gauss)
        file_name = "Drawn.webp"
        ok = sedpath + "/" + file_name
        cv2.imwrite(ok, pencil_image)
        warnerstark = "Hehe, Drawn By @FridayOT"
    await event.delete()
    await borg.send_file(event.chat_id, file=ok, caption=warnerstark)
    for files in (ok, img):
        if files and os.path.exists(files):
            os.remove(files)
     
@friday.on(friday_on_cmd(pattern="aic$"))
async def warnerstarkgang(event):
    if event.fwd_from:
        return
    img = await convert_to_image(event, borg)
    await event.edit("`Coverting This Media To Image Now.`")
    so = "**Powered By @FridayOT**"
    await event.delete()
    await borg.send_file(event.chat_id, file=img, caption=so)
    os.remove(img)
    
@friday.on(friday_on_cmd(pattern="compressimage(?: |$)(.*)"))
async def asscompress(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("Reply To Image To Compress It")
        return
    sed = await event.get_reply_message()
    if not sed.photo:
        await event.edit("This Only Works On Images")
        return
    sedq = int(event.pattern_match.group(1)) if event.pattern_match.group(1) else 75
    image_path = await friday.download_media(sed.media)
    im = Image.open(image_path)
    ok = "CompressedBy@FridayOt.png"
    im.save(ok, optimize=True, quality=sedq)
    await event.edit("`Compressing This Image.`")
    so = "**Powered By @FridayOT**"
    await event.delete()
    await borg.send_file(event.chat_id, file=ok, caption=so)
    for files in (ok, image_path):
        if files and os.path.exists(files):
            os.remove(files)
    
    
@friday.on(friday_on_cmd(pattern="cimage ?(.*)"))
@friday.on(sudo_cmd(pattern="cimage ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Oh Wait Let Me Get Wear Glasses")
    if not event.reply_to_msg_id:
        ommhg = await friday.edit_or_reply(event, "Reply To Any Image.")
        return
    reply_message = await event.get_reply_message()
    ommhg = await friday.edit_or_reply(event, "Processing. please wait.")
    img = await convert_to_image(event, borg)
    image = open(img, 'rb')
    url_s = upload_file(image)
    link = f"https://telegra.ph{url_s[0]}"
    c = {
      "Type":"CaptionRequest",
      "Content":link
    }
    h = {
      "Content-Type":"application/json"
    }
    r = requests.post("https://captionbot.azurewebsites.net/api/messages", headers = h, json = c)
    endard = r.text.replace('"', "")
    await ommhg.edit(endard)
    if os.path.exists(img):
        os.remove(img)
    
@friday.on(friday_on_cmd(pattern="speedup$"))
async def fasty(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("Reply To Any Video.")
        return
    await event.edit("Ah, Shit. Here it Starts.")
    kk = await event.get_reply_message()
    if not kk.video or kk.video_note:
        await event.edit("`Oho, Reply To Video Only`")
        return
    hmm = await event.client.download_media(kk.media)
    c_time = time.time()
    cmd = f'ffmpeg -i {hmm} -vf  "setpts=0.25*PTS" FastMotionBy@FridayOT.mp4'
    await friday.run_cmd(cmd)
    filem = "FastMotionBy@FridayOT.mp4"
    if not os.path.exists(filem):
        await event.edit("**Process, Failed !**")
        return
    final_file = await uf(
            file_name=filem,
            client=bot,
            file=open(filem, 'rb'),
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, event, c_time, "Uploading Fast Motion video..", filem
                )
            ),
        )
    await event.delete()
    await borg.send_file(
        event.chat_id,
        final_file,
        caption="**Fast Motion** - Powered By @FridayOT")
    for files in (filem, hmm):
        if files and os.path.exists(files):
            os.remove(files)
            
@friday.on(friday_on_cmd(pattern="slowdown$"))
async def fasty(event):
    if event.fwd_from:
        return
    await event.edit("Ah, Shit. Here it Starts.")
    if not event.reply_to_msg_id:
        await event.edit("Reply To Any Video.")
        return
    kk = await event.get_reply_message()
    if not kk.video or kk.video_note:
        await event.edit("`Oho, Reply To Video Only`")
        return
    hmm = await event.client.download_media(kk.media)
    c_time = time.time()
    cmd = f'ffmpeg -i {hmm} -vf  "setpts=4*PTS" SlowMotionBy@FridayOT.mp4'
    await friday.run_cmd(cmd)
    filem = "SlowMotionBy@FridayOT.mp4"
    if not os.path.exists(filem):
        await event.edit("**Process, Failed !**")
        return
    final_file = await uf(
            file_name=filem,
            client=bot,
            file=open(filem, 'rb'),
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, event, c_time, "Uploading Slow Motion Video..", filem
                )
            ),
        )
    await borg.send_file(
        event.chat_id,
        final_file,
        caption="**Slow Motion** - Powered By @FridayOT")
    await event.delete()
    for files in (filem, hmm):
        if files and os.path.exists(files):
            os.remove(files)
    
@friday.on(friday_on_cmd(pattern="vidflip$"))
async def flip(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("Reply To Any Video.")
        return
    await event.edit("Ah, Shit. Here it Starts.")
    kk = await event.get_reply_message()
    if not kk.video or kk.video_note:
        await event.edit("`Oho, Reply To Video Only`")
        return
    hmm = await event.client.download_media(kk.media)
    c_time = time.time()
    cmd = f'ffmpeg -i {hmm} -vf "transpose=2,transpose=2" FlipedBy@FridayOT.mp4'
    await friday.run_cmd(cmd)
    filem = "FlipedBy@FridayOT.mp4"
    if not os.path.exists(filem):
        await event.edit("**Process, Failed !**")
        return
    final_file = await uf(
            file_name=filem,
            client=bot,
            file=open(filem, 'rb'),
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, event, c_time, "Uploading Flipped video..", filem
                )
            ),
        )
    await event.delete()
    await borg.send_file(
        event.chat_id,
        final_file,
        caption="**Video Flipped** - Powered By @FridayOT")
    for files in (filem, hmm):
        if files and os.path.exists(files):
            os.remove(files)
            
@friday.on(friday_on_cmd(pattern="extractaudio$"))
async def audio_extract(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("Reply To Any Video.")
        return
    await event.edit("Ah, Shit. Here it Starts.")
    kk = await event.get_reply_message()
    if not kk.video or kk.video_note:
        await event.edit("`Oho, Reply To Video Only`")
        return
    hmm = await event.client.download_media(kk.media)
    try:
        thumb = await event.client.download_media(kk.media, thumb=-1)
    except:
        thumb = "./resources/IMG_20200929_103719_628.jpg"
    name_out = str(os.path.basename(hmm)).split(".")[0] + str(".mp3")
    c_time = time.time()
    cmd = f"ffmpeg -i {hmm} -map 0:a {name_out}"
    await friday.run_cmd(cmd)
    filem = name_out
    if not os.path.exists(filem):
        await event.edit("**Process, Failed !**")
        return
    final_file = await uf(
            file_name=filem,
            client=bot,
            file=open(filem, 'rb'),
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, event, c_time, "Uploading Audio From The video..", filem
                )
            ),
        )
    await event.delete()
    await borg.send_file(
        event.chat_id,
        final_file,
        thumb=thumb,
        caption="**Audio Extarcted** - Powered By @FridayOT")
    for files in (filem, hmm):
        if files and os.path.exists(files):
            os.remove(files)
            
@friday.on(friday_on_cmd(pattern="(videonote|convertvideonote)$"))
async def convert_to_note(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("Reply To Any Video.")
        return
    await event.edit("Ah, Shit. Here it Starts.")
    kk = await event.get_reply_message()
    if not (kk.video or kk.video_note or kk.gif or kk.video_note):
        await event.edit("`Oho, Reply To Video Only.`")
        return
    hmm = await event.client.download_media(kk.media)
    try:
        thumb = await event.client.download_media(kk.media, thumb=-1)
    except:
        thumb = "./resources/IMG_20200929_103719_628.jpg"
    c_time = time.time()
    filem = "ConvertedBy@FridayOT.mp4"
    await crop_vid(hmm, filem)
    if not os.path.exists(filem):
        await event.edit("**Process, Failed !**")
        return
    final_file = await uf(
            file_name=filem,
            client=bot,
            file=open(filem, 'rb'),
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, event, c_time, "Uploading Round / Video Note.", filem
                )
            ),
        )
    await event.delete()
    await borg.send_file(
        event.chat_id,
        final_file,
        thumb=thumb, 
        video_note=True)
    for files in (filem, hmm):
        if files and os.path.exists(files):
            os.remove(files)
        
def dodgeV2(image, mask):
    return cv2.divide(image, 255 - mask, scale=256)

@friday.on(friday_on_cmd(pattern="memify (.*)"))
async def starkmeme(event):
    if event.fwd_from:
        return
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
        imgpath = sedpath + "/" + "memeimg.webp"
        await borg.send_file(event.chat_id, imgpath)
        if os.path.exists(imgpath):
            os.remove(imgpath)
        await mryeast.delete()
    else:
        top_text = hmm
        bottom_text = ""
        generate_meme(seds, top_text=top_text, bottom_text=bottom_text)
        imgpath = sedpath + "/" + "memeimg.webp"
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
    file_name = "memeimg.webp"
    ok = sedpath + "/" + file_name
    im.save(ok, "WebP")
    
@friday.on(friday_on_cmd(pattern=r"glitch"))
@friday.on(sudo_cmd(pattern=r"glitch", allow_sudo=True))
async def glitch(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Are You on Weed? Please Reply To Image`")
        return
    sed = await event.get_reply_message()
    okbruh = await event.edit("`Gli, Glitchiiingggg.....`")
    photolove = await convert_to_image(event, friday)
    pathsn = f"./starkgangz/@fridayot.gif"
    await event.edit("Glitching Image :/")
    glitch_imgs = glitcher.glitch_image(photolove, 2, gif=True, color_offset=True)
    glitch_imgs[0].save(
        pathsn,
        format="GIF",
        append_images=glitch_imgs[1:],
        save_all=True,
        duration=DURATION,
        loop=LOOP,
    )
    c_time = time.time()
    await event.edit("Optimizing Now")
    optimize(pathsn)
    await event.edit("Starting Upload")
    stark_m = await uf(
        	file_name="Glitched@FridayOt.gif",
            client=borg,
            file=open(pathsn, 'rb'),
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, event, c_time, "Uploading..", pathsn
                )
            ),
        )
    await borg.send_file(event.chat_id,
                         stark_m,
                         caption="Powered By @FridayOT")
    await okbruh.delete()
    for starky in (pathsn, photolove):
        if starky and os.path.exists(starky):
            os.remove(starky)

    
CMD_HELP.update(
    {
        "imagetools": "**imagetools**\
        \n\n**Syntax : **`.cit`\
        \n**Usage :** colourizes the given picture.\
        \n\n**Syntax : **`.nst`\
        \n**Usage :** removes colours from image.\
        \n\n**Syntax : **`.tni`\
        \n**Usage :** Toonify the image.\
        \n\n**Syntax : ** `.thug`\
        \n**Usage :** makes a thug life meme image.\
        \n\n**Syntax : ** `.tig`\
        \n**Usage :** Makes a triggered gif of the replied image.\
        \n\n**Syntax : ** `.spin <number between 1-6>`\
        \n**Usage :** Spins The Given Image.\
        \n\n**Syntax : ** `.jail`\
        \n**Usage :** Makes a jail image of the replied image.\
        \n\n**Syntax : ** `.fgs searchtext;fake text`\
        \n**Usage :** Makes a Fake Google Search Image.\
        \n\n**Syntax : ** `.ph username:fake text`\
        \n**Usage :** Makes a Fake PornHub comment with given username and text.\
        \n\n**Syntax : ** `.greyscale`\
        \n**Usage :** Makes a black and white image of the replied image.\
        \n\n**Syntax : **`.nsfw <replying to the image>`\
        \n**Usage :** Identifies If The Given Image Is Nsfw Or Not.\
        \n\n**Syntax : **`.picgen`\
        \n**Usage :** Genetates Fake Image.\
        \n\n**Note : **The Person In Picture Really Doesn't Exist.\
        \n\n**Syntax : ** `.lnews <text>`\
        \n**Usage :** Makes a Fake News Streaming With Replyed Image And Text."
    }
)
