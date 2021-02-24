# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
"""
Userbot module to help you manage a group
"""

from asyncio import sleep

from telethon import events
from telethon.utils import pack_bot_file_id
from fridaybot.utils import friday_on_cmd, edit_or_reply, sudo_cmd
from fridaybot import CMD_HELP
from fridaybot.modules.sql_helper.welcome_sql import (
    add_welcome_setting,
    get_current_welcome_settings,
    rm_welcome_setting,
    update_previous_welcome,
)
from os import remove
from telethon.tl import functions
from fridaybot.function import is_admin
from telethon.errors import (
    BadRequestError,
    ChatAdminRequiredError,
    ImageProcessFailedError,
    PhotoCropSizeSmallError,
    UserAdminInvalidError,
)
from telethon.tl.types import (
    ChannelParticipantAdmin,
    ChannelParticipantCreator,
    ChannelParticipantsAdmins,
)
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantsBots
from telethon.tl.types import ChannelParticipantsAdmins
from fridaybot.modules.sql_helper import warns_sql as sql
from telethon.errors.rpcerrorlist import MessageTooLongError, UserIdInvalidError
from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditBannedRequest,
    EditPhotoRequest,
)
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChatAdminRights,
    ChatBannedRights,
    MessageEntityMentionName,
    MessageMediaPhoto,
)

from fridaybot import BOTLOG, BOTLOG_CHATID, CMD_HELP
import asyncio
import re
from fridaybot import CMD_HELP
from fridaybot.modules.sql_helper.filter_sql import (
    add_filter,
    get_all_filters,
    remove_all_filters,
    remove_filter,
)
from telethon import events, utils
from telethon.tl import types
from fridaybot.modules.sql_helper.snips_sql import (
    add_snip,
    get_all_snips,
    get_snips,
    remove_snip,
)

DELETE_TIMEOUT = 0
TYPE_TEXT = 0
TYPE_PHOTO = 1
TYPE_DOCUMENT = 2


global last_triggered_filters
last_triggered_filters = {}

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
# ================================================



# ------------------------------------------------------------------------------------
async def get_user_from_event(event):
    args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif args:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the User's Username, ID or Reply!`")
            return None, None
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj, extra
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError):
            return None, None
    return user_obj, extra


async def get_user_sender_id(user, event):
    if isinstance(user, str):
        user = int(user)

    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None

    return user_obj
# --------------------------------------------------------------------------------------------


# @register(outgoing=True, pattern="^.setevent$")
@friday.on(friday_on_cmd(pattern="setgpic$"))
@friday.on(sudo_cmd(pattern="setgpic$", allow_sudo=True))
async def set_group_photo(event):
    if event.fwd_from:
        return
    """ For .setevent command, changes the picture of a group """
    if not event.is_group:
        poppo = await friday.edit_or_reply(event, "`I don't think this is a group.`")
        return
    replyevent = await event.get_reply_message()
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    photo = None
    if not admin and not creator:
        poppo = await friday.edit_or_reply(event, NO_ADMIN)
        return
    if replyevent and replyevent.media:
        if isinstance(replyevent.media, MessageMediaPhoto):
            photo = await event.client.download_media(message=replyevent.photo)
        elif "image" in replyevent.media.document.mime_type.split("/"):
            photo = await event.client.download_file(replyevent.media.document)
        else:
            poppo = await friday.edit_or_reply(event, INVALID_MEDIA)

    if photo:
        try:
            await event.client(
                EditPhotoRequest(event.chat_id, await event.client.upload_file(photo))
            )
            poppo = await friday.edit_or_reply(event, CHAT_PP_CHANGED)

        except PhotoCropSizeSmallError:
            poppo = await friday.edit_or_reply(event, PP_TOO_SMOL)
        except ImageProcessFailedError:
            poppo = await friday.edit_or_reply(event, PP_ERROR)


# @register(outgoing=True, pattern="^.promote(?: |$)(.*)")
@friday.on(friday_on_cmd(pattern="promote(?: |$)(.*)"))
@friday.on(sudo_cmd(pattern="promote(?: |$)(.*)", allow_sudo=True))
async def promote(event):
    if event.fwd_from:
        return
    if not event.is_group:
        poppo = await friday.edit_or_reply(event, "`I don't think this is a group.`")
        return
    """ For .promote command, promotes the replied/tagged person """
    # Get targeted chat
    chat = await event.get_chat()
    # Grab admin status or creator in a chat
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, also return
    if not admin and not creator:
        poppo = await friday.edit_or_reply(event, NO_ADMIN)
        return

    new_rights = ChatAdminRights(
        add_admins=False,
        invite_users=True,
        change_info=False,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
    )

    poppo = await friday.edit_or_reply(event, "`Promoting...`")
    user, rank = await get_user_from_event(event)
    if not rank:
        rank = "admeme"  # Just in case.
    if user:
        pass
    else:
        return

    # Try to promote if current user is admin or creator
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, new_rights, rank))
        await poppo.edit(f"Sucessfully, Promoted [{user.first_name}](tg://user?id={user.id}) in {event.chat.title}")

    # If Telethon spit BadRequestError, assume
    # we don't have Promote permission
    except BadRequestError:
        await poppo.edit(NO_PERM)
        return
    # Announce to the logging group if we have promoted successfully
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#PROMOTE\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {event.chat.title}(`{event.chat_id}`)",
        )


