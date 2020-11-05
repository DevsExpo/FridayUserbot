import base64

from userbot.utils import friday_on_cmd


@friday.on(friday_on_cmd(pattern="bencode ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    kek = event.pattern_match.group(1)
    try:
        sample_string_bytes = kek.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")
        await event.edit(f"**ENCODED MESSAGE** - `{base64_string}`")
    except:
        await event.edit("Something went wrong !")


@friday.on(friday_on_cmd(pattern="bdecode ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    starky = event.pattern_match.group(1)
    try:
        base64_bytez = starky.encode("ascii")
        sample_string_bytez = base64.b64decode(base64_bytez)
        sample_strings = sample_string_bytez.decode("ascii")
        await event.edit(f"**Decoded string** : `{sample_strings}`")
    except:
        await event.edit("Can't be Decoded Probably Due To Invalid String")
