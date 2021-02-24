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

import asyncio
import time
import time as t
import zipfile
from datetime import datetime
import shutil
from fridaybot import CMD_HELP
from fridaybot.function import convert_to_image, crop_vid, runcmd
from fridaybot.utils import friday_on_cmd, sudo_cmd
import shutil
import os
import uuid
import img2pdf
from fridaybot.utils import friday_on_cmd
from telethon.tl.types import InputMessagesFilterPhotos

if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
  os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
  
@friday.on(friday_on_cmd(pattern=r"ci2pdf(?: |$)(.*)"))
async def heck(event):
    if event.fwd_from:
        return  
    un = event.pattern_match.group(1)
    rndm = uuid.uuid4().hex
    dir = f"./{rndm}/"
    media_count = 0
    text_count = 0
    os.makedirs(dir)
    if un:
        chnnl = un
    else:
        chnnl = event.chat_id
    await event.edit(f"**Fetching All Images From This Channel**")
    try:
        chnnl_msgs = await borg.get_messages(chnnl, limit=3000, filter=InputMessagesFilterPhotos)
    except:
        await event.edit("**Unable To fetch Messages !** \n`Please, Check Channel Details And IF There Are Any Images :/`")
        return
    total = int(chnnl_msgs.total)
    await event.edit(f"**Downloading {total} Images**")
    for d in chnnl_msgs:
        media_count += 1
        await borg.download_media(d.media, dir)
    images_path = []
    images_names = os.listdir(dir)
    for i in images_names:
        path = os.path.join(dir, i)
        images_path.append(path)
    with open('imagetopdf@fridayot.pdf', "wb") as f:
        f.write(img2pdf.convert(images_path))    
    await event.delete()    
    await borg.send_file(event.chat_id, "imagetopdf@fridayot.pdf", caption="Powered By @FridayOT")  
    os.remove("imagetopdf@fridayot.pdf")
    shutil.rmtree(dir)
    
    
@friday.on(friday_on_cmd(pattern=r"pdf2docx"))
async def hmm(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("Reply to any Pdf File.")
        return
    hmmu = await event.edit("hmm... Please Wait...🚶")
    lol = await event.get_reply_message()
    starky = await borg.download_media(lol.media, Config.TMP_DOWNLOAD_DIRECTORY)
    hmmu = await event.edit("hmm... Please Wait..")
    pdf_file = starky
    docx_file = './fridaybot/DOWNLOADS/FRIDAYOT.docx'
    parse(pdf_file, docx_file, start=0, end=None)
    await borg.send_file(
        event.chat_id, docx_file, caption=f"*PDF Converted Into Docx by Friday bot. Get your Friday From @FRIDAYOT."
    )
    os.remove(pdf_file)
    os.remove(docx_file)
    await event.delete()
    


CMD_HELP.update(
    {
        "fileTools": "**File Tools**\
\n\n**Syntax : **`.pdf2docx <reply to pdf>`\
\n**Usage :** Converts Given Pdf Into Docx.\
\n\n**Syntax : **`.p2dcl <channel username>`\
\n**Usage :** Converts All The Pdf's From Channel Into Docx."
    }
)
