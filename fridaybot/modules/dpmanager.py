# Author: Shubhendra Kushwaha
# @TheShubhendra (shubhendrakushwaha94@gmail.com)

from telethon.tl.functions.photos import DeletePhotosRequest
from telethon.tl.types import InputPhoto
from fridaybot import CMD_HELP


@friday.on(friday_on_cmd(pattern=r"deldpall$"))
async def delete_all_dp(event):
    client = event.client
    pics = await client.get_profile_photos("me")
    await event.edit(f"`Going to delete {len(pics)} profile pics`")
    for pic in pics:
        await client(
            DeletePhotosRequest(
                id=[
                    InputPhoto(
                        id=pic.id,
                        access_hash=pic.access_hash,
                        file_reference=pic.file_reference,
                    )
                ]
            )
        )


@friday.on(friday_on_cmd(pattern=r"deldp +(.*)"))
async def delete_all_dp(event):
    client = event.client
    pics = await client.get_profile_photos("me")
    try:
        n = int(event.pattern_match.group(1))
    except BaseException:
        return
    if n > len(pics):
        n = len(pics)
    await event.edit(f"`Going to delete {n} profile pics`")
    for i in range(n):
        pic = pics[i]
        await client(
            DeletePhotosRequest(
                id=[
                    InputPhoto(
                        id=pic.id,
                        access_hash=pic.access_hash,
                        file_reference=pic.file_reference,
                    )
                ]
            )
        )


@friday.on(friday_on_cmd(pattern=r"dpcount ?(.*)"))
async def dp_count(event):
    client = event.client
    pics = await client.get_profile_photos("me")
    await event.edit(f"`{len(pics)} pics found on your profile`")


CMD_HELP.update(
    {
        "deldpall": "Deletes your all profile pictures.",
        "deldp <number>": "Delete last given numbers of profile pictures.",
        "dpcount": "Count your current profile pictures",
    }
)
