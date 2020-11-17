import asyncio
from asyncio import sleep

from telethon.errors import ChatAdminRequiredError
from telethon.errors import UserAdminInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd
from fridaybot.utils import sudo_cmd

#
BOTLOG = True
BOTLOG_CHATID = Config.PRIVATE_GROUP_ID

# =================== CONSTANT ===================

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)


UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)


@friday.on(friday_on_cmd(pattern=f"zombies ?(.*)"))
async def rm_deletedacc(show):
    """ For .zombies command, list all the zombies in a chat. """

    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "`No Deleted Accounts Found, Group Is Clean`"

    if con != "clean":
        await show.edit("`Searching For Zombies...`")
        async for user in show.client.iter_participants(show.chat_id):

            if user.deleted:
                del_u += 1
                await sleep(1)
        if del_u > 0:
            del_status = f"Found **{del_u}** Zombies In This Group.\
            \nClean Them By Using `.zombies clean`"
        await show.edit(del_status)
        return

    # Here laying the sanity check
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        await show.edit("`I Am Not An Admin Here!`")
        return

    await show.edit("`Killing Zombies...`")
    del_u = 0
    del_a = 0

    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client(
                    EditBannedRequest(show.chat_id, user.id, BANNED_RIGHTS)
                )
            except ChatAdminRequiredError:
                await show.edit("`I Don't Have Ban Rights In This Group`")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await show.client(EditBannedRequest(show.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1

    if del_u > 0:
        del_status = f"**Killed** `{del_u}` **Zombies**"

    if del_a > 0:
        del_status = f"**Killed** `{del_u}` **Zombies** \
        \n`{del_a}` Zombie Admin Accounts Are Not Removed!"

    await show.edit(del_status)
    await sleep(2)
    await show.delete()

    if BOTLOG:
        await show.client.send_message(
            BOTLOG_CHATID,
            "#CLEANUP\n"
            f"Cleaned **{del_u}** Zombies!!\
            \nCHAT: {show.chat.title}(`{show.chat_id}`)",
        )
