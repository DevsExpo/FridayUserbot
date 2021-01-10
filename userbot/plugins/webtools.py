# @Hackintush
import asyncio
import math
import os
import time

import requests
from iplookup import iplookup
from selenium import webdriver
from youtube_search import YoutubeSearch

from userbot import CMD_HELP, logging
from userbot.Configs import Config
from userbot.function import apk_dl
from userbot.utils import edit_or_reply, friday_on_cmd, sudo_cmd

sedpath = Config.TMP_DOWNLOAD_DIRECTORY
from userbot import logging

logger = logging.getLogger("[--WARNING--]")
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)

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
            "".join(["■" for i in range(math.floor(percentage / 5))]),
            "".join(["▢" for i in range(20 - math.floor(percentage / 5))]),
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


@friday.on(friday_on_cmd(pattern="wshot ?(.*)"))
@friday.on(sudo_cmd(pattern="wshot ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    urlissed = event.pattern_match.group(1)
    sedlyfstarky = await edit_or_reply(event, "Capturing Webshot, Stay Tuned.")
    driver = webdriver.Chrome()
    driver.get(urlissed)
    driver.get_screenshot_as_file("Webshot.png")
    imgpath = "Webshot.png"
    await sedlyfstarky.edit("Completed. Uploading in Telegram..")
    await borg.send_file(
        event.chat_id,
        file=imgpath,
        caption=f"**Webshot OF** `{urlissed}` \n**Powered By CɪᴘʜᴇʀX**",
    )


@friday.on(friday_on_cmd(pattern="lp ?(.*)"))
@friday.on(sudo_cmd(pattern="lp ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
        tfbro = await edit_or_reply(event, "Wait Fetching Website Info")
        gone = event.pattern_match.group(1)
        url = f"https://api.ip2whois.com/v1?key=free&domain=" + gone
        await event.edit(
            "Fecthing Website Info ! Stay Tuned. This may take some time ;)"
        )
        lol = iplookup.iplookup
        okthen = lol(gone)
        sed = requests.get(url=url).json()
        km = sed["registrant"]
        kek = sed["registrar"]
        sedlyf = (
            f'Domain Name => {sed["domain"]} \nCreated On => {sed["create_date"]} \nDomain ID => {sed["domain_id"]} \nHosted ON => {kek["url"]}'
            f'\nLast updated => {sed["update_date"]} \nExpiry Date => {sed["expire_date"]} \nDomain Age => {sed["domain_age"]}'
            f'\nOwner => {km["name"]} \nCountry => {km["country"]} \nState => {km["region"]}'
            f'\nPhone Number => {km["phone"]} \nDomain Ip => {okthen}'
        )
        await tfbro.edit(sedlyf)
    except Exception:
        await tfbro.edit(f"Something Went Wrong. Maybe Website Wrong.")


@friday.on(friday_on_cmd(pattern="bin ?(.*)"))
@friday.on(sudo_cmd(pattern="bin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
        tfsir = await edit_or_reply(event, "Wait Fetching Bin Info")
        kek = event.pattern_match.group(1)
        url = f"https://lookup.binlist.net/{kek}"
        midhunkm = requests.get(url=url).json()
        kekvro = midhunkm["country"]
        data_is = (
            f"<b><u>Bin</u></b> ➠ <code>{kek}</code> \n"
            f"<b><u>Type</u></b> ➠ <code>{midhunkm['type']}</code> \n"
            f"<b><u>Scheme</u></b> ➠ <code>{midhunkm['scheme']}</code> \n"
            f"<b><u>Brand</u></b> ➠ <code>{midhunkm['brand']}</code> \n"
            f"<b><u>Country</u></b> ➠ <code>{kekvro['name']} {kekvro['emoji']}</code> \n"
        )
        await tfsir.edit(data_is, parse_mode="HTML")
    except:
        await tfsir.edit("Not a Valid Bin or Don't Have Enough Info.")


@friday.on(friday_on_cmd(pattern="iban ?(.*)"))
@friday.on(sudo_cmd(pattern="iban ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    inputs = event.pattern_match.group(1)
    api = f"https://openiban.com/validate/{inputs}?getBIC=true&validateBankCode=true"
    lol = requests.get(url=api).json()
    try:
        tfhm = await edit_or_reply(event, "Wait Fetching IBAN Info")
        banks = lol["bankData"]
        kek = (
            f"<b><u>VALID</u></b> ➠ <code>{lol['valid']}</code> \n"
            f"<b><u>IBAN</u></b> ➠ <code>{lol['iban']}</code> \n"
            f"<b><u>BANK-CODE</u></b> ➠ <code>{banks['bankCode']}</code> \n"
            f"<b><u>BANK-NAME</u></b> ➠ <code>{banks['name']}</code> \n"
            f"<b><u>ZIP</u></b> ➠ <code>{banks['zip']}</code> \n"
            f"<b><u>CITY</u></b> ➠ <code>{banks['city']}</code> \n"
            f"<b><u>BIC</u></b> ➠ <code>{banks['bic']}</code> \n"
        )
        await tfhm.edit(kek, parse_mode="HTML")
    except:
        await tfhm.edit(f"Invalid IBAN or Doesn't Have Enough Info")


@friday.on(friday_on_cmd(pattern="gitdl ?(.*)"))
@friday.on(sudo_cmd(pattern="gitdl ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
        kekman = await edit_or_reply(event, "Fetching Repo")
        inputs = event.pattern_match.group(1)
        sed = event.pattern_match.group(1)
        if sed:
            if " " in sed:
                stark = inputs.split(" ", 2)
        gitusername = stark[0]
        gitrepo = stark[1]
        gitbranch = stark[2]
        link = f"https://github.com/{gitusername}/{gitrepo}/archive/{gitbranch}.zip"
        await kekman.edit("Uploading... Stark Tuned.")
        await event.delete()
        await borg.send_file(event.chat_id, file=link, caption="You Repo Achieve File.")
    except:
        await borg.send_message(
            event.chat_id, "**Usage** : `.gitdl <gitusername> <gitrepo> <gitbranch>`"
        )


@friday.on(friday_on_cmd(pattern="yts ?(.*)"))
@friday.on(sudo_cmd(pattern="yts ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
        fin = event.pattern_match.group(1)
        stark_result = await edit_or_reply(event, "Fectching Result this May Take Time")
        results = YoutubeSearch(f"{fin}", max_results=5).to_dict()
        noob = "<b>YOUTUBE SEARCH</b> \n\n"
        for moon in results:
            hmm = moon["id"]
            kek = f"https://www.youtube.com/watch?v={hmm}"
            stark_name = moon["title"]
            stark_chnnl = moon["channel"]
            total_stark = moon["duration"]
            stark_views = moon["views"]
            noob += (
                f"<b><u>VIDEO-TITLE</u></b> ➠ <code>{stark_name}</code> \n"
                f"<b><u>LINK</u></b> ➠ <code>{kek}</code> \n"
                f"<b><u>CHANNEL</u></b> ➠ <code>{stark_chnnl}</code> \n"
                f"<b><u>DURATION</u></b> ➠ <code>{total_stark}</code> \n"
                f"<b><u>TOTAL-VIEWS</u></b> ➠ <code>{stark_views}</code> \n\n"
            )
        await stark_result.edit(noob, parse_mode="HTML")
    except:
        await event.edit("Something went Wrong.")


@friday.on(friday_on_cmd(pattern="akd ?(.*)"))
@friday.on(sudo_cmd(pattern="akd ?(.*)", allow_sudo=True))
async def _(event):
    akkad = event.pattern_match.group(1)
    if event.fwd_from:
        return
    pathz, name = await apk_dl(akkad, Config.TMP_DOWNLOAD_DIRECTORY, event)
    await borg.send_file(event.chat_id, pathz, caption="Uploaded by CɪᴘʜᴇʀX Server")


CMD_HELP.update(
    {
        "webtools": "**Web Tools**\
\n\n**Syntax : **`.wshot <website URL>`\
\n**Usage :** takes screenshot of webpage.\
\n\n**Syntax : **`.lp <URL link>`\
\n**Usage :** Gives whois information about website.\
\n\n**Syntax : **`.bin <bin>`\
\n**Usage :** Provides information about bin.\
\n\n**Syntax : **`.iban <iban>`\
\n**Usage :** Provides information about IBAN.\
\n\n**Syntax : **`.gitdl <repository name>`\
\n**Usage :** Gets repository link.\
\n\n**Syntax : **`.yts <query>`\
\n**Usage :** searches the query on YouTube and give results.\
\n\n**Syntax : **`.akd <query>`\
\n**Usage :** Finds and uploads apk files."
    }
)
