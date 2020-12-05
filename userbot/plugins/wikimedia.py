"""WikiMedia.ORG
Syntax: .wikimedia Query"""
import requests
from uniborg.util import edit_or_reply, friday_on_cmd, sudo_cmd

from userbot import CMD_HELP


@friday.on(friday_on_cmd(pattern="wikimedia (.*)"))
@friday.on(sudo_cmd(pattern="wikimedia (.*)", allow_sudo=True))
async def _(event):
    wowsosmart = await edit_or_reply(event, "Wait Finding This Media")
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    url = "https://commons.wikimedia.org/w/api.php?action={}&generator={}&prop=imageinfo&gimlimit={}&redirects=1&titles={}&iiprop={}&format={}".format(
        "query",
        "images",
        "5",
        input_str,
        "timestamp|user|url|mime|thumbmime|mediatype",
        "json",
    )
    r = requests.get(url).json()
    result = ""
    results = r["query"]["pages"]
    for key in results:
        current_value = results[key]
        pageid = current_value["pageid"]
        title = current_value["title"]
        imageinfo = current_value["imageinfo"][0]
        timestamp = imageinfo["timestamp"]
        user = imageinfo["user"]
        descriptionurl = imageinfo["descriptionurl"]
        mime = imageinfo["mime"]
        mediatype = imageinfo["mediatype"]
        result += """\n
        pageid: {}
        title: {}
        timestamp: {}
        user: [{}]({})
        mime: {}
        mediatype: {}
        """.format(
            pageid, title, timestamp, user, descriptionurl, mime, mediatype
        )
    await wowsosmart.edit(
        "**Search**: {} \n\n **Results**: {}".format(input_str, result)
    )


CMD_HELP.update(
    {
        "wikimedia": "**Wikimedia**\
\n\n**Syntax : **`.wikimedia <query>`\
\n**Usage :** Searches for media from wikipedia with your query."
    }
)
