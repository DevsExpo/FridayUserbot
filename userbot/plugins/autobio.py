# AutoBio plugin for TeleBot
# Using this might lead to ban of your account, use at your own risk.
# Re-Written by @its_xditya

import asyncio
import time
from telethon.tl import functions
from telethon.errors import FloodWaitError
from userbot.utils import admin_cmd


DEL_TIME_OUT = 60


@borg.on(admin_cmd(pattern="bio"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        bio = f"📅 {DMY} | This is my bio, I guess.. 😁 | ⌚️ {HM}"
        logger.info(bio)
        try:
            await borg(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                about=bio
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        # else:
            # logger.info(r.stringify())
            # await borg.send_message(  # pylint:disable=E0602
            #     Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
            #     "Successfully Changed Profile Bio"
            # )
        await asyncio.sleep(DEL_TIME_OUT)