# @register(outgoing=True, pattern="^.demote(?: |$)(.*)")
@friday.on(friday_on_cmd(pattern="demote(?: |$)(.*)"))
@friday.on(sudo_cmd(pattern="demote(?: |$)(.*)", allow_sudo=True))
async def demote(event):
    if event.fwd_from:
        return
    if not event.is_group:
        poppo = await friday.edit_or_reply(event, "`I don't think this is a group.`")
        return
    """ For .demote command, demotes the replied/tagged person """
    # Admin right check
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        poppo = await friday.edit_or_reply(event, NO_ADMIN)
        return

    # If passing, declare that we're going to demote
    poppo = await friday.edit_or_reply(event, "`Demoting...`")
    rank = "admeme"  # dummy rank, lol.
    user, reason = await get_user_from_event(event)
    if user:
        pass
    else:
        return
    # New rights after demotion
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
        popp9 = await friday.edit_or_reply(event, NO_PERM)
        return
    await poppo.edit(f"Demoted, [{user.first_name}](tg://user?id={user.id}) in {event.chat.title} Sucessfully!")

    # Announce to the logging group if we have demoted successfully
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#DEMOTE\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {event.chat.title}(`{event.chat_id}`)",
        )


# @register(outgoing=True, pattern="^.ban(?: |$)(.*)")
@friday.on(friday_on_cmd(pattern="ban(?: |$)(.*)"))
@friday.on(sudo_cmd(pattern="ban(?: |$)(.*)", allow_sudo=True))
async def ban(event):
    if event.fwd_from:
        return
    if not event.is_group:
        poppo = await friday.edit_or_reply(event, "`I don't think this is a group.`")
        return
    """ For .ban command, bans the replied/tagged person """
    # Here laying the sanity check
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        poppo = await friday.edit_or_reply(event, NO_ADMIN)
        return

    user, reason = await get_user_from_event(event)
    if user:
        pass
    else:
        return

    # Announce that we're going to whack the pest
    poppo = await friday.edit_or_reply(event, "`Dusting Dust of ban Hammer`")

    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS))
    except BadRequestError:
        await poppo.edit(NO_PERM)
        return
    # Helps ban group join spammers more easily
    try:
        reply = await event.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        poppio = await friday.edit_or_reply(event, "`I dont have message nuking rights! But still he was banned!`")
        return
    # Delete message and then tell that the command
    # is done gracefully
    # Shout out the ID, so that fedadmins can fban later
    if reason:
        await poppo.edit(f"Sucessfully, Banned [{user.first_name}](tg://user?id={user.id}) in {event.chat.title} For Reason: {reason}")
    else:
        await poppo.edit(f"Sucessfully, Banned [{user.first_name}](tg://user?id={user.id}) in {event.chat.title}")
    # Announce to the logging group if we have banned the person
    # successfully!
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#BAN\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {event.chat.title}(`{event.chat_id}`)",
        )


# @register(outgoing=True, pattern="^.unban(?: |$)(.*)")
@friday.on(friday_on_cmd(pattern="unban(?: |$)(.*)"))
@friday.on(sudo_cmd(pattern="unban(?: |$)(.*)", allow_sudo=True))
async def nothanos(event):
    if event.fwd_from:
        return
    if not event.is_group:
        poppo = await friday.edit_or_reply(event, "`I don't think this is a group.`")
        return
    """ For .unban command, unbans the replied/tagged person """
    # Here laying the sanity check
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        poppo = await friday.edit_or_reply(event, NO_ADMIN)
        return

    # If everything goes well...
    poppo = await friday.edit_or_reply(event, "`Unbanning...`")

    user = await get_user_from_event(event)
    user = user[0]
    if user:
        pass
    else:
        return

    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS))
        await poppo.edit(f"Sucessfully, UnBanned, [{user.first_name}](tg://user?id={user.id}) in {event.chat.title}")

        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#UNBAN\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {event.chat.title}(`{event.chat_id}`)",
            )
    except UserIdInvalidError:
        await poppo.edit("`Uh oh my unban logic broke!`")


