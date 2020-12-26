#    Copyright (C) @chsaiujwal 2020
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
import re
import sys
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve
from uniborg.util import friday_on_cmd
from fridaybot import CMD_HELP
from fridaybot.utils import admin_cmd

@friday.on(admin_cmd(pattern="book (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    lool = 0
    await event.edit("searching for the book...")
    lin = "https://b-ok.cc/s/"
    text = input_str
    link = lin+text

    headers = ['User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0']
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    f = open("book.txt",'w')
    total = soup.find(class_="totalCounter")
    for nb in total.descendants:
      nbx = nb.replace("(", "").replace(")", "")
    if nbx == "0":
        await event.edit("No Books Found with that name.")
    else:

        for tr in soup.find_all('td'):
            for td in tr.find_all('h3'):
                for ts in td.find_all('a'):
                    title = ts.get_text()
                    lool = lool+1
                for ts in td.find_all('a', attrs={'href': re.compile("^/book/")}):
                    ref = (ts.get('href'))
                    link = "https://b-ok.cc" + ref

                f.write("\n"+title)
                f.write("\nBook link:- " + link+"\n\n")

        f.write("By Friday.")
        f.close()
        caption="By Friday.\n Get Your Friday From @FRIDAYCHAT"
        
        await borg.send_file(event.chat_id, "book.txt", caption=f"**BOOKS GATHERED SUCCESSFULLY!\n\nBY FRIDAY. GET YOUR OWN FRIDAY FROM @FRIDAYCHAT.**")
        os.remove("book.txt")
        await event.delete()
        


CMD_HELP.update(
    {
        "booksdl": "**Books Scraper**\
\n\n**Syntax : **`.book <book name>`\
\n**Usage :** Gets Instant Download Link Of Given Book."
    }
)
