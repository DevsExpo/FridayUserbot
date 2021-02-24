from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from fridaybot import CMD_HELP
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd
import json
from fridaybot import CMD_HELP
import requests

@friday.on(friday_on_cmd(pattern="bible ?(.*)"))
@friday.on(sudo_cmd(pattern="bible ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str is None:
      await friday.edit_or_reply(event, "Input Not Found. 🤦")
    try:
      Hitler = input_str.split(":",2)
      book = (Hitler[0])
      cr = (Hitler[1])
      ve = (Hitler[2])
    except:
      await friday.edit_or_reply(event, "Input Not Proper. Give Input in the form of `.bible bookName:chapter:verse` ")
    try:
      url = f"https://bible-api.com/{book.strip()}+{cr.strip()}:{ve.strip()}"
    
      pablo = requests.get(url).json()
    
      ref = pablo.get("reference")
      mnmm = pablo.get("verses")
      mnm = mnmm[0]

      bd = mnm.get("book_id")

      bn = mnm.get("book_name")

      chapter = mnm.get("chapter")

      verse = mnm.get("verse")

      texr = mnm.get("text")

      Escobar = f"""<u><b>Bible Information Gathered</b></u>
<b><u>Book Name</u> : {bn}
<u>Book ID</u> : {bd}
<u>Chapter</u> : {chapter}
<u>Verse</u> : {verse}
<u>Reference</u> : {ref}
<u>Text</u> : {texr.strip()}


<u>By Friday bot.
Get Your Fridaybot From @FRIDAYOT</u></b>
"""
      await borg.send_message(
        event.chat_id,
        Escobar,
        parse_mode="HTML",
        silent=True,
      )
    
    except:
      await friday.edit_or_reply(event, "Given Text is Invalid. 🤦")
    




CMD_HELP.update(
    {
        "bible": "**Bible**\
\n\n**Syntax : **`.bible bookName:chapter:verse`\
\n**Usage :** Gives verse from bible.\
\n\n**Example : **`.bible John:5:2`\
\nThis above syntax gives 2nd verse From 5th chapter from John book."
    }
)