@friday.on(friday_on_cmd(pattern=r"mute(?: |$)(.*)"))
async def spider(event):
    if event.fwd_from:
        return
    if not event.is_group:
        poppo = await friday.edit_or_reply(event, "`I don't think this is a group.`")
        return
    """
    This function is basically muting peeps
    """
    # Check if the function running under SQL mode
    try:
        from userbot.modules.sql_helper.spam_mute_sql import mute
    except AttributeError:
        poppo = await friday.edit_or_reply(event, NO_SQL)
        return

    # Admin or creator check
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        poppo = await friday.edit_or_reply(event, NO_ADMIN)
        return

    user, reason = await get_user_from_event(event)
    if user:
        pass
    else:
        return

    self_user = await event.client.get_me()

    if user.id == self_user.id:
        poppo = await friday.edit_or_reply(event, "`Hands too short, can't duct tape myself...\n(ヘ･_･)ヘ┳━┳`")
        return

    # If everything goes well, do announcing and mute
    poppo = await friday.edit_or_reply(event, "`Gets a tape!`")
    if mute(event.chat_id, user.id) is False:
        return await poppo.edit("`Error! User probably already muted.`")
    else:
        try:
            await event.client(EditBannedRequest(event.chat_id, user.id, MUTE_RIGHTS))

            # Announce that the function is done
            if reason:
                await poppo.edit(f"`Safely taped !!`\nReason: {reason}")
            else:
                await poppo.edit("`Safely taped !!`")

            # Announce to logging group
            if BOTLOG:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "#MUTE\n"
                    f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                    f"CHAT: {event.chat.title}(`{event.chat_id}`)",
                )
        except UserIdInvalidError:
            return await event.edit("`Uh oh my mute logic broke!`")


# @register(outgoing=True, pattern="^.unmute(?: |$)(.*)")
@friday.on(friday_on_cmd(pattern="unmute(?: |$)(.*)"))
@friday.on(sudo_cmd(pattern="unmute(?: |$)(.*)", allow_sudo=True))
async def unmoot(event):
    if event.fwd_from:
        return
    if not event.is_group:
        poppo = await friday.edit_or_reply(event, "`I don't think this is a group.`")
        return
    """ For .unmute command, unmute the replied/tagged person """
    # Admin or creator check
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        poppo = await friday.edit_or_reply(event, NO_ADMIN)
        return

    # Check if the function running under SQL mode
    try:
        from userbot.modules.sql_helper.spam_mute_sql import unmute
    except AttributeError:
        poppo = await friday.edit_or_reply(event, NO_SQL)
        return

    # If admin or creator, inform the user and start unmuting
    poppo = await friday.edit_or_reply(event, "```Unmuting...```")
    user = await get_user_from_event(event)
    user = user[0]
    if user:
        pass
    else:
        return

    if unmute(event.chat_id, user.id) is False:
        return await poppo.edit("`Error! User probably already unmuted.`")
    else:

        try:
            await event.client(EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS))
            await poppo.edit("```Unmuted Successfully```")
        except UserIdInvalidError:
            await poppo.edit("`Uh oh my unmute logic broke!`")
            return

        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#UNMUTE\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {event.chat.title}(`{event.chat_id}`)",
            )


# @register(outgoing=True, pattern="^.adminlist$")
@friday.on(friday_on_cmd(pattern="adminlist$"))
@friday.on(sudo_cmd(pattern="adminlist$", allow_sudo=True))
async def get_admin(event):
    if event.fwd_from:
        return
    if not event.is_group:
        poppo = await friday.edit_or_reply(event, "`I don't think this is a group.`")
        return
    """ For .admins command, list all of the admins of the chat. """
    poppo = await friday.edit_or_reply(event, "processing...")
    info = await event.client.get_entity(event.chat_id)
    title = info.title if info.title else "this chat"
    mentions = f"<b>Admins in {title}:</b> \n"
    try:
        async for user in event.client.iter_participants(
            event.chat_id, filter=ChannelParticipantsAdmins
        ):
            if not user.deleted:
                link = f'<a href="tg://user?id={user.id}">{user.first_name}</a>'
                userid = f"<code>{user.id}</code>"
                mentions += f"\n{link} {userid}"
            else:
                mentions += f"\nDeleted Account <code>{user.id}</code>"
    except ChatAdminRequiredError as err:
        mentions += " " + str(err) + "\n"
    await poppo.edit(mentions, parse_mode="html")


# @register(outgoing=True, pattern="^.pin(?: |$)(.*)")
@friday.on(friday_on_cmd(pattern="pin(?: |$)(.*)"))
@friday.on(sudo_cmd(pattern="pin(?: |$)(.*)", allow_sudo=True))
async def pin(event):
    if event.fwd_from:
        return
    """ For .pin command, pins the replied/tagged message on the top the chat. """
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    # If not admin and not creator, return
    if not admin and not creator:
        poppo = await friday.edit_or_reply(event, NO_ADMIN)
        return
    to_pin = event.reply_to_msg_id

    if not to_pin:
        poppo = await friday.edit_or_reply(event, "`Reply to a message to pin it.`")
        return

    options = event.pattern_match.group(1)

    is_silent = True

    if options.lower() == "loud":
        is_silent = False

    try:
        await event.client(UpdatePinnedMessageRequest(event.to_id, to_pin, is_silent))
    except BadRequestError:
        poppo = await friday.edit_or_reply(event, NO_PERM)
        return
    h = str(event.chat_id).replace("-100", "")
    poppo = await friday.edit_or_reply(event, f"I Have Pinned This [Message](http://t.me/c/{h}/{to_pin})")
    user = await get_user_sender_id(event.sender_id, event)

    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#PIN\n"
            f"ADMIN: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {event.chat.title}(`{event.chat_id}`)\n"
            f"LOUD: {not is_silent}",
        )


