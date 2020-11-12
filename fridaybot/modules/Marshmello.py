from telethon import events
import asyncio
import os
import sys
from fridaybot.utils import admin_cmd
import random
#Marshmellow
img1=("https://telegra.ph/file/ec11c696c29a55f8c26d8.mp4")
img2=("https://telegra.ph/file/c840ab181db5e46ef4452.mp4")
img3=("https://telegra.ph/file/43e6a780c8191c8e45982.mp4")
img4=("https://telegra.ph/file/5a4913b32a0c1e4a4f0ea.mp4")
img5=("https://telegra.ph/file/704cbbbdaca9da75cb341.mp4")
img6=("https://telegra.ph/file/d9b725fb54006585b6ffb.mp4")
img7=("https://telegra.ph/file/eb9590fc40420bd33c800.mp4")
img8=("https://telegra.ph/file/da16427c75ad283882fdf.mp4")

@borg.on(admin_cmd(outgoing=True, pattern="mrs"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("SENDING....📱📲")
    await asyncio.sleep(0.9)
    x=(random.randrange(1,8))
    if x==1:
        await borg.send_file(event.chat_id,img1)
        await event.delete()
    if x==2:
        await borg.send_file(event.chat_id,img2)
        await event.delete()
    if x==3:
        await borg.send_file(event.chat_id,img3)
        await event.delete()
    if x==4:
        await borg.send_file(event.chat_id,img3)
        await event.delete()        
    if x==5:
        await borg.send_file(event.chat_id,img4)
        await event.delete()
    if x==6:
        await borg.send_file(event.chat_id,img5)
        await event.delete()
    if x==7:
        await borg.send_file(event.chat_id,img6)
        await event.delete()
    if x==8:
        await borg.send_file(event.chat_id,img7)
        await event.delete()      