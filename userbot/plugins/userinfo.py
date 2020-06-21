#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from .. import loader, utils
import logging

from telethon.tl.functions.users import GetFullUserRequest

logger = logging.getLogger(__name__)


@loader.tds
class UserInfoMod(loader.Module):
    """Tells you about people"""
    strings = {"name": "User Info",
               "first_name": "First name: <code>{}</code>",
               "last_name": "\nLast name: <code>{}</code>",
               "id": "\nID: <code>{}</code>",
               "bio": "\nBio: <code>{}</code>",
               "restricted": "\nRestricted: <code>{}</code>",
               "deleted": "\nDeleted: <code>{}</code>",
               "bot": "\nBot: <code>{}</code>",
               "verified": "\nVerified: <code>{}</code>",
               "dc_id": "\nDC ID: <code>{}</code>",
               "find_error": "<b>Couldn't find that user.</b>",
               "no_args_or_reply": "<b>No args or reply was provided.</b>",
               "provide_user": "Provide a user to locate",
               "searching_user": "Searching for user...",
               "cannot_find": "Can't find user.",
               "permalink_txt": "<a href='tg://user?id={uid}'>{txt}</a>",
               "permalink_uid": "<a href='tg://user?id={uid}'>Permalink to {uid}</a>",
               "encode_cfg_doc": "Encode unicode characters"}

    def __init__(self):
        self.config = loader.ModuleConfig("ENCODE", False, lambda m: self.strings("encode_cfg_doc", m))

    def _handle_string(self, string):
        if self.config["ENCODE"]:
            return utils.escape_html(ascii(string))
        return utils.escape_html(string)

    @loader.unrestricted
    @loader.ratelimit
    async def userinfocmd(self, message):
        """Use in reply to get user info"""
        if message.is_reply:
            full = await self.client(GetFullUserRequest((await message.get_reply_message()).from_id))
        else:
            args = utils.get_args(message)
            if not args:
                return await utils.answer(message, self.strings("no_args_or_reply", message))
            try:
                full = await self.client(GetFullUserRequest(args[0]))
            except ValueError:
                return await utils.answer(message, self.strings("find_error", message))
        logger.debug(full)
        reply = self.strings("first_name", message).format(self._handle_string(full.user.first_name))
        if full.user.last_name is not None:
            reply += self.strings("last_name", message).format(self._handle_string(full.user.last_name))
        reply += self.strings("id", message).format(utils.escape_html(full.user.id))
        reply += self.strings("bio", message).format(self._handle_string(full.about))
        reply += self.strings("restricted", message).format(utils.escape_html(str(full.user.restricted)))
        reply += self.strings("deleted", message).format(utils.escape_html(str(full.user.deleted)))
        reply += self.strings("bot", message).format(utils.escape_html(str(full.user.bot)))
        reply += self.strings("verified", message).format(utils.escape_html(str(full.user.verified)))
        if full.user.photo:
            reply += self.strings("dc_id", message).format(utils.escape_html(str(full.user.photo.dc_id)))
        await utils.answer(message, reply)

    @loader.unrestricted
    @loader.ratelimit
    async def permalinkcmd(self, message):
        """Get permalink to user based on ID or username"""
        args = utils.get_args(message)
        if len(args) < 1:
            await utils.answer(message, self.strings("provide_user", message))
            return
        try:
            user = int(args[0])
        except ValueError:
            user = args[0]
        try:
            user = await self.client.get_entity(user)
        except ValueError as e:
            logger.debug(e)
            # look for the user
            await utils.answer(message, self.strings("searching_user", message))
            await self.client.get_dialogs()
            try:
                user = await self.client.get_entity(user)
            except ValueError:
                await utils.answer(message, self.strings("cannot_find", message))
                return
        if len(args) > 1:
            await utils.answer(message, self.strings("permalink_txt", message).format(uid=user.id, txt=args[1]))
        else:
            await utils.answer(message, self.strings("permalink_uid", message).format(uid=user.id))

    async def client_ready(self, client, db):
        self.client = client
