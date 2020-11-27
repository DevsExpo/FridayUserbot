import asyncio
import os
from pathlib import Path

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd, load_module

DELETE_TIMEOUT = 5


@friday.on(friday_on_cmd(pattern="install"))
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        sedplugin = await event.get_reply_message()
        try:
            downloaded_file_name = await event.client.download_media(
                sedplugin,
                "fridaybot/modules/",
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await event.edit(
                    "Friday Has Installed `{}` Sucessfully.".format(
                        os.path.basename(downloaded_file_name)
                    )
                )
            else:
                os.remove(downloaded_file_name)
                await event.edit(
                    "Errors! This plugin is already installed/pre-installed."
                )
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(
                f"Error While Installing This Plugin, Please Make Sure That its py Extension. \n**ERROR :** {e}"
            )
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()


CMD_HELP.update(
    {
        "install": "**Install**\
\n\n**Syntax : **`.install <reply to plugin>`\
\n**Usage :** it installs replyed plugin"
    }
)
