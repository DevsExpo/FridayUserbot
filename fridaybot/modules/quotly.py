#    This file is part of NiceGrill.

#    NiceGrill is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    NiceGrill is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with NiceGrill.  If not, see <https://www.gnu.org/licenses/>.

import json
import os
import random
import textwrap
import urllib

import emoji
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont, ImageOps
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions, types

from fridaybot import CMD_HELP, bot
from fridaybot.utils import friday_on_cmd

COLORS = [
    "#F07975",
    "#F49F69",
    "#F9C84A",
    "#8CC56E",
    "#6CC7DC",
    "#80C1FA",
    "#BCB3F9",
    "#E181AC",
]


class Quote:
    async def process(msg, user, client, reply, replied=None):
        font = ImageFont.truetype("Fonts/Roboto-Medium.ttf", 43, encoding="utf-16")
        font2 = ImageFont.truetype("Fonts/Roboto-Regular.ttf", 33, encoding="utf-16")
        mono = ImageFont.truetype("Fonts/DroidSansMono.ttf", 30, encoding="utf-16")
        italic = ImageFont.truetype("Fonts/Roboto-Italic.ttf", 33, encoding="utf-16")
        fallback = ImageFont.truetype("Fonts/Quivira.otf", 43, encoding="utf-16")
        # Splitting text
        maxlength = 0
        width = 0
        text = []
        for line in msg.split("\n"):
            length = len(line)
            if length > 43:
                text += textwrap.wrap(line, 43)
                maxlength = 43
                if width < fallback.getsize(line[:43])[0]:
                    if "MessageEntityCode" in str(reply.entities):
                        width = mono.getsize(line[:43])[0] + 30
                    else:
                        width = fallback.getsize(line[:43])[0]
                next
            else:
                text.append(line + "\n")
                if width < fallback.getsize(line)[0]:
                    if "MessageEntityCode" in str(reply.entities):
                        width = mono.getsize(line)[0] + 30
                    else:
                        width = fallback.getsize(line)[0]
                if maxlength < length:
                    maxlength = length

        title = ""
        try:
            details = await client(
                functions.channels.GetParticipantRequest(reply.chat_id, user.id)
            )
            if isinstance(details.participant, types.ChannelParticipantCreator):
                title = (
                    details.participant.rank if details.participant.rank else "Creator"
                )
            elif isinstance(details.participant, types.ChannelParticipantAdmin):
                title = (
                    details.participant.rank if details.participant.rank else "Admin"
                )
        except TypeError:
            pass
        titlewidth = font2.getsize(title)[0]

        # Get user name
        lname = "" if not user.last_name else user.last_name
        tot = user.first_name + " " + lname

        namewidth = fallback.getsize(tot)[0] + 10

        if namewidth > width:
            width = namewidth
        width += (
            titlewidth + 30 if titlewidth > width - namewidth else -(titlewidth - 30)
        )
        height = len(text) * 40

        # Profile Photo BG
        pfpbg = Image.new("RGBA", (125, 600), (0, 0, 0, 0))

        # Draw Template
        top, middle, bottom = await Quote.drawer(width, height)
        # Profile Photo Check and Fetch
        yes = False
        color = random.choice(COLORS)
        async for photo in client.iter_profile_photos(user, limit=1):
            yes = True
        if yes:
            pfp = await client.download_profile_photo(user)
            paste = Image.open(pfp)
            os.remove(pfp)
            paste.thumbnail((105, 105))

            # Mask
            mask_im = Image.new("L", paste.size, 0)
            draw = ImageDraw.Draw(mask_im)
            draw.ellipse((0, 0, 105, 105), fill=255)

            # Apply Mask
            pfpbg.paste(paste, (0, 0), mask_im)
        else:
            paste, color = await Quote.no_photo(user, tot)
            pfpbg.paste(paste, (0, 0))

        # Creating a big canvas to gather all the elements
        canvassize = (
            middle.width + pfpbg.width,
            top.height + middle.height + bottom.height,
        )
        canvas = Image.new("RGBA", canvassize)
        draw = ImageDraw.Draw(canvas)

        y = 80
        if replied:
            # Creating a big canvas to gather all the elements
            replname = "" if not replied.sender.last_name else replied.sender.last_name
            reptot = replied.sender.first_name + " " + replname
            font2.getsize(reptot)[0]
            if reply.sticker:
                sticker = await reply.download_media()
                stimg = Image.open(sticker)
                canvas = canvas.resize((stimg.width + pfpbg.width, stimg.height + 160))
                top = Image.new("RGBA", (200 + stimg.width, 300), (29, 29, 29, 255))
                draw = ImageDraw.Draw(top)
                await Quote.replied_user(
                    draw, reptot, replied.message.replace("\n", " "), 20
                )
                top = top.crop((135, 70, top.width, 300))
                canvas.paste(pfpbg, (0, 0))
                canvas.paste(top, (pfpbg.width + 10, 0))
                canvas.paste(stimg, (pfpbg.width + 10, 140))
                os.remove(sticker)
                return True, canvas
            canvas = canvas.resize((canvas.width + 60, canvas.height + 120))
            top, middle, bottom = await Quote.drawer(middle.width + 60, height + 105)
            canvas.paste(pfpbg, (0, 0))
            canvas.paste(top, (pfpbg.width, 0))
            canvas.paste(middle, (pfpbg.width, top.height))
            canvas.paste(bottom, (pfpbg.width, top.height + middle.height))
            draw = ImageDraw.Draw(canvas)
            if replied.sticker:
                replied.text = "Sticker"
            elif replied.photo:
                replied.text = "Photo"
            elif replied.audio:
                replied.text = "Audio"
            elif replied.voice:
                replied.text = "Voice Message"
            elif replied.document:
                replied.text = "Document"
            await Quote.replied_user(
                draw,
                reptot,
                replied.message.replace("\n", " "),
                maxlength + len(title),
                len(title),
            )
            y = 200
        elif reply.sticker:
            sticker = await reply.download_media()
            stimg = Image.open(sticker)
            canvas = canvas.resize((stimg.width + pfpbg.width + 30, stimg.height + 10))
            canvas.paste(pfpbg, (0, 0))
            canvas.paste(stimg, (pfpbg.width + 10, 10))
            os.remove(sticker)
            return True, canvas
        elif reply.document and not reply.audio and not reply.audio:
            docname = ".".join(reply.document.attributes[-1].file_name.split(".")[:-1])
            doctype = reply.document.attributes[-1].file_name.split(".")[-1].upper()
            if reply.document.size < 1024:
                docsize = str(reply.document.size) + " Bytes"
            elif reply.document.size < 1048576:
                docsize = str(round(reply.document.size / 1024, 2)) + " KB "
            elif reply.document.size < 1073741824:
                docsize = str(round(reply.document.size / 1024 ** 2, 2)) + " MB "
            else:
                docsize = str(round(reply.document.size / 1024 ** 3, 2)) + " GB "
            docbglen = (
                font.getsize(docsize)[0]
                if font.getsize(docsize)[0] > font.getsize(docname)[0]
                else font.getsize(docname)[0]
            )
            canvas = canvas.resize((pfpbg.width + width + docbglen, 160 + height))
            top, middle, bottom = await Quote.drawer(width + docbglen, height + 30)
            canvas.paste(pfpbg, (0, 0))
            canvas.paste(top, (pfpbg.width, 0))
            canvas.paste(middle, (pfpbg.width, top.height))
            canvas.paste(bottom, (pfpbg.width, top.height + middle.height))
            canvas = await Quote.doctype(docname, docsize, doctype, canvas)
            y = 80 if text else 0
        else:
            canvas.paste(pfpbg, (0, 0))
            canvas.paste(top, (pfpbg.width, 0))
            canvas.paste(middle, (pfpbg.width, top.height))
            canvas.paste(bottom, (pfpbg.width, top.height + middle.height))
            y = 85

        # Writing User's Name
        space = pfpbg.width + 30
        namefallback = ImageFont.truetype("Fonts/Quivira.otf", 43, encoding="utf-16")
        for letter in tot:
            if letter in emoji.UNICODE_EMOJI:
                newemoji, mask = await Quote.emoji_fetch(letter)
                canvas.paste(newemoji, (space, 24), mask)
                space += 40
            else:
                if not await Quote.fontTest(letter):
                    draw.text((space, 20), letter, font=namefallback, fill=color)
                    space += namefallback.getsize(letter)[0]
                else:
                    draw.text((space, 20), letter, font=font, fill=color)
                    space += font.getsize(letter)[0]

        if title:
            draw.text(
                (canvas.width - titlewidth - 20, 25), title, font=font2, fill="#898989"
            )

        # Writing all separating emojis and regular texts
        x = pfpbg.width + 30
        bold, mono, italic, link = await Quote.get_entity(reply)
        index = 0
        emojicount = 0
        textfallback = ImageFont.truetype("Fonts/Quivira.otf", 33, encoding="utf-16")
        textcolor = "white"
        for line in text:
            for letter in line:
                index = (
                    msg.find(letter)
                    if emojicount == 0
                    else msg.find(letter) + emojicount
                )
                for offset, length in bold.items():
                    if index in range(offset, length):
                        font2 = ImageFont.truetype(
                            "Fonts/Roboto-Medium.ttf", 33, encoding="utf-16"
                        )
                        textcolor = "white"
                for offset, length in italic.items():
                    if index in range(offset, length):
                        font2 = ImageFont.truetype(
                            "Fonts/Roboto-Italic.ttf", 33, encoding="utf-16"
                        )
                        textcolor = "white"
                for offset, length in mono.items():
                    if index in range(offset, length):
                        font2 = ImageFont.truetype(
                            "Fonts/DroidSansMono.ttf", 30, encoding="utf-16"
                        )
                        textcolor = "white"
                for offset, length in link.items():
                    if index in range(offset, length):
                        font2 = ImageFont.truetype(
                            "Fonts/Roboto-Regular.ttf", 30, encoding="utf-16"
                        )
                        textcolor = "#898989"
                if letter in emoji.UNICODE_EMOJI:
                    newemoji, mask = await Quote.emoji_fetch(letter)
                    canvas.paste(newemoji, (x, y - 2), mask)
                    x += 45
                    emojicount += 1
                else:
                    if not await Quote.fontTest(letter):
                        draw.text((x, y), letter, font=textfallback, fill=textcolor)
                        x += textfallback.getsize(letter)[0]
                    else:
                        draw.text((x, y), letter, font=font2, fill=textcolor)
                        x += font2.getsize(letter)[0]
                msg = msg.replace(letter, "¶", 1)
            y += 40
            x = pfpbg.width + 30
        return True, canvas

    async def drawer(width, height):
        # Top part
        top = Image.new("RGBA", (width, 20), (0, 0, 0, 0))
        draw = ImageDraw.Draw(top)
        draw.line((10, 0, top.width - 20, 0), fill=(29, 29, 29, 255), width=50)
        draw.pieslice((0, 0, 30, 50), 180, 270, fill=(29, 29, 29, 255))
        draw.pieslice(
            (top.width - 75, 0, top.width, 50), 270, 360, fill=(29, 29, 29, 255)
        )

        # Middle part
        middle = Image.new("RGBA", (top.width, height + 75), (29, 29, 29, 255))

        # Bottom part
        bottom = ImageOps.flip(top)

        return top, middle, bottom

    async def fontTest(letter):
        test = TTFont("Fonts/Roboto-Medium.ttf")
        for table in test["cmap"].tables:
            if ord(letter) in table.cmap.keys():
                return True

    async def get_entity(msg):
        bold = {0: 0}
        italic = {0: 0}
        mono = {0: 0}
        link = {0: 0}
        if not msg.entities:
            return bold, mono, italic, link
        for entity in msg.entities:
            if isinstance(entity, types.MessageEntityBold):
                bold[entity.offset] = entity.offset + entity.length
            elif isinstance(entity, types.MessageEntityItalic):
                italic[entity.offset] = entity.offset + entity.length
            elif isinstance(entity, types.MessageEntityCode):
                mono[entity.offset] = entity.offset + entity.length
            elif isinstance(entity, types.MessageEntityUrl):
                link[entity.offset] = entity.offset + entity.length
            elif isinstance(entity, types.MessageEntityTextUrl):
                link[entity.offset] = entity.offset + entity.length
            elif isinstance(entity, types.MessageEntityMention):
                link[entity.offset] = entity.offset + entity.length
        return bold, mono, italic, link

    async def doctype(name, size, type, canvas):
        font = ImageFont.truetype("Fonts/Roboto-Medium.ttf", 38)
        doc = Image.new("RGBA", (130, 130), (29, 29, 29, 255))
        draw = ImageDraw.Draw(doc)
        draw.ellipse((0, 0, 130, 130), fill="#434343")
        draw.line((66, 28, 66, 53), width=14, fill="white")
        draw.polygon([(67, 77), (90, 53), (42, 53)], fill="white")
        draw.line((40, 87, 90, 87), width=8, fill="white")
        canvas.paste(doc, (160, 23))
        draw2 = ImageDraw.Draw(canvas)
        draw2.text((320, 40), name, font=font, fill="white")
        draw2.text((320, 97), size + type, font=font, fill="#AAAAAA")
        return canvas

    async def no_photo(reply, tot):
        pfp = Image.new("RGBA", (105, 105), (0, 0, 0, 0))
        pen = ImageDraw.Draw(pfp)
        color = random.choice(COLORS)
        pen.ellipse((0, 0, 105, 105), fill=color)
        letter = "" if not tot else tot[0]
        font = ImageFont.truetype("Fonts/Roboto-Regular.ttf", 60)
        pen.text((32, 17), letter, font=font, fill="white")
        return pfp, color

    async def emoji_fetch(emoji):
        emojis = json.loads(
            urllib.request.urlopen(
                "https://github.com/erenmetesar/modules-repo/raw/master/emojis.txt"
            )
            .read()
            .decode()
        )
        if emoji in emojis:
            img = emojis[emoji]
            return await Quote.transparent(
                urllib.request.urlretrieve(img, ".tmp/emoji.png")[0]
            )
        else:
            img = emojis["⛔"]
            return await Quote.transparent(
                urllib.request.urlretrieve(img, ".tmp/emoji.png")[0]
            )

    async def transparent(emoji):
        emoji = Image.open(emoji).convert("RGBA")
        emoji.thumbnail((40, 40))

        # Mask
        mask = Image.new("L", (40, 40), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 40, 40), fill=255)
        return emoji, mask

    async def replied_user(draw, tot, text, maxlength, title):
        namefont = ImageFont.truetype("Fonts/Roboto-Medium.ttf", 38)
        namefallback = ImageFont.truetype("Fonts/Quivira.otf", 38)
        textfont = ImageFont.truetype("Fonts/Roboto-Regular.ttf", 32)
        textfallback = ImageFont.truetype("Fonts/Roboto-Medium.ttf", 38)
        maxlength = maxlength + 7 if maxlength < 10 else maxlength
        text = text[: maxlength - 2] + ".." if len(text) > maxlength else text
        draw.line((165, 90, 165, 170), width=5, fill="white")
        space = 0
        for letter in tot:
            if not await Quote.fontTest(letter):
                draw.text((180 + space, 86), letter, font=namefallback, fill="#888888")
                space += namefallback.getsize(letter)[0]
            else:
                draw.text((180 + space, 86), letter, font=namefont, fill="#888888")
                space += namefont.getsize(letter)[0]
        space = 0
        for letter in text:
            if not await Quote.fontTest(letter):
                draw.text((180 + space, 132), letter, font=textfallback, fill="#888888")
                space += textfallback.getsize(letter)[0]
            else:
                draw.text((180 + space, 132), letter, font=textfont, fill="white")
                space += textfont.getsize(letter)[0]


