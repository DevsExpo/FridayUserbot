#    Copyright (C) Midhun KM 2020-2021
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

import shutil
import os
import uuid
from fridaybot.utils import friday_on_cmd
from fridaybot import CMD_HELP

@friday.on(friday_on_cmd(pattern="chnnlzip(?: |$)(.*)"))
async def starky(event):
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
    await event.edit(f"**Fetching All Files From This Channel**")
    try:
        chnnl_msgs = await borg.get_messages(chnnl, limit=3000)
    except:
        await event.edit("**Unable To fetch Messages !** \n`Please, Check Channel Details And IF THere Are Any Media :/`")
        return
    total = int(chnnl_msgs.total)
    await event.edit(f"**Downloading {total} Media/Messages**")
    for d in chnnl_msgs:
        if d.media:
            media_count += 1
            await borg.download_media(d.media, dir)
        if d.text:
            text_count += 1
            f = open(f"{dir}{chnnl}.txt", "a")
            f.write(f"{d.raw_text} \n\n")
    await event.edit(f"**Total Media :** `{total}` \n**Downloaded Media :** `{media_count}` \n**Total Texts Appended :** `{text_count}` \n**Now Zipping Files.**")
    shutil.make_archive(f"{chnnl}", "zip", dir)
    tf = await event.edit(f"**Total Media :** `{total}` \n**Downloaded Media :** `{media_count}` \n**Total Texts Appended :** `{text_count}` \n**Uploading Zip**")
    await borg.send_file(event.chat_id, f"{chnnl}.zip", caption=f"**Total Media :** `{total}` \n**Downloaded Media :** `{media_count}` \n**Total Texts Appended :** `{text_count}`")
    await tf.delete()
    os.remove(f"{chnnl}.zip")
    shutil.rmtree(dir)
            



CMD_HELP.update(
    {
        "channel_zipper": "**Channel Zipper**\
\n\n**Syntax : **`.chnnlzip <channel username>`\
\n**Usage :** Zips All The Files/images/messages in the channel."
    }
)
