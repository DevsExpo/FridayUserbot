from uniborg.util import friday_on_cmd
import requests
from userbot import CMD_HELP
from userbot.utils import admin_cmd
from userbot.Configs import Config




@friday.on(admin_cmd(pattern="gplink (.*)"))
async def _(event):
    if event.fwd_from:
        return
    if Config.GPLINKS_API_KEY is None:
        await event.edit(
            "Need to get an API key from https://gplinks.in\nModule stopping!"
        )
        return
    input_str = event.pattern_match.group(1)
    wtf = input_str.split(" ",1)
    ok = (wtf[0])
    no = (wtf[1])
    
    
    r = requests.get(f"https://gplinks.in/api?api={Config.GPLINKS_API_KEY}&url={ok}&alias={no}")
    
    kk = r.json()
    if kk.get("status")=="error":
	    ko = kk.get("message")
	    ok= ko [0]
	    hel = "Error, Reason:-  "+ok
    elif kk.get("status")=="success":
      
      pop = kk.get("shortenedUrl")
      
      hel = f"""
 
 Link Generated Successfully

Given Link:- {ok}

Shortened Link:- {pop}"""
    
    
    
    await borg.send_message(
        event.chat_id,
        hel,
        parse_mode="HTML"
    )
    
    await event.delete()


CMD_HELP.update(
    {
        "gplinks": "**GPLinks**\
\n\n**Syntax : **`.gplink <link to sshorten> <alias>`\
\n**Usage :** Shortens Given Link In GPlinks.\
\n\n**Example : **`.gplink google.com CipherX`\
\nThis above syntax gives:- https://go.gplinks.co/CipherX"
    }
)





    
