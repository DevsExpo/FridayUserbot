# Created By @Hackintush
# Usage : For Http Proxy : .http , For Socks4 : .socks4 , For socks5 : .socks5

import os

from pySmartDL import SmartDL

from userbot.utils import friday_on_cmd, sudo_cmd
from userbot import CMD_HELP

CIPHERX_HTTP = "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=3000&country=IR&ssl=all&anonymity=all"
HTTP_TXT = "**🔅Proxy List Info** \n🔹Type: __Https__ \n🔸TimeOut: __3000__ \n🔹Country: __IR__ \n🔸Ssl: All \n🔹Anonymity: __All__ \n🔸Provided By ✨CɪᴘʜᴇʀX✨ \n**🔹Here Is Your Proxy List** 👇"
CIPHERX_SOCKS4 = "https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=3000&country=IR"
SOCKS4_TXT = "**🔅Proxy List Info** \n🔹Type: __Socks4__ \n🔸TimeOut: __3000__ \n🔹Country: __IR__ \n🔸Ssl: __Only For Http Proxy__ \n🔹Anonymity: __Only For Http__ \n🔸Provided By ✨CɪᴘʜᴇʀX✨ \n**🔹Here Is Your Proxy List** 👇"
CIPHERX_SOCKS5 = "https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=2000&country=all"
SOCKS5_TXT = "**🔅Proxy List Info** \n🔹Type: __Socks5__ \n🔸TimeOut: __2000__ \n🔹Country: __All__ \n🔸Ssl: __Only For Http Proxy__ \n🔹Anonymity: __Only For Http__ \n🔸Provided By ✨CɪᴘʜᴇʀX✨ \n**🔹Here Is Your Proxy List** 👇"
sedpng = "https://telegra.ph/file/6a7f81fb3878d501f87e5.jpg"


@friday.on(friday_on_cmd(pattern="http$"))
@friday.on(sudo_cmd(pattern="http$", allow_sudo=True))
async def cipherxme(event):
    await event.get_chat()
    file_name = "Http_CipherX.txt"
    downloaded_file_name = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, file_name)
    downloader = SmartDL(f"{CIPHERX_HTTP}", downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    await event.client.send_file(
        event.chat_id,
        downloaded_file_name,
        force_document=False,
        thumb=sedpng,
        caption=HTTP_TXT,
    )


@friday.on(friday_on_cmd(pattern="socks4$"))
@friday.on(friday_on_cmd(pattern="socks4$", allow_sudo=True))
async def hackintush(event):
    await event.get_chat()
    file_name = "Socks4_CipherX.txt"
    downloaded_file_name = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, file_name)
    downloader = SmartDL(f"{CIPHERX_SOCKS4}", downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    # await borg.send_message(event.chat_id , SOCKS4_TXT)
    await event.client.send_file(
        event.chat_id,
        downloaded_file_name,
        thumb=sedpng,
        caption=SOCKS4_TXT,
        allow_cache=False,
        force_document=False,
    )


@friday.on(friday_on_cmd(pattern="socks5$"))
@friday.on(friday_on_cmd(pattern="socks5$", allow_sudo=True))
async def hubs(event):
    await event.get_chat()
    file_name = "Socks5_CipherX.txt"
    downloaded_file_name = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, file_name)
    downloader = SmartDL(f"{CIPHERX_SOCKS5}", downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    # await borg.send_message(event.chat_id , SOCKS5_TXT)
    await event.client.send_file(
        event.chat_id,
        downloaded_file_name,
        thumb=sedpng,
        caption=SOCKS5_TXT,
        allow_cache=False,
        force_document=False,
    )
    
CMD_HELP.update(
    {
        "proxyscrape": "**Proxy scrape**\
\n\n**Syntax : **`.http`\
\n**Usage :** Scrapes http proxies automatically.\
\n\n**Syntax : **`.socks4`\
\n**Usage :** Scrapes socks4 proxies automatically.\
\n\n**Syntax : **`.socks5`\
\n**Usage :** Scrapes socks5 proxies automatically."
    }
)
