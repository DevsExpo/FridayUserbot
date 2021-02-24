# @UniBorg
from urllib.parse import urlparse
import asyncio
import json
import math
import requests
import os
import subprocess
import time
from datetime import datetime
from urllib.parse import urlparse
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pySmartDL import SmartDL
from telethon.tl.types import DocumentAttributeVideo
from fridaybot.function.FastTelethon import upload_file
from fridaybot import CMD_HELP, LOGS, TEMP_DOWNLOAD_DIRECTORY
from fridaybot.function.events import register
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd


async def progress(current, total, event, start, type_of_ps, file_name=None):
    """Generic progress_callback for uploads and downloads."""
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        if elapsed_time == 0:
            return
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            "".join(["▰" for i in range(math.floor(percentage / 10))]),
            "".join(["▱" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nETA: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            try:
                await event.edit(
                    "{}\n**File Name:** `{}`\n{}".format(type_of_ps, file_name, tmp)
                    
                )
            except:
                pass
        else:
            try:
                await event.edit("{}\n{}".format(type_of_ps, tmp))
            except:
                pass


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


@friday.on(friday_on_cmd(pattern="download(?: |$)(.*)"))
@friday.on(sudo_cmd(pattern="download(?: |$)(.*)", allow_sudo=True))
async def download(target_file):
    if target_file.fwd_from:
        return
    friday = await friday.edit_or_reply(target_file, "`Processing ...`")
    await friday.edit("Processing using fridaybot server ( ◜‿◝ )♡")
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    if not target_file.reply_to_msg_id:
        await friday.edit("`Reply to a message to download to my local server.`")
        return
    sedd = await target_file.get_reply_message()
    if not sedd.media:
        await event.edit("`I Can Only Download Media As For Now.`")
        return
    try:
        c_time = time.time()
        downloaded_file_name = await target_file.client.download_media(
                await target_file.get_reply_message(),
                TEMP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, target_file, c_time, "Downloading This Media...")
                ),
            )
    except Exception as e:  # pylint:disable=C0103,W0703
        await friday.edit(str(e))
    else:
        await friday.edit(
                "Downloaded to `{}` successfully !!".format(downloaded_file_name)
            )


@friday.on(friday_on_cmd(pattern=r"uploadir (.*)"))
async def uploadir(udir_event):
    if udir_event.fwd_from:
        return
    """ For .uploadir command, allows you to upload everything from a folder in the server"""
    input_str = udir_event.pattern_match.group(1)
    if os.path.exists(input_str):
        await udir_event.edit("Downloading Using Userbot Server....")
        lst_of_files = []
        for r, d, f in os.walk(input_str):
            for file in f:
                lst_of_files.append(os.path.join(r, file))
            for file in d:
                lst_of_files.append(os.path.join(r, file))
        LOGS.info(lst_of_files)
        uploaded = 0
        await udir_event.edit(
            "Found {} files. Uploading will start soon. Please wait!".format(
                len(lst_of_files)
            )
        )
        for single_file in lst_of_files:
            if os.path.exists(single_file):
                # https://stackoverflow.com/a/678242/4723940
                caption_rts = os.path.basename(single_file)
                c_time = time.time()
                if not caption_rts.lower().endswith(".mp4"):
                    await udir_event.client.send_file(
                        udir_event.chat_id,
                        single_file,
                        caption=caption_rts,
                        force_document=False,
                        allow_cache=False,
                        reply_to=udir_event.message.id,
                        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                            progress(
                                d,
                                t,
                                udir_event,
                                c_time,
                                "Uploading in Progress.......",
                                single_file,
                            )
                        ),
                    )
                else:
                    thumb_image = os.path.join(input_str, "thumb.jpg")
                    c_time = time.time()
                    metadata = extractMetadata(createParser(single_file))
                    duration = 0
                    width = 0
                    height = 0
                    if metadata.has("duration"):
                        duration = metadata.get("duration").seconds
                    if metadata.has("width"):
                        width = metadata.get("width")
                    if metadata.has("height"):
                        height = metadata.get("height")
                    await udir_event.client.send_file(
                        udir_event.chat_id,
                        single_file,
                        caption=caption_rts,
                        thumb=thumb_image,
                        force_document=False,
                        allow_cache=False,
                        reply_to=udir_event.message.id,
                        attributes=[
                            DocumentAttributeVideo(
                                duration=duration,
                                w=width,
                                h=height,
                                round_message=False,
                                supports_streaming=True,
                            )
                        ],
                        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                            progress(
                                d, t, udir_event, c_time, "Uploading...", single_file
                            )
                        ),
                    )
                os.remove(single_file)
                uploaded = uploaded + 1
        await udir_event.edit("Uploaded {} files successfully !!".format(uploaded))
    else:
        await udir_event.edit("404: Directory Not Found")


