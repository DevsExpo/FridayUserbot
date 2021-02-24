import os
import shutil
from re import findall
from fridaybot import CMD_HELP
from fridaybot.function.gmdl import googleimagesdownload
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd
import io
import os
import re
import os
import requests
from fridaybot import CMD_HELP
from fridaybot.function import convert_to_image
from fridaybot.utils import friday_on_cmd, sudo_cmd
import json
import requests
import urllib
import shutil
from re import findall
import requests
from bs4 import BeautifulSoup
from PIL import Image
from fridaybot.function.gmdl import googleimagesdownload
from fridaybot import CMD_HELP
from fridaybot.utils import errors_handler, register, friday_on_cmd

opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36"
opener.addheaders = [("User-agent", useragent)]

sedpath = "./yandex/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)
    
# Copyright (C) 2019 The Raphielscape Company LLC.
# Thanks to @kandnub, for this awesome module !!
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.

@friday.on(friday_on_cmd(pattern=r"reverse(?: |$)(\d*)"))
async def okgoogle(img):
    if img.fwd_from:
        return
    """ For .reverse command, Google search images and stickers. """
    if os.path.isfile("okgoogle.png"):
        os.remove("okgoogle.png")
    event = img
    message = await img.get_reply_message()
    if message and message.media:
        photo = io.BytesIO()
        await bot.download_media(message, photo)
    else:
        await img.edit("`Reply to photo or sticker nigger.`")
        return

    if photo:
        await img.edit("`Processing...`")
        try:
            image = Image.open(photo)
        except OSError:
            await img.edit("`Unsupported sexuality, most likely.`")
            return
        name = "okgoogle.png"
        image.save(name, "PNG")
        image.close()
        searchUrl = "https://www.google.com/searchbyimage/upload"
        multipart = {"encoded_image": (name, open(name, "rb")), "image_content": ""}
        response = requests.post(searchUrl, files=multipart, allow_redirects=False)
        fetchUrl = response.headers["Location"]
        if response != 400:
            await img.edit(
                "`Image successfully uploaded to Google. Maybe.`"
                "\n`Parsing source now. Maybe.`"
            )
        else:
            await img.edit("`Google told me to fuck off.`")
            return

        os.remove(name)
        match = await ParseSauce(fetchUrl + "&preferences?hl=en&fg=1#languages")
        guess = match["best_guess"]
        imgspage = match["similar_images"]

        if guess and imgspage:
            await img.edit(f"[{guess}]({fetchUrl})\n\n`Looking for this Image...`")
        else:
            await img.edit("`Can't find this piece of shit.`")
            return
        lim = findall(r"lim=\d+", guess)
        try:
            lim = lim[0]
            lim = lim.replace("lim=", "")
            guess = guess.replace("lim=" + lim[0], "")
        except IndexError:
            lim = 5
        response = googleimagesdownload()
        logger.info(guess)
        arguments = {
            "keywords": guess,
            "silent_mode": True,
            "limit": lim,
            "format": "jpg",
            "no_directory": "no_directory",
        }
        paths = response.download(arguments)
        lst = paths[0][guess]
        await event.edit(f"[{guess}]({fetchUrl})\n\n[Visually similar images]({imgspage})")
        await event.client.send_file(
            await event.client.get_input_entity(event.chat_id), lst
        )
        shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))


async def ParseSauce(googleurl):
    """Parse/Scrape the HTML code for the info we want."""

    source = opener.open(googleurl).read()
    soup = BeautifulSoup(source, "html.parser")

    results = {"similar_images": "", "best_guess": ""}

    try:
        for similar_image in soup.findAll("input", {"class": "gLFyf"}):
            url = "https://www.google.com/search?tbm=isch&q=" + urllib.parse.quote_plus(
                similar_image.get("value")
            )
            results["similar_images"] = url
    except BaseException:
        pass

    for best_guess in soup.findAll("div", attrs={"class": "r5a77d"}):
        results["best_guess"] = best_guess.get_text()

    return results

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

@friday.on(friday_on_cmd(pattern=r"yandex"))
@friday.on(sudo_cmd(pattern=r"yandex", allow_sudo=True))
async def hmm(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    hmmu = await event.reply("hmm... Reverse Searching The Image On Yandex...🚶")
    sed = await event.get_reply_message()
    img = await convert_to_image(event, borg)
    filePath = img
    searchUrl = 'https://yandex.ru/images/search'
    files = {'upfile': ('blob', open(filePath, 'rb'), 'image/jpeg')}
    params = {'rpt': 'imageview', 'format': 'json', 'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
    response = requests.post(searchUrl, params=params, files=files)
    query_string = json.loads(response.content)['blocks'][0]['params']['url']
    img_search_url= searchUrl + '?' + query_string
    caption = f"""<b>Reverse Search Conpleted!</b>
Reverse Searched Link:- {img_search_url}
Note:- Yandex is a Russian search engine, so better open link in chrome with auto-translate.
Another Note:- Don't Use This Command continually, Yandex Will Block Your Request.
<u><b>Reverse Search Completed By Friday.
Get Your Own Friday From @FRIDAYCHAT.</b></u>
"""
    await borg.send_message(
        event.chat_id,
        caption,
        parse_mode="HTML",
    )
    await event.delete()
    
@friday.on(friday_on_cmd(pattern="(img|image|googleimage|gi) ?(.*)"))
@friday.on(sudo_cmd(pattern="(img|image|googleimage|gi) ?(.*)", allow_sudo=True))
async def img_sampler(event):
    await friday.edit_or_reply(event, "`Processing...`")
    reply = await event.get_reply_message()
    if event.pattern_match.group(2):
        query = event.pattern_match.group(2)
    elif reply:
        query = reply.message
    else:
        await friday.edit_or_reply(
            event, "`um, mind mentioning what I actually need to search for ;_;`"
        )
        return

    lim = findall(r"lim=\d+", query)
    try:
        lim = lim[0]
        lim = lim.replace("lim=", "")
        query = query.replace("lim=" + lim[0], "")
    except IndexError:
        lim = 5
    response = googleimagesdownload()
    arguments = {
        "keywords": query,
        "limit": lim,
        "format": "jpg",
        "silent_mode": True,
        "no_directory": "no_directory",
    }
    paths = response.download(arguments)
    lst = paths[0][query]
    await event.client.send_file(
        await event.client.get_input_entity(event.chat_id), lst
    )
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    await event.delete()


CMD_HELP.update(
    {
        "img": "**Img**\
\n\n**Syntax : **`.img <query>`\
\n**Usage :** get images just with a query"
    }
)
    
CMD_HELP.update(
    {
        "yandex_reverse_img": "**Yandex Reverse Image search**\
\n\n**Syntax : **`.yandex <reply to image>`\
\n**Usage :** Reverse Searches The Image on yandex."
    }
)    

CMD_HELP.update(
    {
        "reverse": ".reverse\
        \nUsage: Reply to a pic/sticker to revers-search it on Google Images !!"
    }
)
