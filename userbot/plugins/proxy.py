# Created By @Hackintush
# Usage : For Http Proxy : .http , For Socks4 : .socks4 , For socks5 : .socks5

import os

from pySmartDL import SmartDL

from userbot.utils import friday_on_cmd, sudo_cmd

CɪᴘʜᴇʀX_Http = "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=3000&country=IR&ssl=all&anonymity=all"
HTTP_TXT = "**🔅Proxy List Info** \n🔹Type: __Https__ \n🔸TimeOut: __3000__ \n🔹Country: __IR__ \n🔸Ssl: All \n🔹Anonymity: __All__ \n🔸Provided By ✨CɪᴘʜᴇʀX✨ \n**🔹Here Is Your Proxy List** 👇"
CɪᴘʜᴇʀX_Socks4 = "https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=3000&country=IR"
SOCKS4_TXT = "**🔅Proxy List Info** \n🔹Type: __Socks4__ \n🔸TimeOut: __3000__ \n🔹Country: __IR__ \n🔸Ssl: __Only For Http Proxy__ \n🔹Anonymity: __Only For Http__ \n🔸Provided By ✨CɪᴘʜᴇʀX✨ \n**🔹Here Is Your Proxy List** 👇"
CɪᴘʜᴇʀX_Socks5 = "https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=2000&country=all"
SOCKS5_TXT = "**🔅Proxy List Info** \n🔹Type: __Socks5__ \n🔸TimeOut: __2000__ \n🔹Country: __All__ \n🔸Ssl: __Only For Http Proxy__ \n🔹Anonymity: __Only For Http__ \n🔸Provided By ✨CɪᴘʜᴇʀX✨ \n**🔹Here Is Your Proxy List** 👇"


@friday.on(friday_on_cmd(pattern="http$"))
@friday.on(sudo_cmd(pattern="http$", allow_sudo=True))
async def CɪᴘʜᴇʀXhttp(event):
    await event.get_chat()
    file_name = "Http_CipherX.txt"
    downloaded_file_name = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, file_name)
    downloader = SmartDL(f"{CɪᴘʜᴇʀX_Http}", downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    # await borg.send_message(event.chat_id, HTTP_TXT)
    await event.delete()
    await event.client.send_file(
        event.chat_id,
        downloaded_file_name,
        force_document=True,
        caption=HTTP_TXT,
    )


@friday.on(friday_on_cmd(pattern="socks4$"))
@friday.on(friday_on_cmd(pattern="socks4$", allow_sudo=True))
async def CɪᴘʜᴇʀXsocks4(event):
    await event.get_chat()
    file_name = "Socks4_CipherX.txt"
    downloaded_file_name = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, file_name)
    downloader = SmartDL(f"{CɪᴘʜᴇʀX_Socks4}", downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    # await borg.send_message(event.chat_id, SOCKS4_TXT)
    await event.delete()
    await event.client.send_file(
        event.chat_id,
        downloaded_file_name,
        caption=SOCKS4_TXT,
        allow_cache=False,
        force_document=True,
    )


@friday.on(friday_on_cmd(pattern="socks5$"))
@friday.on(friday_on_cmd(pattern="socks5$", allow_sudo=True))
async def CɪᴘʜᴇʀXsocks5(event):
    await event.get_chat()
    file_name = "Socks5_CipherX.txt"
    downloaded_file_name = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, file_name)
    downloader = SmartDL(f"{CɪᴘʜᴇʀX_Socks5}", downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    # await borg.send_message(event.chat_id, SOCKS5_TXT)
    await event.delete()
    await event.client.send_file(
        event.chat_id,
        downloaded_file_name,
        caption=SOCKS5_TXT,
        allow_cache=False,
        force_document=True,
    )
