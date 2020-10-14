import asyncio
import os
import shutil
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions

FONT_FILE_TO_USE = "Fonts/digital.ttf"


@command(pattern="^.autopic", outgoing=True)
async def autopic(event):
    downloaded_file_name = "userbot/original_pic.png"
    downloader = SmartDL(
        Var.DOWNLOAD_PFP_URL_CLOCK, downloaded_file_name, progress_bar=False
    )
    downloader.start(blocking=False)
    photo = "userbot/photo_pfp.png"
    while not downloader.isFinished():
        pass
    counter = -30
    while True:
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        file_test = im.rotate(counter, expand=False).save(photo, "PNG")
        current_time = datetime.now().strftime("Let's Time Travel %H:%M ")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        drawn_text.text((95, 250), current_time, font=fnt, fill=(255, 255, 255))
        img.save(photo)
        file = await bot.upload_file(photo)  # pylint:disable=E0602
        try:
            await bot(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            os.remove(photo)
            counter -= 30
            await asyncio.sleep(60)
        except BaseException:
            return