@borg.on(friday_on_cmd(pattern="q(?: |$)(.*)"))
async def create_sticker(message):
    if message.fwd_from:
        return
    if not message.reply_to_msg_id:
        await message.edit("```Reply to any user message.```")
        return
    if not os.path.isdir(".tmp"):
        os.mkdir(".tmp", 0o755)
    await message.delete()
    reply = await message.get_reply_message()
    msg = reply.message
    repliedreply = await reply.get_reply_message()
    user = (
        await borg.get_entity(reply.forward.sender) if reply.fwd_from else reply.sender
    )
    res, canvas = await Quote.process(msg, user, borg, reply, repliedreply)
    if not res:
        return
    canvas.save(".tmp/sticker.webp")
    await message.respond(file=".tmp/sticker.webp")
    os.remove(".tmp/sticker.webp")


@friday.on(friday_on_cmd(pattern=r"qbot(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    chat = "@QuotLyBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Making a Quote```")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1031952739)
            )
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @QuotLyBot and try again```")
            return
        if response.text.startswith("Hi!"):
            await event.edit(
                "```Can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


CMD_HELP.update(
    {
        "quotly": "**Quotly**\
\n\n**Syntax : **`.qbot media <reply to some message>`\
\n**Usage :** you will get quoted message."
    }
)
