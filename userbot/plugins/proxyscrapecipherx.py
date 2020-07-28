# Created By @Hackintush
# Usage : For Http Proxy : .http , For Socks4 : .socks4 , For socks5 : .socks5 

from asyncio import sleep
from telethon import events
from userbot.utils import admin_cmd 
from pySmartDL import SmartDL
import os

CɪᴘʜᴇʀX_Http = "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=3000&country=IR&ssl=all&anonymity=all" 
HTTP_TXT = ("**🔅Proxy List Info** \n🔹Type: __Https__ \n🔸TimeOut: __3000__ \n🔹Country: __IR__ \n🔸Ssl: All \n🔹Anonymity: __All__ \n🔸Provided By ✨CɪᴘʜᴇʀX✨ \n**🔹Here Is Your Proxy List** 👇")
CɪᴘʜᴇʀX_Socks4 = "https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=3000&country=IR"
SOCKS4_TXT = ("**🔅Proxy List Info** \n🔹Type: __Socks4__ \n🔸TimeOut: __3000__ \n🔹Country: __IR__ \n🔸Ssl: __Only For Http Proxy__ \n🔹Anonymity: __Only For Http__ \n🔸Provided By ✨CɪᴘʜᴇʀX✨ \n**🔹Here Is Your Proxy List** 👇")
CɪᴘʜᴇʀX_Socks5 = "https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=2000&country=all"
SOCKS5_TXT = ("**🔅Proxy List Info** \n🔹Type: __Socks5__ \n🔸TimeOut: __2000__ \n🔹Country: __All__ \n🔸Ssl: __Only For Http Proxy__ \n🔹Anonymity: __Only For Http__ \n🔸Provided By ✨CɪᴘʜᴇʀX✨ \n**🔹Here Is Your Proxy List** 👇")

@borg.on(admin_cmd(pattern="http")) 
async def CɪᴘʜᴇʀXhttp(event): 
    chat = await event.get_chat() 
    file_name = "Http_CipherX.txt"
    downloaded_file_name = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY , file_name)
    downloader = SmartDL( f"{CɪᴘʜᴇʀX_Http}" , downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False) 
    await borg.send_message(event.chat_id , HTTP_TXT)
    await event.client.send_file(event.chat_id , downloaded_file_name) 
    await event.delete()
    
@borg.on(admin_cmd(pattern="socks4")) 
async def CɪᴘʜᴇʀXsocks4(event): 
    chat = await event.get_chat() 
    file_name = "Socks4_CipherX.txt"
    downloaded_file_name = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY , file_name)
    downloader = SmartDL( f"{CɪᴘʜᴇʀX_Socks4}" , downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False) 
    await borg.send_message(event.chat_id , SOCKS4_TXT)
    await event.client.send_file(event.chat_id , downloaded_file_name) 
    await event.delete()
     
@borg.on(admin_cmd(pattern="socks5")) 
async def CɪᴘʜᴇʀXsocks5(event): 
    chat = await event.get_chat() 
    file_name = "Socks5_CipherX.txt"
    downloaded_file_name = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY , file_name)
    downloader = SmartDL( f"{CɪᴘʜᴇʀX_Socks5}" , downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False) 
    await borg.send_message(event.chat_id , SOCKS5_TXT)
    await event.client.send_file(event.chat_id , downloaded_file_name) 
    await event.delete()