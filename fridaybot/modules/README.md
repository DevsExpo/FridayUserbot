## FRIDAY USERBOT
# EXAMPLE CODE !
```python3
from fridaybot.utils import friday_on_cmd, sudo_cmd, edit_or_reply
from fridaybot.Configs import Config
@friday.on(friday_on_cmd(pattern="alive"))
@friday.on(sudo_cmd(pattern="alive", allow_sudo=True))
async def hello_world(event):
    if event.fwd_from:
        return
    friday = await friday.edit_or_reply(event, "Finding My Controllers....")
    await friday.edit("**HELLO WORLD**\n\nThe following is controlling me too!\n" + Config.SUDO_USERS)
```