# @register(outgoing=True, pattern="^.kick(?: |$)(.*)")
@friday.on(friday_on_cmd(pattern="kick(?: |$)(.*)"))
@friday.on(sudo_cmd(pattern="kick(?: |$)(.*)", allow_sudo=True))
async def kick(event):
    if event.fwd_from:
        return
    if not event.is_group:
        poppo = await friday.edit_or_reply(event, "`I don't think this is a group.`")
        return
    """ For .kick command, kicks the replied/tagged person from the group. """
    # Admin or creator check
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        poppo = await friday.edit_or_reply(event, NO_ADMIN)
        return

    user, reason = await get_user_from_event(event)
    if not user:
        poppo = await friday.edit_or_reply(event, "`Couldn't fetch user.`")
        return

    poppo = await friday.edit_or_reply(event, "`Kicking...`")

    try:
        await event.client.kick_participant(event.chat_id, user.id)
        await sleep(0.5)
    except Exception as e:
        await poppo.edit(NO_PERM + f"\n{str(e)}")
        return

    if reason:
        await poppo.edit(
            f"I Have Kicked [{user.first_name}](tg://user?id={user.id}) from {event.chat.title} For Reason : {reason}"
        )
    else:
        await poppo.edit(f"Kicked [{user.first_name}](tg://user?id={user.id}) from {event.chat.title}")

    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#KICK\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {event.chat.title}(`{event.chat_id}`)\n",
        )


# @register(outgoing=True, pattern="^.users ?(.*)")
@friday.on(friday_on_cmd(pattern="users ?(.*)"))
@friday.on(sudo_cmd(pattern="users ?(.*)", allow_sudo=True))
async def get_users(event):
    if event.fwd_from:
        return
    if not event.is_group:
        poppo = await friday.edit_or_reply(event, "`I don't think this is a group.`")
        return
    """ For .users command, list all of the users in a chat. """
    info = await event.client.get_entity(event.chat_id)
    title = info.title if info.title else "this chat"
    mentions = "Users in {}: \n".format(title)
    try:
        if not event.pattern_match.group(1):
            async for user in event.client.iter_participants(event.chat_id):
                if not user.deleted:
                    mentions += (
                        f"\n[{user.first_name}](tg://user?id={user.id}) `{user.id}`"
                    )
                else:
                    mentions += f"\nDeleted Account `{user.id}`"
        else:
            searchq = event.pattern_match.group(1)
            async for user in event.client.iter_participants(
                event.chat_id, search=f"{searchq}"
            ):
                if not user.deleted:
                    mentions += (
                        f"\n[{user.first_name}](tg://user?id={user.id}) `{user.id}`"
                    )
                else:
                    mentions += f"\nDeleted Account `{user.id}`"
    except ChatAdminRequiredError as err:
        mentions += " " + str(err) + "\n"
    try:
        poppo = await friday.edit_or_reply(event, mentions)
    except MessageTooLongError:
        poppo = await friday.edit_or_reply(event, "Damn, this is a huge group. Uploading users lists as file.")
        file = open("userslist.txt", "w+")
        file.write(mentions)
        file.close()
        await event.client.send_file(
            event.chat_id,
            "userslist.txt",
            caption="Users in {}".format(title),
            reply_to=event.id,
        )
        remove("userslist.txt")

