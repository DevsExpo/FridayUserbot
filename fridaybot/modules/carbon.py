# Copyright (C) 2019 The Raphielscape Company LLC.
# Fixed Delete After Download Issue by @StarkXD
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
# Fixed and made better by @anubisxx
""" Userbot module containing various scrapers. """
import os
import random
from time import sleep
from urllib.parse import quote_plus
from fridaybot.utils import friday_on_cmd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from fridaybot import CHROME_DRIVER, CMD_HELP, GOOGLE_CHROME_BIN
from fridaybot.utils import register

CARBONLANG = "auto"
LANG = "en"


@friday.on(friday_on_cmd(pattern="carbon"))
async def carbon_api(e):
    if e.fwd_from:
        return
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        """ A Wrapper for carbon.now.sh """
        await e.edit("`Processing..`")
        CARBON = "https://carbon.now.sh/?l={lang}&code={code}"
        global CARBONLANG
        textx = await e.get_reply_message()
        pcode = e.text
        if pcode[8:]:
            pcodee = str(pcode[8:])
            if "|" in pcodee:
                pcode, skeme = pcodee.split("|")
            else:
                pcode = pcodee
                skeme = None
        elif textx:
            pcode = str(textx.message)
            skeme = None  # Importing message to module
        code = quote_plus(pcode)  # Converting to urlencoded
        await e.edit("`Meking Carbon...\n25%`")
        url = CARBON.format(code=code, lang=CARBONLANG)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.binary_location = GOOGLE_CHROME_BIN
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        prefs = {"download.default_directory": "./"}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER, options=chrome_options)
        driver.get(url)
        await e.edit("`Be Patient...\n50%`")
        download_path = "./"
        driver.command_executor._commands["send_command"] = (
            "POST",
            "/session/$sessionId/chromium/send_command",
        )
        params = {
            "cmd": "Page.setDownloadBehavior",
            "params": {"behavior": "allow", "downloadPath": download_path},
        }
        driver.execute("send_command", params)
        driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
        await e.edit("`Processing..\n75%`")
        # Waiting for downloading
        sleep(2.5)
        await e.edit("`Done Dana Done...\n100%`")
        file = "./carbon.png"
        await e.edit("`Uploading..`")
        await e.client.send_file(
            e.chat_id,
            file,
            caption="<< `Here's your carbon!` \n **Carbonised Using** [Friday](https://github.com/Starkgang/FridayUserbot)>>",
            force_document=True,
            reply_to=e.message.reply_to_msg_id,
        )
        os.remove("./carbon.png")
        driver.quit()
        # Removing carbon.png after uploading
        await e.delete()  # Deleting msg


CMD_HELP.update(
    {
        "carbon": "**Carbon**\
\n\n**Syntax : **`.carbon <text>`\
\n**Usage :** this plugin converts text into carbon."
    }
)
