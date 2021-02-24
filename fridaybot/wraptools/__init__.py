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


import functools
import re

from telethon import events

from fridaybot import bot
from fridaybot.Configs import Config
from fridaybot.Configs import Config


def ignore_fwd():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            if event.fwd_from:
                await func(event)
            else:
                pass

        return wrapper

    return decorator


def am_i_admin():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            pep = await bot.get_me()
            sed = await bot.get_permissions(event.chat_id, pep)
            if sed.is_admin:
                await func(event)
            if sed.is_creator:
                await func(event)
            else:
                await event.edit(
                    "I Must Be Admin To Do This. Please Make Sure I Am Admin."
                )

        return wrapper

    return decorator


def ignore_bot():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            reply_message = await event.get_reply_message()
            reply_message.sender
            if not reply_message.sender.bot:
                await func(event)
            else:
                await event.edit("Bruh, Reply to Actual Users Message")

        return wrapper

    return decorator


def ignore_pm():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            if event.is_group:
                await func(event)
            else:
                await event.edit("This Command Only Works On Groups.")

        return wrapper

    return decorator


def ignore_grp():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            if event.is_group:
                pass
            else:
                await func(event)

        return wrapper

    return decorator