@friday.on(friday_on_cmd(pattern="zombies(?: |$)(.*)"))
@friday.on(sudo_cmd(pattern="zombies(?: |$)(.*)", allow_sudo=True))
async def rm_deletedacc(event):
    if event.fwd_from:
        return
    if not event.is_group:
        poppo = await friday.edit_or_reply(event, "`I don't think this is a group.`")
        return
    con = event.pattern_match.group(1).lower()
    del_u = 0
    del_status = "`No deleted accounts found, Group is clean`"
    if con != "clean":
        poppo = await friday.edit_or_reply(event, "`Searching for ghost/deleted/zombie accounts...`")
        async for user in event.client.iter_participants(event.chat_id):

            if user.deleted:
                del_u += 1
                await sleep(1)
        if del_u > 0:
            del_status = f"Found **{del_u}** ghost/deleted/zombie account(s) in this group,\
            \nclean them by using `.zombies clean`"

        poppo = await friday.edit_or_reply(event, del_status)
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        poppo = await friday.edit_or_reply(event, "`I am not an admin here!`")
        return
    poppo = await friday.edit_or_reply(event, "`Deleting deleted accounts...\nOh I can do that?!?!`")
    del_u = 0
    del_a = 0
    async for user in event.client.iter_participants(event.chat_id):
        if user.deleted:
            try:
                await poppo.client(
                    EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS)
                )
            except ChatAdminRequiredError:
                await poppo.edit("`I don't have ban rights in this group`")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await event.client(EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1
    if del_u > 0:
        del_status = f"Cleaned **{del_u}** deleted account(s)"
    if del_a > 0:
        del_status = f"Cleaned **{del_u}** deleted account(s) \
        \n**{del_a}** deleted admin accounts are not removed"

    await poppo.edit(del_status)
    await sleep(2)
    await poppo.delete()


@command(incoming=True)
async def on_snip(event):
    global last_triggered_filters
    name = event.raw_text
    if event.chat_id in last_triggered_filters:
        if name in last_triggered_filters[event.chat_id]:
            return False
        
    snips = get_all_filters(event.chat_id)
    if snips:
        for snip in snips:
            pattern = r"( |^|[^\w])" + re.escape(snip.keyword) + r"( |$|[^\w])"
            if re.search(pattern, name, flags=re.IGNORECASE):
                if snip.snip_type == TYPE_PHOTO:
                    media = types.InputPhoto(
                        int(snip.media_id),
                        int(snip.media_access_hash),
                        snip.media_file_reference,
                    )
                elif snip.snip_type == TYPE_DOCUMENT:
                    media = types.InputDocument(
                        int(snip.media_id),
                        int(snip.media_access_hash),
                        snip.media_file_reference,
                    )
                else:
                    media = None
                event.message.id
                if event.reply_to_msg_id:
                    event.reply_to_msg_id
                await event.reply(snip.reply, file=media)
                if event.chat_id not in last_triggered_filters:
                    last_triggered_filters[event.chat_id] = []
                last_triggered_filters[event.chat_id].append(name)
                await asyncio.sleep(DELETE_TIMEOUT)
                last_triggered_filters[event.chat_id].remove(name)


@friday.on(friday_on_cmd(pattern="filter (.*)"))
@friday.on(sudo_cmd(pattern="filter (.*)", allow_sudo=True))
async def on_snip_save(event):
    if event.fwd_from:
        return
    hitler = await friday.edit_or_reply(event, "Processing....")
    name = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if msg:
        snip = {"type": TYPE_TEXT, "text": msg.message or ""}
        if msg.media:
            media = None
            if isinstance(msg.media, types.MessageMediaPhoto):
                media = utils.get_input_photo(msg.media.photo)
                snip["type"] = TYPE_PHOTO
            elif isinstance(msg.media, types.MessageMediaDocument):
                media = utils.get_input_document(msg.media.document)
                snip["type"] = TYPE_DOCUMENT
            if media:
                snip["id"] = media.id
                snip["hash"] = media.access_hash
                snip["fr"] = media.file_reference
        add_filter(
            event.chat_id,
            name,
            snip["text"],
            snip["type"],
            snip.get("id"),
            snip.get("hash"),
            snip.get("fr"),
        )
        await hitler.edit(f"filter {name} saved successfully. Get it with {name}")
    else:
        await hitler.edit(
            "Reply to a message with `savefilter keyword` to save the filter"
        )


@friday.on(friday_on_cmd(pattern="filters$"))
@friday.on(sudo_cmd(pattern="filters$", allow_sudo=True))
async def on_snip_list(event):
    if event.fwd_from:
        return
    indiaislove = await friday.edit_or_reply(event, "Processing....")
    all_snips = get_all_filters(event.chat_id)
    OUT_STR = "Available Filters in the Current Chat:\n"
    if len(all_snips) > 0:
        for a_snip in all_snips:
            OUT_STR += f"👉 {a_snip.keyword} \n"
    else:
        OUT_STR = "No Filters. Start Saving using `.filter`"
    if len(OUT_STR) > 4096:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "filters.text"
            await bot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="Available Filters in the Current Chat",
                reply_to=event,
            )
            await event.delete()
    else:
        await indiaislove.edit(OUT_STR)


@friday.on(friday_on_cmd(pattern="stop (.*)"))
@friday.on(sudo_cmd(pattern="stop (.*)", allow_sudo=True))
async def on_snip_delete(event):
    if event.fwd_from:
        return
    iloveindia = await friday.edit_or_reply(event, "Processing...")
    name = event.pattern_match.group(1)
    remove_filter(event.chat_id, name)
    await iloveindia.edit(f"filter {name} deleted successfully")


@friday.on(friday_on_cmd(pattern="rmfilters$"))
@friday.on(sudo_cmd(pattern="rmfilters$", allow_sudo=True))
async def on_all_snip_delete(event):
    if event.fwd_from:
        return
    edit_or_reply(event, "Processing....")
    remove_all_filters(event.chat_id)
    await event.edit(f"filters **in current chat** deleted successfully")
    
@friday.on(events.NewMessage(pattern=r"\#(\S+)", outgoing=True))
async def on_snip(event):
    name = event.pattern_match.group(1)
    snip = get_snips(name)
    if snip:
        if snip.snip_type == TYPE_PHOTO:
            media = types.InputPhoto(
                int(snip.media_id),
                int(snip.media_access_hash),
                snip.media_file_reference,
            )
        elif snip.snip_type == TYPE_DOCUMENT:
            media = types.InputDocument(
                int(snip.media_id),
                int(snip.media_access_hash),
                snip.media_file_reference,
            )
        else:
            media = None
        message_id = event.message.id
        if event.reply_to_msg_id:
            message_id = event.reply_to_msg_id
        await borg.send_message(
            event.chat_id, snip.reply, reply_to=message_id, file=media
        )
        await event.delete()


