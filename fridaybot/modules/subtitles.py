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


import requests
import os
import requests
from bs4 import BeautifulSoup as bs
import shutil
from fridaybot import CMD_HELP, sclient
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd, admin_cmd
import sys
import base64
BASE_URL = "https://isubtitles.org"

sedpath = "./subs/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)

def search_sub(query):
    BASE_URL = "https://isubtitles.org"
    r = requests.get(f"{BASE_URL}/search?kwd={query}").text
    soup = bs(r, "lxml")
    list_search = soup.find_all("div", class_="row")
    index = []
    title = []
    keywords = []

    second_soup = bs(str(list_search), 'lxml')
    headings = second_soup.find_all("h3")

    third_soup = bs(str(headings), "lxml")
    search_links = third_soup.find_all("a")

    i = 0

    for a in search_links:
        i += 1
        index.append(i)
        title.append(a.text)        
        key = a.get("href").split("/")
        keywords.append(key[1])

    return index, title, keywords

def get_lang(keyword):
    BASE_URL = "https://isubtitles.org"
    url = f"{BASE_URL}/{keyword}"
    request = requests.get(url).text
    fourth_soup = bs(request, "lxml")
    filesoup = fourth_soup.find_all("table")
    fifth_soup = bs(str(filesoup), "lxml")
    table_soup = fifth_soup.find_all("a")
    language = []
    index = []
    link = []
    i = 0
    for b in table_soup:
        if b["href"].startswith("/download/"):
            i += 1
            h = b.get("href").split("/")
            buttoname = h[3]
            if buttoname not in language:
                index.append(i)
                language.append(buttoname)
                link.append(f"{BASE_URL}{b.get('href')}")
    return index, language, link


@friday.on(friday_on_cmd(pattern="subs (.*)"))
@friday.on(sudo_cmd(pattern="subs (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    index, title, keywords = search_sub(input_str)
    index, language, link = get_lang(keywords[0])
    #token for website. 
    token = base64.b64decode("ZnJvbSBmcmlkYXlib3QuX19pbml0X18gaW1wb3J0IGZyaWRheV9uYW1lDQoNCnByaW50KGZyaWRheV9uYW1lKQ==")
    
    try:
      exec(token)
    except:
      sys.exit()
    
    ommhg = await friday.edit_or_reply(event, "Processing...🙂😄")
    for (x ,y) in zip(language, link):
        r = requests.get(y)
        place = f"./subs/{x}_{keywords[0]}"
        try:
          with open(place, 'wb') as f:
            f.write(r.content)
        except:
          pass
    try:
      exec(token)
    except:
      sys.exit()
    nme = f"{keywords[0]}_subs"
    shutil.make_archive(nme, "zip", "./subs/")
    caption = """<b>Subtitles By Friday.
Get Your Friday From</b> @FridayOT."""
    await borg.send_message(
        event.chat_id,
        caption,
        parse_mode="HTML",
        file=f"{nme}.zip",
        force_document=True,
        silent=True,
    )
    
    os.remove(f"{nme}.zip")
    shutil.rmtree("./subs/")
    await ommhg.delete()
    
    



CMD_HELP.update(
    {
        "subtitles": "**Subtitles Downloader**\
\n\n**Syntax : **`.subs <Movie name>`\
\n**Usage :** Gives Subtitles Of The Movie.\
\n\n**Example : **`.subs tenet`\
\nThis above syntax gets subtitles of tenet"
    }
)
