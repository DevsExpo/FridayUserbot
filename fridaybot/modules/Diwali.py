import asyncio
import random

from fridaybot.utils import admin_cmd

# Marshmellow
img1 = "https://telegra.ph/file/e2a002fbd79e519f30879.jpg"
img2 = "https://telegra.ph/file/916f762e89d55087844f9.jpg"
img3 = "https://telegra.ph/file/1452a59664280336e715b.jpg"
img4 = "https://telegra.ph/file/4e691947ef29e52bfc681.jpg"
img5 = "https://telegra.ph/file/1452a59664280336e715b.jpg"
img6 = "https://telegra.ph/file/b2ab83023df401e813f35.jpg"
img7 = "https://telegra.ph/file/fbe680b696f9bf0f6a0a8.jpg"
img8 = "https://telegra.ph/file/dcea4f11e8b615f5f78a4.jpg"
img9 = "https://telegra.ph/file/b71f2b1e788bbe338fa36.jpg"
img10 = "https://telegra.ph/file/6e96007d83b45e3239f95.jpg"
img11 = "https://telegra.ph/file/1a07fcc41ffc970925813.jpg"
img12 = "https://telegra.ph/file/e43e0ba9a9449da7c96bf.jpg"
img13 = "https://telegra.ph/file/08102180e81c6280834ae.jpg"
img14 = "https://telegra.ph/file/74fcf4bcba0057361895e.jpg"
img15 = "https://telegra.ph/file/fad1b7e9069e0d369c94b.jpg"
img16 = "https://telegra.ph/file/5eb1880e788a7663be2bb.jpg"


@borg.on(admin_cmd(outgoing=True, pattern="diwali"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("SENDING...:-)")
    await asyncio.sleep(0.9)
    x = random.randrange(1, 16)
    if x == 1:
        await borg.send_file(event.chat_id, img1)
        await event.delete()
    if x == 2:
        await borg.send_file(event.chat_id, img2)
        await event.delete()
    if x == 3:
        await borg.send_file(event.chat_id, img3)
        await event.delete()
    if x == 4:
        await borg.send_file(event.chat_id, img3)
        await event.delete()
    if x == 5:
        await borg.send_file(event.chat_id, img4)
        await event.delete()
    if x == 6:
        await borg.send_file(event.chat_id, img5)
        await event.delete()
    if x == 7:
        await borg.send_file(event.chat_id, img6)
        await event.delete()
    if x == 8:
        await borg.send_file(event.chat_id, img7)
        await event.delete()
    if x == 9:
        await borg.send_file(event.chat_id, img9)
        await event.delete()
    if x == 10:
        await borg.send_file(event.chat_id, img10)
        await event.delete()
    if x == 11:
        await borg.send_file(event.chat_id, img11)
        await event.delete()
    if x == 12:
        await borg.send_file(event.chat_id, img12)
        await event.delete()
    if x == 13:
        await borg.send_file(event.chat_id, img13)
        await event.delete()
    if x == 14:
        await borg.send_file(event.chat_id, img14)
        await event.delete()
    if x == 15:
        await borg.send_file(event.chat_id, img15)
        await event.delete()
