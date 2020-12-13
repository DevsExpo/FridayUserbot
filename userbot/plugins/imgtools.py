# All Credits Belong to @hackintush

import os

import requests
from telethon.tl.types import MessageMediaPhoto

from userbot import CMD_HELP
from userbot.utils import friday_on_cmd, sudo_cmd

sedpath = "./cipherx/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)


@friday.on(friday_on_cmd(pattern=r"enc"))
@friday.on(sudo_cmd(pattern=r"enc", allow_sudo=True))
async def hmm(event):
    life = Config.DEEP_API_KEY
    if life == None:
        life = "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"
        await event.edit("No Api Key Found, Please Add it. For Now Using Local Key")
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    headers = {"api-key": life}
    hmm = await event.edit("Styling...")
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    img_file = {
        "image": open(img, "rb"),
    }
    url = "https://api.deepai.org/api/neural-style"
    r = requests.post(url=url, files=img_file, headers=headers).json()
    sedimg = r["output_url"]
    await borg.send_file(event.chat_id, sedimg)
    await hmm.delete()
    if os.path.exists(img):
        os.remove(img)


@friday.on(friday_on_cmd(pattern=r"reso"))
@friday.on(sudo_cmd(pattern=r"reso", allow_sudo=True))
async def hmm(event):
    life = Config.DEEP_API_KEY
    if life == None:
        life = "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"
        await event.edit("No Api Key Found, Please Add it. For Now Using Local Key")
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    headers = {"api-key": life}
    hmm = await event.edit("Making It Super Resolution...")
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    img_file = {
        "image": open(img, "rb"),
    }
    url = "https://api.deepai.org/api/torch-srgan"
    r = requests.post(url=url, files=img_file, headers=headers).json()
    sedimg = r["output_url"]
    await borg.send_file(event.chat_id, sedimg)
    await hmm.delete()
    if os.path.exists(img):
        os.remove(img)


@friday.on(friday_on_cmd(pattern=r"cele"))
@friday.on(sudo_cmd(pattern=r"cele", allow_sudo=True))
async def hmm(event):
    life = Config.DEEP_API_KEY
    if life == None:
        life = "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"
        await event.edit("No Api Key Found, Please Add it. For Now Using Local Key")
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    headers = {"api-key": life}
    hmm = await event.edit("Recognizing the Celebrity...")
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    img_file = {
        "image": open(img, "rb"),
    }
    url = "https://api.deepai.org/api/celebrity-recognition"
    r = requests.post(url=url, files=img_file, headers=headers).json()
    sedcopy = r["output"]
    hmmyes = sedcopy["detections"]
    game = sedcopy["nsfw_score"]
    final = f"**IMG RESULT** \n**Detections :** `{hmmyes}` \n**NSFW SCORE :** `{game}`"
    await borg.send_message(event.chat_id, final)
    await hmm.delete()
    if os.path.exists(img):
        os.remove(img)


CMD_HELP.update(
    {
        "imgtools": "**imgtools**\
        \n\n**Syntax : **`.enc`\
        \n**Usage :** Enhancerize any anime pic.\
        \n\n**Syntax : **`.reso`\
        \n**Usage :** Makes a super resolution quality image from your picture.\
        \n\n**Syntax : ** `.cele`\
        \n**Usage :** Recognizes the celebrity."
    }
)
