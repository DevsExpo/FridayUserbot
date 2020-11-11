"""Auto Profile Updation Commands
.autoname"""
import asyncio
import time

from telethon.errors import FloodWaitError
from telethon.tl import functions
from uniborg.util import edit_or_reply, friday_on_cmd, sudo_cmd

from fridaybot import ALIVE_NAME

DEL_TIME_OUT = 60
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "FridayUserbot"


@friday.on(friday_on_cmd(pattern="autoname"))  # pylint:disable=E0602
@friday.on(sudo_cmd(pattern="autoname", allow_sudo=True))
async def _(event):
    sed = await edit_or_reply(event, "`Starting AutoName Please Wait`")
    if event.fwd_from:
        return

    while True:

        DM = time.strftime("%d-%m-%y")

        HM = time.strftime("%H:%M")

        name = f"🕒{HM} ⚡{DEFAULTUSER}⚡ 📅{DM}"

        logger.info(name)

        try:

            await borg(
                functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                    first_name=name
                )
            )

        except FloodWaitError as ex:

            logger.warning(str(e))

            await asyncio.sleep(ex.seconds)

        # else:

        # logger.info(r.stringify())

        # await borg.send_message(  # pylint:disable=E0602

        #     Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602

        #     "Successfully Changed Profile Name"

        # )

        await asyncio.sleep(DEL_TIME_OUT)

    await sed.edit(f"Auto Name has been started my Master")
