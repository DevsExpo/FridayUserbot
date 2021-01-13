import os

from PIL import Image

from userbot import CMD_HELP, bot
from userbot.utils import admin_cmd

if not os.path.isdir("./cipherx/"):
    os.makedirs("./cipherx/")


@bot.on(admin_cmd(pattern=r"cmask"))
async def scan(event):
    path = "cipherx"

    await event.edit("Lets give a Mask 🤪")

    reply = await event.get_reply_message()

    lol = await borg.download_media(reply.media, path)
    linc = event.text
    link = linc[7:]
    pic = linc[31:]
    import cv2

    imagePath = lol

    maskPath = f"{pic}"

    cascPath = "./resources/face.xml"

    faceCascade = cv2.CascadeClassifier(cascPath)

    image = cv2.imread(imagePath)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.15)

    background = Image.open(imagePath)

    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)

    file_name = "old.png"

    hehe = path + "/" + file_name

    background.save(hehe, "PNG")

    await borg.send_file(event.chat_id, hehe)

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)

    await event.delete()


@bot.on(admin_cmd(pattern=r"pro"))
async def scan(event):
    path = "cipherx"

    await event.edit("Lets give a Mask 🤪")

    reply = await event.get_reply_message()

    lol = await borg.download_media(reply.media, path)

    import cv2

    os.system("wget https://telegra.ph/file/f061c861ba85fbb23a51e.png")

    imagePath = lol

    maskPath = "f061c861ba85fbb23a51e.png"

    cascPath = "./resources/face.xml"

    faceCascade = cv2.CascadeClassifier(cascPath)

    image = cv2.imread(imagePath)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.15)

    background = Image.open(imagePath)

    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)

    file_name = "pro.png"

    hehe = path + "/" + file_name

    background.save(hehe, "PNG")

    await borg.send_file(event.chat_id, hehe)

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)

    await event.delete()


@bot.on(admin_cmd(pattern=r"oxy"))
async def scan(event):
    path = "cipherx"

    await event.edit("Lets give a Mask 🤪")

    reply = await event.get_reply_message()

    lol = await borg.download_media(reply.media, path)

    import cv2

    os.system("wget https://telegra.ph/file/df2d739544595ae337642.png")

    imagePath = lol

    maskPath = "df2d739544595ae337642.png"

    cascPath = "./resources/face.xml"

    faceCascade = cv2.CascadeClassifier(cascPath)

    image = cv2.imread(imagePath)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.15)

    background = Image.open(imagePath)

    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)

    file_name = "old.png"

    hehe = path + "/" + file_name

    background.save(hehe, "PNG")

    await borg.send_file(event.chat_id, hehe)

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)

    await event.delete()


@bot.on(admin_cmd(pattern=r"gold"))
async def scan(event):
    path = "cipherx"

    await event.edit("Lets give a Mask 🤪")

    reply = await event.get_reply_message()

    lol = await borg.download_media(reply.media, path)

    import cv2

    os.system("wget https://telegra.ph/file/4cc40d1e0846667488341.png")

    imagePath = lol

    maskPath = "4cc40d1e0846667488341.png"

    cascPath = "./resources/face.xml"

    faceCascade = cv2.CascadeClassifier(cascPath)

    image = cv2.imread(imagePath)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.15)

    background = Image.open(imagePath)

    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)

    file_name = "old.png"

    hehe = path + "/" + file_name

    background.save(hehe, "PNG")

    await borg.send_file(event.chat_id, hehe)

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)

    await event.delete()


@bot.on(admin_cmd(pattern=r"old"))
async def scan(event):
    path = "cipherx"

    await event.edit("Lets give a Mask 🤪")

    reply = await event.get_reply_message()

    lol = await borg.download_media(reply.media, path)

    import cv2

    os.system("wget https://telegra.ph/file/55fcb205c6f8f4790585e.png")

    imagePath = lol

    maskPath = "55fcb205c6f8f4790585e.png"

    cascPath = "./resources/face.xml"

    faceCascade = cv2.CascadeClassifier(cascPath)

    image = cv2.imread(imagePath)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.15)

    background = Image.open(imagePath)

    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)

    file_name = "old.png"

    hehe = path + "/" + file_name

    background.save(hehe, "PNG")

    await borg.send_file(event.chat_id, hehe)

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)

    await event.delete()


@bot.on(admin_cmd(pattern=r"krish"))
async def scan(event):
    path = "cipherx"

    await event.edit("Lets give a Mask 🤪")

    reply = await event.get_reply_message()

    lol = await borg.download_media(reply.media, path)

    import cv2

    os.system("wget https://telegra.ph/file/54d2a267d411951b41a20.png")

    imagePath = lol

    maskPath = "54d2a267d411951b41a20.png"

    cascPath = "./resources/face.xml"

    faceCascade = cv2.CascadeClassifier(cascPath)

    image = cv2.imread(imagePath)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.15)

    background = Image.open(imagePath)

    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)

    file_name = "old.png"

    hehe = path + "/" + file_name

    background.save(hehe, "PNG")

    await borg.send_file(event.chat_id, hehe)

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)

    await event.delete()


@bot.on(admin_cmd(pattern=r"cprotect"))
async def scan(event):
    path = "cipherx"

    await event.edit("Lets give a Mask 🤪")

    reply = await event.get_reply_message()

    lol = await borg.download_media(reply.media, path)

    import cv2

    os.system("wget https://telegra.ph/file/b934a713abb321bd1a9fe.png")

    imagePath = lol

    maskPath = "b934a713abb321bd1a9fe.png"

    cascPath = "./resources/face.xml"

    faceCascade = cv2.CascadeClassifier(cascPath)

    image = cv2.imread(imagePath)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.15)

    background = Image.open(imagePath)

    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)

    file_name = "old.png"

    hehe = path + "/" + file_name

    background.save(hehe, "PNG")

    await borg.send_file(event.chat_id, hehe)

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)

    await event.delete()


CMD_HELP.update(
    {
        "maskfun": "List of All Available Fun Commands.\
\n\n.cmask\
\n\n.pro\
\n\n.oxy\
\n\n.old\
\n\n.gold\
\n\n.krish\
\n\n.cprotect"
    }
)
