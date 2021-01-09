from anime_downloader.sites import get_anime_class

from userbot import CMD_HELP
from userbot.utils import admin_cmd


@friday.on(admin_cmd(pattern="anime (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    ommhg = await event.reply("Searching For Anime...")
    lmao = input_str.split(":", 1)
    try:
       site = lmao[1]
    except:
       site = "twist.moe"
       await event.reply("Please Provide Site Name From Next Time. Now Continuing With Default Site.")

    lol = lmao[0]
    why = site.lower()

    Twist = get_anime_class(why)
    try:
       search = Twist.search(lol)
    except:
       await ommhg.edit("Please Try Different Site. Given Site is Down.")

    title1 = search[0].title
    url1 = search[0].url
    title2 = search[1].title
    url2 = search[1].url
    title3 = search[2].title
    url3 = search[2].url
    title4 = search[3].title
    url4 = search[3].url
    title5 = search[4].title
    url5 = search[4].url

    await event.edit(
        f"<b><u>Anime Search Complete</b></u> \n\n\n<b>Title</b>:-  <code>{title1}</code> \n<b>URL Link</b>:- {url1}\n\n<b>Title</b>:-  <code>{title2}</code> \n<b>URL Link</b>:- {url2}\n\n<b>Title</b>:-  <code>{title3}</code>\n<b>URL Link</b>:- {url3}\n\n<b>Title</b>:-  <code>{title4}</code> \n<b>URL Link</b>:- {url4}\n\n<b>Title</b>:-  <code>{title5}</code> \n<b>URL Link</b>:- {url5}\n\n<b>Links Gathered by CɪᴘʜᴇʀX</b>",
        parse_mode="HTML",
    )
    await ommhg.delete()


CMD_HELP.update(
    {
        "anime": "**Anime**\
\n\n**Syntax : **`.anime <Amime Name:site Name>`\
\n**Usage :** Automatically Gets Streaming Link Of The Anime.\
\n**Example :** `.anime one piece:twist.moe`\
\n**Note** :** Get Site names list from [Here](https://devsexpoanime.netlify.app/)."
    }
)
