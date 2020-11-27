"""
for bot credits to @pureindialover
"""

from telethon.tl import functions

from fridaybot import CMD_HELP
from fridaybot.events import register


@register(outgoing=True, pattern="^.create (b|g|c)(?: |$)(.*)")
async def telegraphs(grop):

    """ For .create command, Creating New Group & Channel """

    if not grop.text[0].isalpha() and grop.text[0] not in ("/", "#", "@", "!"):

        if grop.fwd_from:

            return

        type_of_group = grop.pattern_match.group(1)

        group_name = grop.pattern_match.group(2)

        if type_of_group == "b":

            try:

                result = await grop.client(
                    functions.messages.CreateChatRequest(  # pylint:disable=E0602
                        users=["@meikobot"],
                        # Not enough users (to create a chat, for example)
                        # Telegram, no longer allows creating a chat with ourselves
                        title=group_name,
                    )
                )

                created_chat_id = result.chats[0].id

                await grop.client(
                    functions.messages.DeleteChatUserRequest(
                        chat_id=created_chat_id, user_id="@Serena_Robot"
                    )
                )

                result = await grop.client(
                    functions.messages.ExportChatInviteRequest(
                        peer=created_chat_id,
                    )
                )

                await grop.edit(
                    "Your `{}` Group Made Boss!. Join [{}]({})".format(
                        group_name, group_name, result.link
                    )
                )

            except Exception as e:  # pylint:disable=C0103,W0703

                await grop.edit(str(e))

        elif type_of_group == "g" or type_of_group == "c":

            try:

                r = await grop.client(
                    functions.channels.CreateChannelRequest(  # pylint:disable=E0602
                        title=group_name,
                        about="Welcome to this Channel boss",
                        megagroup=False if type_of_group == "c" else True,
                    )
                )

                created_chat_id = r.chats[0].id

                result = await grop.client(
                    functions.messages.ExportChatInviteRequest(
                        peer=created_chat_id,
                    )
                )

                await grop.edit(
                    "Your `{}` Group/Channel Has been made Boss!. Join [{}]({})".format(
                        group_name, group_name, result.link
                    )
                )

            except Exception as e:  # pylint:disable=C0103,W0703

                await grop.edit(str(e))


CMD_HELP.update(
    {
        "create": "**Create**\
\n\n**Syntax : **`.create g <group name>`\
\n**Usage :** Creates a private group with given name.\
\n\n**Syntax : **`.create b <group name>`\
\n**Usage :** Creates a private group with bot in it and given name.\
\n\n**Syntax : **`.create c <channel name>`\
\n**Usage :** Creates a channel with given name."
    }
)
