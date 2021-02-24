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

import tracemoepy
import os
import glob
import asyncio
import math
import os
import time
from telethon.tl.types import DocumentAttributeAudio
from fridaybot.function import progress, humanbytes, time_formatter, convert_to_image
from fridaybot.function.FastTelethon import upload_file

@friday.on(friday_on_cmd(pattern="anp$"))
async def anime_name(event):
    tracemoe = tracemoepy.tracemoe.TraceMoe()
    file_s = await convert_to_image(event, friday)
    c_time = time.time()
    await event.edit("`Searching For This Anime. Bruh.`")
    try:
      st = tracemoe.search(file_s, encode=True)
    except:
      await event.edit("`SomeThing is Sad, Failed.`")
      return
    video = tracemoe.natural_preview(st)
    with open('preview@FridayOT.mp4', 'wb') as f:
      f.write(video)
    # Hmm Stolen From Userge
    # Anime Reverse Search Powered by tracemoepy.
    # TraceMoePy (GitHub: https://github.com/DragSama/tracemoepy)
    # (C) Author: Phyco-Ninja (https://github.com/Phyco-Ninja) (@PhycoNinja13b)
    ws = st['docs'][0]
    caption = (f"**Title**: **{ws['title_english']}**\n"
                   f"   🇯🇵 (`{ws['title_romaji']} - {ws['title_native']}`)\n"
                   f"\n**Anilist ID:** `{ws['anilist_id']}`"
                   f"\n**Similarity**: `{ws['similarity']*100}`"
                   f"\n**Episode**: `{ws['episode']}")
    starkfile = 'preview@FridayOT.mp4'
    warner = await upload_file(
            file_name=f"{st.docs[0].title}.mp4",
            client=borg,
            file=open(starkfile, 'rb'),
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, event, c_time, "Uploading Your Preview!", starkfile
                )
            ),
        )
    await event.delete()
    await friday.send_file(event.chat_id,
      warner,
      caption=caption
      )
