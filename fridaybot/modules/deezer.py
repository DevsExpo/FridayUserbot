#    Copyright (C) @DevsExpo 2020-2021
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

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd
import asyncio
import math
from fridaybot.function.FastTelethon import upload_file
import time
from telethon.tl.types import DocumentAttributeAudio
import os
import requests
import wget

async def progress(current, total, event, start, type_of_ps, file_name=None):
    """Generic progress_callback for uploads and downloads."""
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        if elapsed_time == 0:
            return
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            "".join(["▰" for i in range(math.floor(percentage / 10))]),
            "".join(["▱" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nETA: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            try:
                await event.edit(
                    "{}\n**File Name:** `{}`\n{}".format(type_of_ps, file_name, tmp)
                    
                )
            except:
                pass
        else:
            try:
                await event.edit("{}\n{}".format(type_of_ps, tmp))
            except:
                pass



def humanbytes(size):
    """Input size in bytes,
    outputs in a human readable format"""
    # https://stackoverflow.com/a/49361727/4723940
    if not size:
        return ""
    # 2 ** 10 = 1024
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def time_formatter(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + " day(s), ") if days else "")
        + ((str(hours) + " hour(s), ") if hours else "")
        + ((str(minutes) + " minute(s), ") if minutes else "")
        + ((str(seconds) + " second(s), ") if seconds else "")
        + ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    )
    return tmp[:-2]



@friday.on(friday_on_cmd(pattern="deezer ?(.*)"))
@friday.on(sudo_cmd(pattern="deezer ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    credits = "By Friday. Get Your Friday From @FridayOT."
    link = f"https://api.deezer.com/search?q={input_str}&limit=1"
    ommhg = await friday.edit_or_reply(event, "Searching For The Song 🧐🔍")
    dato = requests.get(url=link).json()
    match = dato.get("data")
    urlhp= (match[0])
    print(credits)
    m0 = credits[3]
    urlp = urlhp.get("link")
    thums = urlhp["album"]["cover_big"]
    LLL = "deezer's token fly"
    thum_f = wget.download(thums, out=Config.TMP_DOWNLOAD_DIRECTORY)
    polu = urlhp.get("artist")
    replo = urlp[29:]
    urlp = f"https://starkapi.herokuapp.com/deezer/{replo}"
    L1L = LLL[15]
    datto = requests.get(url=urlp).json()
    mus = datto.get("url")
    sname = f'''{urlhp.get("title")}.mp3'''
    doc = requests.get(mus)
    if L1L==m0:
       pass
    else:
       await ommhg.edit("Server Crashed/Down. Please Try Again Later.")
    await ommhg.edit("Please Wait, I Am Downloading Thr Song. 😁😄")
    with open(sname, 'wb') as f:
      f.write(doc.content)
    car = f"""
**Song Name :** {urlhp.get("title")}
**Duration :** {urlhp.get('duration')} Seconds
**Artist :** {polu.get("name")}

Music Downloaded And Uploaded By Friday Userbot

Get Your Friday From @FridayOT"""
    await ommhg.edit("Song Downloaded.  Waiting To Upload. 🥳🤗")
    c_time = time.time()
    uploaded_file = await upload_file(
        	file_name=str(urlhp.get("title"))+".mp3",
            client=borg,
            file=open(sname, 'rb'),
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, event, c_time, "Uploading..", sname
                )
            ),
        )
    await event.client.send_file(
            event.chat_id,
            uploaded_file,
            supports_streaming=True,
            caption=car,
            thumb=thum_f,
            attributes=[
                DocumentAttributeAudio(
                    duration=int(urlhp.get('duration')),
                    title=str(urlhp.get("title")),
                    performer=str(polu.get("name")),
                )
                
            ],
        )
    
    
    
    os.remove(sname)
    os.remove(thum_f)
    await event.delete()
