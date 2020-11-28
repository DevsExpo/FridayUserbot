# CɪᴘʜᴇʀX
# Credit by @hackintush
import os
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from userbot.utils import friday_on_cmd


@friday.on(friday_on_cmd(pattern="ota"))
async def _(event):
    if event.fwd_from:
        return
    datetime.now()
    BASE_URL = "http://www.google.com"
    if event.reply_to_msg_id:
        await event.edit("Processing...")
        previous_message = await event.get_reply_message()
        previous_message_text = previous_message.message
        if previous_message.media:
            downloaded_file_name = await borg.download_media(
                previous_message, Config.TMP_DOWNLOAD_DIRECTORY
            )
            SEARCH_URL = "{}/searchbyimage/upload".format(BASE_URL)
            multipart = {
                "encoded_image": (
                    downloaded_file_name,
                    open(downloaded_file_name, "rb"),
                ),
                "image_content": "",
            }
            google_rs_response = requests.post(
                SEARCH_URL, files=multipart, allow_redirects=False
            )
            the_location = google_rs_response.headers.get("Location")
            os.remove(downloaded_file_name)
        else:
            previous_message_text = previous_message.message
            SEARCH_URL = "{}/searchbyimage?image_url={}"
            request_url = SEARCH_URL.format(BASE_URL, previous_message_text)
            google_rs_response = requests.get(request_url, allow_redirects=False)
            the_location = google_rs_response.headers.get("Location")
        await event.edit("Found the Charactor. Honor CɪᴘʜᴇʀX")
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
        }
        response = requests.get(the_location, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        prs_div = soup.find_all("div", {"class": "r5a77d"})[0]
        prs_anchor_element = prs_div.find("a")
        BASE_URL + prs_anchor_element.get("href")
        prs_text = prs_anchor_element.text
    await event.edit("/protecc " + prs_text.replace("wallpaper phone", ""))
