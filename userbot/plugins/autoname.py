#New optimized and beautified format made by @Hackintush 
import asyncio
import time

from telethon.errors import FloodWaitError
from telethon.tl import functions
from uniborg.util import edit_or_reply, friday_on_cmd, sudo_cmd

from userbot import ALIVE_NAME, CMD_HELP

DEL_TIME_OUT = 60
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "CɪᴘʜᴇʀX"


@friday.on(friday_on_cmd(pattern="autoname"))  # pylint:disable=E0602
@friday.on(sudo_cmd(pattern="autoname", allow_sudo=True))
async def _(event):
    sed = await edit_or_reply(event, "`Starting AutoName. Please Wait...`")
    if event.fwd_from:
        return

    while True:
        dictionary = {
            '0' : '₀', '1' : '₁', '2' : '₂', '3' : '₃', '4': '₄',
            '5' : '₅', '6' : '₆', '7' : '₇', '8' : '₈', '9' : '₉' 
        }

        HM = time.strftime("%H:%M")
        for key, value in dictionary.items():
            HM = HM.replace(key,value)

        name = f"{DEFAULTUSER} {HM}"

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

    await sed.edit(f"**Auto Name has been started**")


CMD_HELP.update(
    {
        "autoname": "**Autoname**\
\n\n**Syntax : **`.autoname`\
\n**Usage :** Change Name With Time"
    }
)
