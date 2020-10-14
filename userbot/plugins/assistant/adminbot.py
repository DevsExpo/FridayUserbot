import asyncio
import time
from asyncio import sleep
from datetime import datetime
from os import remove

import emoji
from googletrans import Translator
from telethon import Button
from telethon import custom
from telethon import events
from telethon.errors import BadRequestError
from telethon.errors import ChatAdminRequiredError
from telethon.errors import ImageProcessFailedError
from telethon.errors import PhotoCropSizeSmallError
from telethon.errors import UserAdminInvalidError
from telethon.errors.rpcerrorlist import MessageDeleteForbiddenError
from telethon.errors.rpcerrorlist import MessageTooLongError
from telethon.errors.rpcerrorlist import UserIdInvalidError
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.channels import EditPhotoRequest
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import Channel
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.types import Chat
from telethon.tl.types import ChatAdminRights
from telethon.tl.types import ChatBannedRights
from telethon.tl.types import MessageEntityMentionName
from telethon.tl.types import MessageMediaPhoto
from telethon.tl.types import User
from telethon.utils import get_display_name

from userbot import bot
from userbot import BOTLOG
from userbot import BOTLOG_CHATID
from userbot import CMD_HELP
from userbot import Lastupdate
from userbot.uniborgConfig import Config
from userbot.utils import admin_cmd
from userbot.utils import edit_or_reply
from userbot.utils import errors_handler
from userbot.utils import register
from userbot.utils import sudo_cmd

# =================== CONSTANT ===================
PP_TOO_SMOL = "`The image is too small`"
PP_ERROR = "`Failure while processing the image`"
NO_ADMIN = "`I am not an admin nub nibba!`"
NO_PERM = (
    "`I don't have sufficient permissions! This is so sed. Alexa play Tera Baap Aaya`"
)
NO_SQL = "`Running on Non-SQL mode!`"

CHAT_PP_CHANGED = "`Chat Picture Changed`"
CHAT_PP_ERROR = (
    "`Some issue with updating the pic,`"
    "`maybe coz I'm not an admin,`"
    "`or don't have enough rights.`"
)
INVALID_MEDIA = "`Invalid Extension`"

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

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)

UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)


@tgbot.on(events.NewMessage(pattern="^/bun(?: |$)(.*)"))
async def ban(event):
    noob = event.from_id
    userids = []
    async for user in tgbot.iter_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    ):
        userids.append(user.id)
    if noob not in userids:
        await event.reply("You're not an admin!")
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await event.reply("I Am Not Admin 🥺.")
        return

    user, reason = await get_user_from_event(event)
    if user:
        pass
    else:
        return
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS))
    except BadRequestError:
        await event.reply("No Permission Sar 🤭.")
        return
    # Helps ban group join spammers more easily
    try:
        reply = await event.get_reply_message()
        if reply:
            pass
    except BadRequestError:
        await event.reply(
            "`I dont have message nuking rights! But still he was banned!`"
        )
        return
    if reason:
        await event.reply(f"Banned `{str(user.id)}` \nReason: {reason}")
    else:
        await event.reply(f"Banned  `{str(user.id)}` !")


@tgbot.on(events.NewMessage(pattern="^/unbun(?: |$)(.*)"))
async def nothanos(event):
    userids = []
    noob = event.from_id
    async for user in tgbot.iter_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    ):
        userids.append(user.id)
    if noob not in userids:
        await event.reply("You're not an admin!")
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await event.reply("Me Not Admin 🥺")
        return
    user = await get_user_from_event(event)
    user = user[0]
    if user:
        pass
    else:
        return
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS))
        await event.reply("`Unbanned Successfully. Granting another chance.🚶`")
    except BadRequestError:
        await event.reply("`No Permission 🤭`")
        return


@tgbot.on(events.NewMessage(pattern="^/prumote(?: |$)(.*)"))
async def promote(event):
    userids = []
    noob = event.from_id
    async for user in tgbot.iter_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    ):
        userids.append(user.id)
    if noob not in userids:
        await event.reply("You're not an admin!")
        return
    """ For .promote command, promotes the replied/tagged person """
    # Get targeted chat
    chat = await event.get_chat()
    # Grab admin status or creator in a chat
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, also return
    if not admin and not creator:
        await event.reply("Me Not Admin 🥺")
        return
    new_rights = ChatAdminRights(
        add_admins=False,
        invite_users=False,
        change_info=False,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
    )
    user, rank = await get_user_from_event(event)
    if not rank:
        rank = "mememaster"  # Just in case.
    if user:
        pass
    else:
        return
    # Try to promote if current user is admin or creator
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, new_rights, rank))
        await event.reply("`Promoted Successfully! Now gib Party`")

    # If Telethon spit BadRequestError, assume
    # we don't have Promote permission
    except BadRequestError:
        await event.reply("No Permission To Promote 🤭")
        return


@tgbot.on(events.NewMessage(pattern="^/demute(?: |$)(.*)"))
async def demote(event):
    userids = []
    noob = event.from_id
    async for user in tgbot.iter_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    ):
        userids.append(user.id)
    if noob not in userids:
        await event.reply("You're not an admin!")
        return
    """ For .demote command, demotes the replied/tagged person """
    # Admin right check
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await event.reply("I Am Not Admin 🤭")
        return

    rank = "mememaster"  # dummy rank, lol.
    user = await get_user_from_event(event)
    user = user[0]
    if user:
        pass
    else:
        return

    newrights = ChatAdminRights(
        add_admins=None,
        invite_users=None,
        change_info=None,
        ban_users=None,
        delete_messages=None,
        pin_messages=None,
    )
    # Edit Admin Permission
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, newrights, rank))

    # If we catch BadRequestError from Telethon
    # Assume we don't have permission to demote
    except BadRequestError:
        await event.reply("Me No Permission 🤔")
        return
    await event.reply("`Demoted this retard Successfully!`")


@tgbot.on(events.NewMessage(pattern="^/pin(?: |$)(.*)"))
async def pin(event):
    userids = []
    noob = event.from_id
    async for user in tgbot.iter_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    ):
        userids.append(user.id)
    if noob not in userids:
        await event.reply("You're not an admin!")
        return
    """ For .pin command, pins the replied/tagged message on the top the chat. """
    # Admin or creator check
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        await event.reply("I Need Administration Permission 🤔")
        return

    to_pin = event.reply_to_msg_id

    if not to_pin:
        await event.reply("`Reply to a message to pin it.`")
        return

    options = event.pattern_match.group(1)
    is_silent = True
    if options.lower() == "loud":
        is_silent = False
    try:
        await event.client(UpdatePinnedMessageRequest(event.to_id, to_pin, is_silent))
    except BadRequestError:
        await event.reply("No Permission 🥺")
        return
    await event.reply("`Pinned Successfully!`")
    user = await get_user_from_id(msg.from_id, msg)


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif args:
        user = args[0]
        if len(args) == 2:
            extra = args[1]

        if user.isnumeric():
            user = int(user)

        if not user:
            await event.reply("`Pass the user's username, id or reply!`")
            return

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None

    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)

    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None

    return user_obj
