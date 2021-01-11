from telethon import events
import subprocess, os , asyncio, PIL, cv2, shutil
from userbot.utils import admin_cmd 
from userbot import bot
path = "./cipherx/"
if not os.path.isdir(path):
    os.makedirs(path)

@bot.on(admin_cmd(pattern="rgif"))
async def _(event):
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    download = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(download)
    ret, frame = img.read()
    cv2.imwrite("cipher.png", frame)
    danish = PIL.Image.open("cipher.png")
    dark,python = danish.size
    cobra = f"""ffmpeg -f lavfi -i color=c=00ff00:s={dark}x{python}:d=10 -loop 1 -i cipher.png -filter_complex "[1]rotate=angle=PI*t:fillcolor=none:ow='hypot(iw,ih)':oh=ow[fg];[0][fg]overlay=x=(W-w)/2:y=(H-h)/2:shortest=1:format=auto,format=yuv420p" -movflags +faststart cipher.mp4 -y"""                 
    await event.edit("```Processing ...```")
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    process = await asyncio.create_subprocess_shell(
        cobra, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    await event.edit("```Uploading...```")
    await event.client.send_file(event.chat_id, "cipher.mp4" , force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("cipher.mp4")
    os.remove("cipher.png")
