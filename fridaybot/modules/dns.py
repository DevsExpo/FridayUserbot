"""DA.GD helpers in @UniBorg
Available Commands:
.isup URL
.dns google.com
.url <long url>
.unshort <short url>"""
import requests

from fridaybot.utils import edit_or_reply
from fridaybot.utils import friday_on_cmd
from fridaybot.utils import sudo_cmd


@friday.on(friday_on_cmd("dns (.*)"))
@friday.on(sudo_cmd("dns (.*)", allow_sudo=True))
async def _(event):
    starky = await edit_or_reply(event, "Processing.....")
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/dns/{}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await starky.edit("DNS records of {} are \n{}".format(input_str, response_api))
    else:
        await starky.edit("i can't seem to find {} on the internet".format(input_str))


@friday.on(friday_on_cmd("url (.*)"))
@friday.on(sudo_cmd("dns (.*)", allow_sudo=True))
async def _(event):
    starkxd = await edit_or_reply(event, "Processing....")
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await starkxd.edit("Generated {} for {}.".format(response_api, input_str))
    else:
        await starkxd.edit("something is wrong. please try again later.")


@friday.on(friday_on_cmd("unshort (.*)"))
async def _(event):
    sadness = await edit_or_reply(event, "Processing...")
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if not input_str.startswith("http"):
        input_str = "http://" + input_str
    r = requests.get(input_str, allow_redirects=False)
    if str(r.status_code).startswith("3"):
        await sadness.edit(
            "Input URL: {}\nReDirected URL: {}".format(input_str, r.headers["Location"])
        )
    else:
        await sadness.edit(
            "Input URL {} returned status_code {}".format(input_str, r.status_code)
        )
