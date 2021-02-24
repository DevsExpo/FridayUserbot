import asyncio
from datetime import datetime
import os
from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd, sudo_cmd

fridaythumb = "./resources/IMG_20200929_103719_628.jpg"


@friday.on(friday_on_cmd(pattern="send ?(.*)"))
@friday.on(sudo_cmd(pattern="send ?(.*)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    if input_str.endswith(".py"):
        the_plugin_file = "./fridaybot/modules/{}".format(input_str)
    else:
        the_plugin_file = "./fridaybot/modules/{}.py".format(input_str)
    end = datetime.now()
    (end - start).seconds
    men = f"**Plugin Name :** `{input_str}` \n**This Plugin is Part Of Friday, Please Read License Before Using In Your Projects.**"
    if not os.path.exists(the_plugin_file):
        await event.edit(f"__No Plugin Match Found For__ **{input_str}**")
        return
    await event.client.send_file(  # pylint:disable=E0602
        event.chat_id,
        the_plugin_file,
        thumb=fridaythumb,
        caption=men,
        force_document=True,
        allow_cache=False,
        reply_to=message_id,
    )
    await asyncio.sleep(5)
    await event.delete()


CMD_HELP.update(
    {
        "send": "**Send**\
\n\n**Syntax : **`.send <plugin name>`\
\n**Usage :** sends the plugin."
    }
)