@friday.on(friday_on_cmd(pattern=r"upload (.*)"))
async def upload(u_event):
    if u_event.fwd_from:
        return
    """ For .upload command, allows you to upload a file from the fridaybot's server """
    await u_event.edit("Processing ...")
    input_str = u_event.pattern_match.group(1)
    if input_str in ("fridaybot.session", "config.env"):
        await u_event.edit("`That's a dangerous operation! Not Permitted!`")
        return
    if os.path.exists(input_str):
        c_time = time.time()
        await u_event.client.send_file(
            u_event.chat_id,
            input_str,
            force_document=True,
            allow_cache=False,
            reply_to=u_event.message.id,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, u_event, c_time, "Uploading...", input_str)
            ),
        )
        await u_event.edit("Uploaded successfully !!")
    else:
        await u_event.edit("404: File Not Found")


def get_video_thumb(file, output=None, width=90):
    """ Get video thumbnail """
    metadata = extractMetadata(createParser(file))
    popen = subprocess.Popen(
        [
            "ffmpeg",
            "-i",
            file,
            "-ss",
            str(
                int((0, metadata.get("duration").seconds)[metadata.has("duration")] / 2)
            ),
            "-filter:v",
            "scale={}:-1".format(width),
            "-vframes",
            "1",
            output,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    if not popen.returncode and os.path.lexists(file):
        return output
    return None


def extract_w_h(file):
    """ Get width and height of media """
    command_to_run = [
        "ffprobe",
        "-v",
        "quiet",
        "-print_format",
        "json",
        "-show_format",
        "-show_streams",
        file,
    ]
    # https://stackoverflow.com/a/11236144/4723940
    try:
        t_response = subprocess.check_output(command_to_run, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as exc:
        LOGS.warning(exc)
    else:
        x_reponse = t_response.decode("UTF-8")
        response_json = json.loads(x_reponse)
        width = int(response_json["streams"][0]["width"])
        height = int(response_json["streams"][0]["height"])
        return width, height


@friday.on(friday_on_cmd(pattern=r"uploadas(stream|vn|all) (.*)"))
async def uploadas(uas_event):
    if uas_event.fwd_from:
        return
    """ For .uploadas command, allows you to specify some arguments for upload. """
    await uas_event.edit("Processing ...")
    type_of_upload = uas_event.pattern_match.group(1)
    supports_streaming = False
    round_message = False
    spam_big_messages = False
    if type_of_upload == "stream":
        supports_streaming = True
    if type_of_upload == "vn":
        round_message = True
    if type_of_upload == "all":
        spam_big_messages = True
    input_str = uas_event.pattern_match.group(2)
    thumb = None
    file_name = None
    if "|" in input_str:
        file_name, thumb = input_str.split("|")
        file_name = file_name.strip()
        thumb = thumb.strip()
    else:
        file_name = input_str
        thumb_path = "a_random_f_file_name" + ".jpg"
        thumb = get_video_thumb(file_name, output=thumb_path)
    if os.path.exists(file_name):
        metadata = extractMetadata(createParser(file_name))
        duration = 0
        width = 0
        height = 0
        if metadata.has("duration"):
            duration = metadata.get("duration").seconds
        if metadata.has("width"):
            width = metadata.get("width")
        if metadata.has("height"):
            height = metadata.get("height")
        try:
            if supports_streaming:
                c_time = time.time()
                await uas_event.client.send_file(
                    uas_event.chat_id,
                    file_name,
                    thumb=thumb,
                    caption=input_str,
                    force_document=False,
                    allow_cache=False,
                    reply_to=uas_event.message.id,
                    attributes=[
                        DocumentAttributeVideo(
                            duration=duration,
                            w=width,
                            h=height,
                            round_message=False,
                            supports_streaming=True,
                        )
                    ],
                    progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                        progress(d, t, uas_event, c_time, "Uploading...", file_name)
                    ),
                )
            elif round_message:
                c_time = time.time()
                await uas_event.client.send_file(
                    uas_event.chat_id,
                    file_name,
                    thumb=thumb,
                    allow_cache=False,
                    reply_to=uas_event.message.id,
                    video_note=True,
                    attributes=[
                        DocumentAttributeVideo(
                            duration=0,
                            w=1,
                            h=1,
                            round_message=True,
                            supports_streaming=True,
                        )
                    ],
                    progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                        progress(d, t, uas_event, c_time, "Uploading...", file_name)
                    ),
                )
            elif spam_big_messages:
                await uas_event.edit("TBD: Not (yet) Implemented")
                return
            os.remove(thumb)
            await uas_event.edit("Uploaded successfully !!")
        except FileNotFoundError as err:
            await uas_event.edit(str(err))
    else:
        await uas_event.edit("404: File Not Found")

@borg.on(friday_on_cmd(pattern='smartdl'))
async def lul(event):
    if event.fwd_from:
        return
    input_str = event.raw_text.split(" ", maxsplit=1)[1]
    mone = await event.edit("**Processing..**")
    start = datetime.now()
    url = input_str
    a = urlparse(input_str)
    file_name = os.path.basename(a.path)
    to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
    downloaded_file_name = os.path.join(to_download_directory, file_name)
    downloader = SmartDL(url, downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    display_message = ""
    c_time = time.time()
    while not downloader.isFinished():
        total_length = downloader.filesize if downloader.filesize else None
        downloaded = downloader.get_dl_size()
        now = time.time()
        diff = now - c_time
        percentage = downloader.get_progress() * 100
        speed = downloader.get_speed()
        elapsed_time = round(diff) * 1000
        progress_str = "[{0}{1}]\nProgress: {2}%".format(
                ''.join(["▰" for i in range(math.floor(percentage / 5))]),
                ''.join(["▱" for i in range(20 - math.floor(percentage / 5))]),
        round(percentage, 2))
        estimated_total_time = downloader.get_eta(human=True)
        try:
            current_message = f"trying to download\n"
            current_message += f"URL: {url}\n"
            current_message += f"File Name: {file_name}\n"
            current_message += f"{progress_str}\n"
            current_message += f"{humanbytes(downloaded)} of {humanbytes(total_length)}\n"
            current_message += f"ETA: {estimated_total_time}"
            if round(diff % 10.00) == 0 and current_message != display_message:
                await mone.edit(current_message)
                display_message = current_message
        except Exception as e:
            logger.info(str(e))
    end = datetime.now()
    ms = (end - start).seconds
    if downloader.isSuccessful():
        c_time = time.time()
        lul = await mone.edit("Downloaded to `{}` in {} seconds.".format(downloaded_file_name, ms))
        lol_m = await upload_file(
            file_name=file_name,
            client=borg,
            file=open(downloaded_file_name, 'rb'),
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, event, c_time, "Uploading This File.", downloaded_file_name
                )
            ),
        )
        await borg.send_file(event.chat_id,
                        lol_m,
                        caption=file_name,
                        force_document=False,
                        allow_cache=False,
                    )
        await lul.delete()
        os.remove(downloaded_file_name)
    else:
        await mone.edit("Incorrect URL\n {}".format(input_str))
    
#    Copyright (C) Midhun Km 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    
@friday.on(friday_on_cmd(pattern="zeelink"))
async def lol_kangers(event):
    if event.fwd_from:
        return
    input_str = event.raw_text.split(" ", maxsplit=1)[1]
    if 'zee' in input_str:
        url = "http://devsexpo.me/zee/"
        sed = {
        'url': input_str
        }
        lmao = requests.get(url=url, headers=sed).json()
    else:
        await event.edit("Only Zee Videos Supported.")
        return
    if lmao['success'] is False:
        await event.edit("Task Failed Due To " + str(lmao['error']))
        return
    await event.edit("Direct Link Fetched \nURL : " + str(lmao['url']))
        
        
CMD_HELP.update(
    {
        "download": ".dl <link|filename> or reply to media\
\nUsage: Downloads file to the server.\
\n\n.upload <path in server>\
\nUsage: Uploads a locally stored file to the chat."
    }
)
