#    Copyright (C) Midhun KM 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditAdminRequest, EditBannedRequest
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (
    ChatAdminRights,
    ChatBannedRights,
    MessageEntityMentionName,
)

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
serena = tgbot
UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)


@assistant_cmd("ban", is_args=True)
@only_groups
@is_bot_admin
@is_admin
async def ban(event):
    chat = await event.get_chat()
    chat.admin_rights
    chat.creator
    user, reason = await get_user_from_event(event)
    kekme = await serena.get_permissions(event.chat_id, user)
    momos = user
    momoz = momos.first_name
    if kekme.is_admin:
        await event.reply("Oh, Yeah? Lets Start Banning Admins.")
        return
    if user:
        pass
    else:
        return
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS))
    except BadRequestError:
        await event.reply("I Could't Ban That User Probably Due To Less Permissions.")
        return
    if reason:
        await event.reply(f"Banned {momoz} For \nReason: {reason}")
    else:
        await event.reply(f"Banned {momoz} !")


@assistant_cmd("unban", is_args=True)
@only_groups
@is_bot_admin
@is_admin
async def nothanos(event):
    chat = await event.get_chat()
    chat.admin_rights
    chat.creator
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
        await event.reply("I Could't UnBan That User Probably Due To Less Permissions.")
        return


@assistant_cmd("promote", is_args=True)
@only_groups
@is_bot_admin
@is_admin
async def promote(event):
    chat = await event.get_chat()
    chat.admin_rights
    chat.creator
    new_rights = ChatAdminRights(
        add_admins=False,
        invite_users=False,
        change_info=False,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
    )
    user, rank = await get_user_from_event(event)
    kekme = await serena.get_permissions(event.chat_id, user)
    if kekme.is_admin:
        await event.reply("Oh, Yeah? Promote A Admin?")
        return
    if not rank:
        rank = "Admin"
    if user:
        pass
    else:
        return
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, new_rights, rank))
        await event.reply("Promoted Successfully! Now give Party")
    except BadRequestError:
        await event.reply(
            "I Could't Promote That User Probably Due To Less Permissions."
        )
        return


@assistant_cmd("demote", is_args=True)
@only_groups
@is_bot_admin
@is_admin
async def demote(event):
    chat = await event.get_chat()
    chat.admin_rights
    chat.creator
    rank = "Admin"
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
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, newrights, rank))
    except BadRequestError:
        await event.reply(
            "I Could't Demote That User Probably Due To Less Permissions."
        )
        return
    await event.reply("Demoted This User Sucessfully.")


@assistant_cmd("pin", is_args=True)
@only_groups
@is_bot_admin
@is_admin
async def pin(event):
    await event.get_chat()
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
        await event.reply(
            "I Could't Pin That Message Probably Due To Less Permissions."
        )
        return
    await event.reply("Pinned This Message Sucessfully.")
    await get_user_sender_id(event.sender_id, event)


@assistant_cmd("kick", is_args=True)
@only_groups
@is_bot_admin
@is_admin
async def kick(event):
    chat = await event.get_chat()
    chat.admin_rights
    chat.creator
    user, reason = await get_user_from_event(event)
    kekme = await serena.get_permissions(event.chat_id, user)
    momos = user
    momos.first_name
    if kekme.is_admin:
        await event.reply("Oh, Yeah? Lets Start kicking Admins.")
        retur
    if not user:
        await event.reply("Mention A User")
        return
    try:
        await event.client.kick_participant(event.chat_id, user.id)
    except:
        await event.reply("I Could't Kick That User Probably Due To Less Permissions.")
        return
    if reason:
        await event.reply(
            f"`Kicked` [{user.first_name}](tg://user?id={user.id})`!`\nReason: {reason}"
        )
    else:
        await event.reply(f"`Kicked` [{user.first_name}](tg://user?id={user.id})`!`")


@assistant_cmd("mute", is_args=True)
@only_groups
@is_bot_admin
@is_admin
async def mute(event):
    chat = await event.get_chat()
    chat.admin_rights
    chat.creator
    user, reason = await get_user_from_event(event)
    kekme = await serena.get_permissions(event.chat_id, user)
    momos = user
    momos.first_name
    if kekme.is_admin:
        await event.reply("Oh, Mutting? Lets Start Banning Admins.")
        retur
    if not user:
        await event.reply("Mention A User")
        return
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, MUTE_RIGHTS))
    except:
        await event.reply("I Could't Mute That User Probably Due To Less Permissions.")
        return
    if reason:
        await event.reply(
            f"`Muted` [{user.first_name}](tg://user?id={user.id})`!`\nReason: {reason}"
        )
    else:
        await event.reply(f"`Kicked` [{user.first_name}](tg://user?id={user.id})`!`")


@assistant_cmd("unmute", is_args=True)
@only_groups
@is_bot_admin
@is_admin
async def mute(event):
    chat = await event.get_chat()
    chat.admin_rights
    chat.creator
    user, reason = await get_user_from_event(event)
    if not user:
        await event.reply("Mention A User")
        return
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, UNMUTE_RIGHTS))
    except:
        await event.reply(
            "I Could't UnMute That User Probably Due To Less Permissions."
        )
        return
    if reason:
        await event.reply(
            f"`UnMuted` [{user.first_name}](tg://user?id={user.id})`!`\nReason: {reason}"
        )
    else:
        await event.reply(f"`Unmute` [{user.first_name}](tg://user?id={user.id})`!`")


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


async def get_user_sender_id(user, event):
    if isinstance(user, str):
        user = int(user)

    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None

    return user_obj
