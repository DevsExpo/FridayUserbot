# Created By @Hackintush
# Usage : For Http Proxy : .http , For Socks4 : .socks4 , For socks5 : .socks5 

from telethon import events
from userbot.utils import admin_cmd 
from pySmartDL import SmartDL
import os

CɪᴘʜᴇʀX_Http = "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=3000&country=IR&ssl=all&anonymity=all" 
HTTP_TXT = ("**Proxy Info** \nType: __Https__ \nTimeOut: __3000__ \nCountry: __IR__ \nSsl: All \nAnonymity: __All__ \nUploaded By [CɪᴘʜᴇʀX](https://t.me/Hackintush) \n**Here Is Your Proxy** 👇")
CɪᴘʜᴇʀX_Socks4 = "https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=3000&country=IR"
SOCKS4_TXT = ("**Proxy Info** \nType: __Socks5__ \nTimeOut: __10000__ \nCountry: __All__ \nSsl: __Only For Http Proxy__ \nAnonymity: __Only For Http__ \nUploaded By [CɪᴘʜᴇʀX](https://t.me/Hackintush) \n**Here Is Your Proxy** 👇")
CɪᴘʜᴇʀX_Socks5 = "https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=3000&country=IR"
SOCKS5_TXT = ("**Proxy Info** \nType: __Socks5__ \nTimeOut: __10000__ \nCountry: __All__ \nSsl: __Only For Http Proxy__ \nAnonymity: __Only For Http__ \nUploaded By [CɪᴘʜᴇʀX](https://t.me/Hackintush) \n**Here Is Your Proxy** 👇")

@borg.on(admin_cmd(pattern="http")) 
async def CɪᴘʜᴇʀXhttp(event): 
    chat = await event.get_chat() 
    file_name = "Http_CipherX.txt"
    downloaded_file_name = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY , file_name)
    downloader = SmartDL( f"{CɪᴘʜᴇʀX_Http}" , downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False) 
    await borg.send_message(event.chat_id , HTTP_TXT)
    await event.client.send_file(event.chat_id , downloaded_file_name) 
    
@borg.on(admin_cmd(pattern="socks4")) 
async def CɪᴘʜᴇʀXsocks4(event): 
    chat = await event.get_chat() 
    file_name = "Socks4_CipherX.txt"
    downloaded_file_name = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY , file_name)
    downloader = SmartDL( f"{CɪᴘʜᴇʀX_Socks4}" , downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False) 
    await borg.send_message(event.chat_id , SOCKS4_TXT)
    await event.client.send_file(event.chat_id , downloaded_file_name) 
 
@borg.on(admin_cmd(pattern="socks5")) 
async def CɪᴘʜᴇʀXsocks5(event): 
    chat = await event.get_chat() 
    file_name = "Socks5_CipherX.txt"
    downloaded_file_name = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY , file_name)
    downloader = SmartDL( f"{CɪᴘʜᴇʀX_Socks5}" , downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False) 
    await borg.send_message(event.chat_id , SOCKS5_TXT)
    await event.client.send_file(event.chat_id , downloaded_file_name) 
    