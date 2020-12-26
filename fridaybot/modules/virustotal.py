import asyncio
import math
import os
import time

import requests
from uniborg.util import friday_on_cmd

from fridaybot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
from fridaybot.Configs import Config
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd

# from var import var


async def progress(current, total, event, start, type_of_ps, file_name=None):
    """Generic progress_callback for uploads and downloads."""
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current != total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "[{0}{1}] {2}%\n".format(
            "".join(["▰" for i in range(math.floor(percentage / 10))]),
            "".join(["▱" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nETA: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            await event.edit(
                "{}\nFile Name: `{}`\n{}".format(type_of_ps, file_name, tmp)
            )
        else:
            await event.edit("{}\n{}".format(type_of_ps, tmp))


def humanbytes(size):
    """Input size in bytes,
    outputs in a human readable format"""
    # https://stackoverflow.com/a/49361727/4723940
    if not size:
        return ""
    # 2 ** 10 = 1024
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def time_formatter(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + " day(s), ") if days else "")
        + ((str(hours) + " hour(s), ") if hours else "")
        + ((str(minutes) + " minute(s), ") if minutes else "")
        + ((str(seconds) + " second(s), ") if seconds else "")
        + ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    )
    return tmp[:-2]


sedpath = "./fridaydevs/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)


@friday.on(friday_on_cmd(pattern="vt(?: |$)(.*)", outgoing=True))
@friday.on(sudo_cmd(pattern="vt(?: |$)(.*)", allow_sudo=True))
async def download(target_file):
    friday = await edit_or_reply(target_file, "`Processing ...`")
    if Config.VIRUSTOTAL_API_KEY is None:
        await friday.edit(
            "Need to get an API key from https://virustotal.com\nModule stopping!"
        )
        return
    await friday.edit("Processing using fridaybot server ( ◜‿◝ )♡")
    input_str = Config.VIRUSTOTAL_API_KEY
    if not os.path.isdir(sedpath):
        os.makedirs(sedpath)
    if target_file.reply_to_msg_id:
        try:
            c_time = time.time()
            downloaded_file_name = await target_file.client.download_media(
                await target_file.get_reply_message(),
                TEMP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, target_file, c_time, "Downloading...")
                ),
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await friday.edit(str(e))
        else:
            await friday.edit(
                "Downloaded to `{}` successfully !!".format(downloaded_file_name)
            )
    else:
        await friday.edit("Reply to a file..")

    url = "https://www.virustotal.com/vtapi/v2/file/scan"

    params = {"apikey": input_str}
    files = {"file": (downloaded_file_name, open(downloaded_file_name, "rb"))}
    response = requests.post(url, files=files, params=params)
    try:
        a = response.json()
        b = a["permalink"]
    except:
        await friday.edit("your file is larger than 32 mb.")
    try:
        await friday.edit(
            f"<b><u> File Scan Request Complete</u></b>\n\n<b>Link of the report:-</b>\n<code>{b}</code>\n\nNote:- Please open the link after 5-10 minutes.",
            parse_mode="HTML",
        )
    except:
        await friday.edit("your file is larger than 32 mb.   --__--")


CMD_HELP.update(
    {
        "virustotal": "**VirusTotal**\
\n\n**Syntax : **`.vt <Reply To A File>`\
\n**Usage :** Scans replyed file with virustotal.\
\n**note** :** File should be less than 32 mb."
    }
)