@friday.on(friday_on_cmd("snips (.*)"))
async def on_snip_save(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if msg:
        snip = {"type": TYPE_TEXT, "text": msg.message or ""}
        if msg.media:
            media = None
            if isinstance(msg.media, types.MessageMediaPhoto):
                media = utils.get_input_photo(msg.media.photo)
                snip["type"] = TYPE_PHOTO
            elif isinstance(msg.media, types.MessageMediaDocument):
                media = utils.get_input_document(msg.media.document)
                snip["type"] = TYPE_DOCUMENT
            if media:
                snip["id"] = media.id
                snip["hash"] = media.access_hash
                snip["fr"] = media.file_reference
        add_snip(
            name,
            snip["text"],
            snip["type"],
            snip.get("id"),
            snip.get("hash"),
            snip.get("fr"),
        )
        await event.edit(
            "snip {name} saved successfully. Get it with #{name}".format(name=name)
        )
    else:
        await event.edit("Reply to a message with `snips keyword` to save the snip")


@friday.on(friday_on_cmd("snipl"))
async def on_snip_list(event):
    if event.fwd_from:
        return
    all_snips = get_all_snips()
    OUT_STR = "Available Snips:\n"
    if len(all_snips) > 0:
        for a_snip in all_snips:
            OUT_STR += f"👉 #{a_snip.snip} \n"
    else:
        OUT_STR = "No Snips. Start Saving using `.snips`"
    if len(OUT_STR) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "snips.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="Available Snips",
                reply_to=event,
            )
            await event.delete()
    else:
        await event.edit(OUT_STR)


