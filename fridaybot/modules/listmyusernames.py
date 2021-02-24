# For @UniBorg
# (c) Shrimadhav U K

from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from uniborg.util import friday_on_cmd

from fridaybot import CMD_HELP


@friday.on(friday_on_cmd("listmyusernames"))
async def mine(event):
    if event.fwd_from:
        return
    """ For .reserved command, get a list of your reserved usernames. """
    result = await bot(GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"{channel_obj.title}\n@{channel_obj.username}\n\n"
    await event.edit(output_str)


CMD_HELP.update(
    {
        "listmyusernames": "**Listmyusernames**\
\n\n**Syntax : **`.listmyusernames`\
\n**Usage :** it lists all your usernames you are holding"
    }
)
