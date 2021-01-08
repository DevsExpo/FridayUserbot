from io import BytesIO
from random import choice, randint
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont
from requests import get

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.saylie (.*)")
async def f_load(message):
    clrs = {
        "red": 1,
        "lime": 2,
        "green": 3,
        "blue": 4,
        "cyan": 5,
        "brown": 6,
        "purple": 7,
        "pink": 8,
        "orange": 9,
        "yellow": 10,
        "white": 11,
        "black": 12,
    }
    clr = randint(1, 12)
    text = message.pattern_match.group(1)
    reply = await message.get_reply_message()
    if text in clrs:
        clr = clrs[text]
        text = None
    if not text:
        if not reply:
            await bruh(message, message.sender)
            return
        if not reply.text:
            await bruh(message, reply.sender)
            return
        text = reply.pattern_match.group(1)

    if text.split(" ")[0] in clrs:
        clr = clrs[text.split(" ")[0]]
        text = " ".join(text.split(" ")[1:])

    if text == "colors":
        await message.edit(
            "Cores disponíveis:\n"
            + ("\n".join([f"• `{i}`" for i in list(clrs.keys())]))
        )
        return

    url = "https://raw.githubusercontent.com/KeyZenD/AmongUs/master/"
    font = ImageFont.truetype(BytesIO(get(url + "bold.ttf").content), 60)
    imposter = Image.open(BytesIO(get(f"{url}{clr}.png").content))
    text_ = "\n".join(["\n".join(wrap(part, 30)) for part in text.split("\n")])
    w, h = ImageDraw.Draw(Image.new("RGB", (1, 1))).multiline_textsize(
        text_, font, stroke_width=2
    )
    text = Image.new("RGBA", (w + 30, h + 30))
    ImageDraw.Draw(text).multiline_text(
        (15, 15), text_, "#FFF", font, stroke_width=2, stroke_fill="#000"
    )
    w = imposter.width + text.width + 10
    h = max(imposter.height, text.height)
    image = Image.new("RGBA", (w, h))
    image.paste(imposter, (0, h - imposter.height), imposter)
    image.paste(text, (w - text.width, 0), text)
    image.thumbnail((512, 512))
    output = BytesIO()
    output.name = "imposter.webp"
    image.save(output)
    output.seek(0)
    await message.delete()
    await message.client.send_file(message.to_id, output, reply_to=reply)


async def bruh(message, user):
    fn = user.first_name
    ln = user.last_name
    name = fn + (" " + ln if ln else "")
    name = "***" + name
    await message.edit(name + choice([" ", "Not"]) + "he was not an Imposter! ***")


CMD_HELP.update(
    {
        "amongus": ".saylie\
    \nSubmit a picture of an among us impostor with a sentence from you."
    }
)