@friday.on(friday_on_cmd("snipd (\S+)"))
async def on_snip_delete(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(1)
    remove_snip(name)
    await event.edit("snip #{} deleted successfully".format(name))

@friday.on(friday_on_cmd(pattern="create (b|g|c)(?: |$)(.*)"))
async def telegraphs(grop):
    if grop.fwd_from:
        return
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
@friday.on(friday_on_cmd(pattern="warn(?: |$)(.*)"))
async def _s(event):
    if event.fwd_from:
        return
    if not event.is_group:
        await event.edit("This Command is Meant To Be Used in Chats/Groups")
        return
    user, reason = await get_user_from_event(event)
    sed = await friday.get_permissions(event.chat_id, user.id)
    if sed.is_admin:
        await event.edit("`Demn, Admins Can't Be Warned`")
        return
    dragon = await friday.get_permissions(event.chat_id, bot.uid)
    if not dragon.is_admin:
        await event.edit("`Demn, Me nOT Admin`")
        return
    limit, soft_warn = sql.get_warn_setting(event.chat_id)
    num_warns, reasons = sql.warn_user(user.id, event.chat_id, reason)
    if num_warns >= limit:
        sql.reset_warns(user.id, event.chat_id)
        if soft_warn:
            await friday.kick_participant(event.chat_id, user.id)
            reply = "{} warnings, {} has been kicked!".format(limit, user.id)
            await event.edit(reply)
        else:
            await friday.edit_permissions(event.chat_id, user.id, view_messages=False)
            reply = "{} warnings, {} has been banned!".format(
                limit, user.id, user.first_name
            )
            await event.edit(reply)
        for warn_reason in reasons:
            reply += "\n - {}".format(warn_reason)
    else:
        reply = "{} has {}/{} warnings... watch out!".format(user.id, num_warns, limit)
        if reason:
            reply += "\nReason for last warn:\n{}".format(reason)
        await event.edit(reply)


@friday.on(friday_on_cmd(pattern="rwarn(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.is_group:
        await event.edit("This Command is Meant To Be Used in Chats/Groups")
        return
    user, reason = await get_user_from_event(event)
    sed = await friday.get_permissions(event.chat_id, user.id)
    if sed.is_admin:
        await event.edit("Demn, Admins Can't Be Warned")
        return
    dragon = await friday.get_permissions(event.chat_id, bot.uid)
    if not dragon.is_admin:
        await event.edit("Demn, Me nOT Admin")
        return
    sql.reset_warns(user.id, event.chat_id)
    await event.edit("Warnings have been reset!")


@friday.on(friday_on_cmd(pattern="allwarns(?: |$)(.*)"))
async def __(event):
    if event.fwd_from:
        return
    if not event.is_group:
        await event.edit("This Command is Meant To Be Used in Chats/Groups")
        return
    user, reason = await get_user_from_event(event)
    result = sql.get_warns(user.id, event.chat_id)
    if result and result[0] != 0:
        num_warns, reasons = result
        limit, soft_warn = sql.get_warn_setting(event.chat_id)
        if reasons:
            text = (
                "This user has {}/{} warnings, for the following reasons: \n\n".format(
                    num_warns, limit
                )
            )
            for reason in reasons:
                text += "- {} \n".format(reason)
            await event.edit(text)
        else:
            await event.edit(
                "User has {}/{} warnings, but no reasons for any of them.".format(
                    num_warns, limit
                )
            )
    else:
        await event.edit("This user hasn't got any warnings!")


@friday.on(friday_on_cmd(pattern="slimit ?(.*)"))
async def m_(event):
    if event.fwd_from:
        return
    if not event.is_group:
        await event.edit("This Command is Meant To Be Used in Chats/Groups")
        return
    args = event.pattern_match.group(1)
    if args:
        if args.isdigit():
            if int(args) < 3:
                await event.edit("The minimum warn limit is 3!")
            else:
                sql.set_warn_limit(event.chat_id, int(args))
                await event.edit("Updated the warn limit to {}".format(args))
        else:
            await event.edit("Give me a number as an arg!")
    else:
        limit, soft_warn = sql.get_warn_setting(event.chat_id)
        await event.edit("The current warn limit is {}".format(limit))


@friday.on(friday_on_cmd(pattern="wap ?(.*)"))
async def m_(event):
    if event.fwd_from:
        return
    if not event.is_group:
        await event.edit("This Command is Meant To Be Used in Chats/groups")
        return
    args = event.pattern_match.group(1)
    if args:
        if args.lower() in ("on", "yes"):
            sql.set_warn_strength(event.chat_id, False)
            await event.edit("Too many warns will now result in a ban!")
        elif args.lower() in ("off", "no"):
            sql.set_warn_strength(event.chat_id, True)
            await event.edit(
                "Too many warns will now result in a kick! Users will be able to join again after."
            )
        else:
            await event.edit("I only understand on/yes/no/off!")
    else:
        limit, soft_warn = sql.get_warn_setting(chat.id)
        if soft_warn:
            await event.edit(
                "Warns are currently set to **kick** users when they exceed the limits."
            )
        else:
            await event.edit(
                "Warns are currently set to **ban** users when they exceed the limits."
            )


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif args:
        user = args[0]
        if len(args) == 2:
            extra = args[1]

        if user.isnumeric():
            user = int(user)

        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
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


async def get_user_sender_id(user, event):
    if isinstance(user, str):
        user = int(user)

    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None

    return user_obj

@friday.on(friday_on_cmd(pattern="admins"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "@admin: **Spam Spotted**"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f"[\u2063](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
    
@friday.on(friday_on_cmd("mention (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = previous_message.forward.sender_id
        else:
            replied_user = previous_message.sender_id
    else:
        await event.edit("reply To Message")
    user_id = replied_user
    caption = """<a href='tg://user?id={}'>{}</a>""".format(user_id, input_str)
    await event.edit(caption, parse_mode="HTML")
    
@friday.on(friday_on_cmd("get_bot ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Bots in this Channel**: \n"
    input_str = event.pattern_match.group(1)
    to_write_chat = await event.get_input_chat()
    chat = None
    if not input_str:
        chat = to_write_chat
    else:
        mentions = "Bots in {} channel: \n".format(input_str)
        try:
            chat = await borg.get_entity(input_str)
        except Exception as e:
            await event.edit(str(e))
            return None
    try:
        async for x in borg.iter_participants(chat, filter=ChannelParticipantsBots):
            if isinstance(x.participant, ChannelParticipantAdmin):
                mentions += "\n ⚜️ [{}](tg://user?id={}) `{}`".format(
                    x.first_name, x.id, x.id
                )
            else:
                mentions += "\n [{}](tg://user?id={}) `{}`".format(
                    x.first_name, x.id, x.id
                )
    except Exception as e:
        mentions += " " + str(e) + "\n"
    await event.edit(mentions)
    
@bot.on(events.ChatAction())  # pylint:disable=E0602
async def _(event):
    cws = get_current_welcome_settings(event.chat_id)
    if cws:
        # logger.info(event.stringify())
        """user_added=False,
        user_joined=True,
        user_left=False,
        user_kicked=False,"""
        if event.user_joined:
            if cws.should_clean_welcome:
                try:
                    await bot.delete_messages(  # pylint:disable=E0602
                        event.chat_id, cws.previous_welcome
                    )
                except Exception as e:  # pylint:disable=C0103,W0703
                    logger.warn(str(e))  # pylint:disable=E0602
            a_user = await event.get_user()
            chat = await event.get_chat()
            me = await bot.get_me()

            title = chat.title if chat.title else "this chat"
            participants = await event.client.get_participants(chat)
            count = len(participants)
            mention = "[{}](tg://user?id={})".format(a_user.first_name, a_user.id)
            first = a_user.first_name
            last = a_user.last_name
            if last:
                fullname = f"{first} {last}"
            else:
                fullname = first
            username = (
                f"@{me.username}" if me.username else f"[Me](tg://user?id={me.id})"
            )
            userid = a_user.id
            current_saved_welcome_message = cws.custom_welcome_message
            mention = "[{}](tg://user?id={})".format(a_user.first_name, a_user.id)

            current_message = await event.reply(
                current_saved_welcome_message.format(
                    mention=mention,
                    title=title,
                    count=count,
                    first=first,
                    last=last,
                    fullname=fullname,
                    username=username,
                    userid=userid,
                ),
                file=cws.media_file_id,
            )
            update_previous_welcome(event.chat_id, current_message.id)


@friday.on(friday_on_cmd(pattern="savewelcome"))
async def _(event):
    if event.fwd_from:
        return
    msg = await event.get_reply_message()
    if msg and msg.media:
        bot_api_file_id = pack_bot_file_id(msg.media)
        add_welcome_setting(event.chat_id, msg.message, True, 0, bot_api_file_id)
        await event.edit("Welcome note saved. ")
    else:
        input_str = event.text.split(None, 1)
        add_welcome_setting(event.chat_id, input_str[1], True, 0, None)
        await event.edit("Welcome note saved. ")


@friday.on(friday_on_cmd(pattern="clearwelcome$"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    cws = get_current_welcome_settings(event.chat_id)
    rm_welcome_setting(event.chat_id)
    await event.edit(
        "Welcome note cleared. "
        + "The previous welcome message was `{}`.".format(cws.custom_welcome_message)
    )


@friday.on(friday_on_cmd(pattern="listwelcome$"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    cws = get_current_welcome_settings(event.chat_id)
    if hasattr(cws, "custom_welcome_message"):
        await event.edit(
            "Welcome note found. "
            + "Your welcome message is\n\n`{}`.".format(cws.custom_welcome_message)
        )
    else:
        await event.edit("No Welcome Message found")
        
CMD_HELP.update(
    {
        "welcome": "**Welcome**\
\n\n**Syntax : **`.savewelcome <welcome message to save>`\
\n**Usage :** Saves welcome message.\
\n\n**Syntax : **`.clearwelcome`\
\n**Usage :** Clears welcome message.\
\n\n**Syntax : **`.listwelcome`\
\n**Usage :** Lists existing welcome message."
    }
)

CMD_HELP.update(
    {
        "admin": ".promote <username/reply> <custom rank (optional)>\
\n**Usage:** Provides admin rights to the person in the chat.\
\n\n.demote <username/reply>\
\n**Usage:** Revokes the person's admin permissions in the chat.\
\n\n.ban <username/reply> <reason (optional)>\
\n**Usage:** Bans the person off your chat.\
\n\n.unban <username/reply>\
\n**Usage:** Removes the ban from the person in the chat.\
\n\n.mute <username/reply> <reason (optional)>\
\n**Usage:** Mutes the person in the chat, works on admins too.\
\n\n.unmute <username/reply>\
\n**Usage:** Removes the person from the muted list.\
\n\n.gmute <username/reply> <reason (optional)>\
\n**Usage:** Mutes the person in all groups you have in common with them.\
\n\n.ungmute <username/reply>\
\n**Usage:** Reply someone's message with .ungmute to remove them from the gmuted list.\
\n\n.zombies\
\n**Usage:** Searches for deleted accounts in a group. Use .zombies clean to remove deleted accounts from the group.\
\n\n.adminlist\
\n**Usage:** Retrieves a list of admins in the chat.\
\n\n.users or .users <name of member>\
\n**Usage:** Retrieves all (or queried) users in the chat.\
\n\n.setgppic <reply to image>\
\n**Usage:** Changes the group's display picture."
    }
)
CMD_HELP.update(
    {
        "warns": "**Warns**\
\n\n**Syntax : **`.warn <reason> <reply or mention the user>`\
\n**Usage :** Warns The Given User.\
\n\n**Syntax : **`.rwarn <reply or mention the user>`\
\n**Usage :** Removes Warn Of The User.\
\n\n**Syntax : **`.allwarns <reply or mention the user>`\
\n**Usage :** Shows All The Warns Of The Given User.\
\n\n**Syntax : **`.slimit <no of max warns>`\
\n**Usage :** Sets Maximum Warn Limit.\
\n\n**Syntax : **`.wap <on or off>`\
\n**Usage :** If this is turned on, user gets banned after reaching maximum warns. If it's off, user is kicked."
    }
)
CMD_HELP.update(
    {
        "filters": "**Filters**\
\n\n**Syntax : **`.filter <word to trigger> <reply to triggered message>`\
\n**Usage :** save filters using this plugin.\
\n\n**Syntax : **`.filters`\
\n**Usage :** All the filters of current chat are listed.\
\n\n**Syntax : **`.stop <filter word to stop>`\
\n**Usage :** Deletes given trigger word.\
\n\n**Syntax : **`.rmfilters`\
\n**Usage :** All the filters in a chat are deleted."
    }
)
CMD_HELP.update(
    {
        "snip": "**Snip**\
\n\n**Syntax : **`.snips <name of snip> <reply to a message>`\
\n**Usage :** saves the message with given text.\
\n\n**Syntax : **`.snipl`\
\n**Usage :** lists all the snips.\
\n\n**Syntax : **`.snipd <name of snip>`\
\n**Usage :** Deletes the snip."
    }
)
