import functools
import inspect
import logging
import re
from pathlib import Path

from telethon import events

from fridaybot import CMD_LIST, LOAD_PLUG, SUDO_LIST, bot, client2, client3, CMD_HELP
from fridaybot.Configs import Config
from fridaybot.wraptools import (
    am_i_admin,
    ignore_bot,
    ignore_fwd,
    ignore_grp,
    ignore_pm,
)
from fridaybot.Configs import Config
sedprint = logging.getLogger("PLUGINS")
cmdhandler = Config.COMMAND_HAND_LER
bothandler = Config.BOT_HANDLER

def command(**args):
    args["func"] = lambda e: e.via_bot_id is None

    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    if 1 == 0:
        return print("stupidity at its best")
    else:
        pattern = args.get("pattern", None)
        allow_sudo = args.get("allow_sudo", False)
        allow_edited_updates = args.get("allow_edited_updates", False)
        args["incoming"] = args.get("incoming", False)
        args["outgoing"] = True
        if bool(args["incoming"]):
            args["outgoing"] = False

        try:
            if pattern is not None and not pattern.startswith("(?i)"):
                args["pattern"] = "(?i)" + pattern
        except:
            pass

        reg = re.compile("(.*)")
        if not pattern == None:
            try:
                cmd = re.search(reg, pattern)
                try:
                    cmd = (
                        cmd.group(1).replace("$", "").replace("\\", "").replace("^", "")
                    )
                except:
                    pass

                try:
                    CMD_LIST[file_test].append(cmd)
                except:
                    CMD_LIST.update({file_test: [cmd]})
            except:
                pass

        if allow_sudo:
            args["from_users"] = list(Config.SUDO_USERS)
            # Mutually exclusive with outgoing (can only set one of either).
            args["incoming"] = True
        del allow_sudo
        try:
            del args["allow_sudo"]
        except:
            pass

        if "allow_edited_updates" in args:
            del args["allow_edited_updates"]

        def decorator(func):
            if not allow_edited_updates:
                bot.add_event_handler(func, events.MessageEdited(**args))
            bot.add_event_handler(func, events.NewMessage(**args))
            if client2:
                client2.add_event_handler(func, events.NewMessage(**args))
            if client3:
                client3.add_event_handler(func, events.NewMessage(**args))
            try:
                LOAD_PLUG[file_test].append(func)
            except Exception:
                LOAD_PLUG.update({file_test: [func]})
            return func
        return decorator


def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path

        import fridaybot.modules
        import fridaybot.utils

        path = Path(f"fridaybot/modules/{shortname}.py")
        name = "fridaybot.modules.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        sedprint.info("Successfully (re)imported " + shortname)
    else:
        import importlib
        import sys
        from pathlib import Path

        import fridaybot.modules
        import fridaybot.utils

        path = Path(f"fridaybot/modules/{shortname}.py")
        name = "fridaybot.modules.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = bot
        mod.tgbot = bot.tgbot
        mod.Config = Config
        mod.Var = Config
        mod.command = command
        mod.logger = logging.getLogger(shortname)
        # support for uniborg
        sys.modules["uniborg.util"] = fridaybot.utils
        sys.modules["friday.util"] = fridaybot.utils
        sys.modules["userbot.utils"] = fridaybot.utils
        sys.modules["userbot.plugins"] = fridaybot.modules
        sys.modules["plugins"] = fridaybot.modules
        sys.modules["userbot"] = fridaybot
        mod.admin_cmd = friday_on_cmd
        mod.sudo_cmd = sudo_cmd
        mod.friday_on_cmd = friday_on_cmd
        mod.CMD_HELP = CMD_HELP
        mod.Config = Config
        mod.ignore_grp = ignore_grp()
        mod.ignore_pm = ignore_pm()
        mod.ignore_bot = ignore_bot()
        mod.am_i_admin = am_i_admin()
        mod.ignore_fwd = ignore_fwd()
        mod.borg = bot
        mod.friday = bot
        # support for paperplaneextended
        sys.modules["fridaybot.events"] = fridaybot.utils
        sys.modules["fridaybot.function.events"] = fridaybot.utils
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["fridaybot.modules." + shortname] = mod
        sedprint.info("Successfully imported " + shortname)

def load_module_dclient(shortname, client):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path

        import fridaybot.modules
        import fridaybot.utils

        path = Path(f"fridaybot/modules/{shortname}.py")
        name = "fridaybot.modules.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    else:
        import importlib
        import sys
        from pathlib import Path

        import fridaybot.modules
        import fridaybot.utils

        path = Path(f"fridaybot/modules/{shortname}.py")
        name = "fridaybot.modules.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = client
        mod.tgbot = bot.tgbot
        mod.Config = Config
        mod.Var = Config
        mod.command = command
        sedlu = str(shortname) + "- MClient -"
        mod.logger = logging.getLogger(sedlu)
        # support for uniborg
        sys.modules["uniborg.util"] = fridaybot.utils
        sys.modules["friday.util"] = fridaybot.utils
        sys.modules["userbot.utils"] = fridaybot.utils
        sys.modules["userbot.plugins"] = fridaybot.modules
        sys.modules["plugins"] = fridaybot.modules
        sys.modules["userbot"] = fridaybot
        mod.admin_cmd = friday_on_cmd
        mod.sudo_cmd = sudo_cmd
        mod.friday_on_cmd = friday_on_cmd
        mod.Config = Config
        mod.ignore_grp = ignore_grp()
        mod.ignore_pm = ignore_pm()
        mod.ignore_bot = ignore_bot()
        mod.am_i_admin = am_i_admin()
        mod.ignore_fwd = ignore_fwd()
        mod.borg = client
        mod.friday = client
        mod.CMD_HELP = CMD_HELP
        sys.modules["fridaybot.events"] = fridaybot.utils
        sys.modules["fridaybot.function.events"] = fridaybot.utils
        spec.loader.exec_module(mod)
        sys.modules["fridaybot.modules." + shortname] = mod

def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                bot.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except:
            name = f"fridaybot.modules.{shortname}"

            for i in reversed(range(len(bot._event_builders))):
                ev, cb = bot._event_builders[i]
                if cb.__module__ == name:
                    del bot._event_builders[i]
    except:
        raise ValueError


def admin_cmd(pattern=None, **args):
    args["func"] = lambda e: e.via_bot_id is None

    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    allow_sudo = args.get("allow_sudo", False)

    # get the pattern from the decorator
    if pattern is not None:
        if pattern.startswith("\#"):
            # special fix for snip.py
            args["pattern"] = re.compile(pattern)
        else:
            args["pattern"] = re.compile(cmdhandler + pattern)
            cmd = cmdhandler + pattern
            try:
                CMD_LIST[file_test].append(cmd)
            except:
                CMD_LIST.update({file_test: [cmd]})

    args["outgoing"] = True
    # should this command be available for other users?
    if allow_sudo:
        args["from_users"] = list(Config.SUDO_USERS)
        # Mutually exclusive with outgoing (can only set one of either).
        args["incoming"] = True
        del args["allow_sudo"]

    # error handling condition check
    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True

    # add blacklist chats, UB should not respond in these chats
    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        args["allow_edited_updates"]
        del args["allow_edited_updates"]
    # check if the plugin should listen for outgoing 'messages'
    return events.NewMessage(**args)

def friday_on_cmd(pattern=None, **args):
    args["func"] = lambda e: e.via_bot_id is None

    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    allow_sudo = args.get("allow_sudo", False)

    # get the pattern from the decorator
    if pattern is not None:
        if pattern.startswith("\#"):
            # special fix for snip.py
            args["pattern"] = re.compile(pattern)
        else:
            args["pattern"] = re.compile(cmdhandler + pattern)
            cmd = cmdhandler + pattern
            try:
                CMD_LIST[file_test].append(cmd)
            except:
                CMD_LIST.update({file_test: [cmd]})

    args["outgoing"] = True
    # should this command be available for other users?
    if allow_sudo:
        args["from_users"] = list(Config.SUDO_USERS)
        # Mutually exclusive with outgoing (can only set one of either).
        args["incoming"] = True
        del args["allow_sudo"]

    # error handling condition check
    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True

    # add blacklist chats, UB should not respond in these chats
    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        args["allow_edited_updates"]
        del args["allow_edited_updates"]
    return events.NewMessage(**args)


""" Userbot module for managing events.
 One of the main components of the fridaybot. """

import asyncio
import datetime
import math
import sys
import traceback
from time import gmtime, strftime

from telethon import events

from fridaybot import bot


def register(**args):
    """ Register a new event. """
    args["func"] = lambda e: e.via_bot_id is None

    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    pattern = args.get("pattern", None)
    disable_edited = args.get("disable_edited", True)

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern

    if "disable_edited" in args:
        del args["disable_edited"]

    reg = re.compile("(.*)")
    if not pattern == None:
        try:
            cmd = re.search(reg, pattern)
            try:
                cmd = cmd.group(1).replace("$", "").replace("\\", "").replace("^", "")
            except:
                pass

            try:
                CMD_LIST[file_test].append(cmd)
            except:
                CMD_LIST.update({file_test: [cmd]})
        except:
            pass

    def decorator(func):
        if not disable_edited:
            bot.add_event_handler(func, events.MessageEdited(**args))
        bot.add_event_handler(func, events.NewMessage(**args))
        if client2:
            client2.add_event_handler(func, events.NewMessage(**args))
        if client3:
            client3.add_event_handler(func, events.NewMessage(**args))
        try:
            LOAD_PLUG[file_test].append(func)
        except Exception:
            LOAD_PLUG.update({file_test: [func]})
        return func
    return decorator


def errors_handler(func):
    async def wrapper(errors):
        try:
            await func(errors)
        except BaseException:

            date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            new = {"error": str(sys.exc_info()[1]), "date": datetime.datetime.now()}

            text = "**USERBOT CRASH REPORT**\n\n"

            link = "[Here](https://t.me/FridayOT)"
            text += "If you wanna you can report it"
            text += f"- just forward this message {link}.\n"
            text += "Nothing is logged except the fact of error and date\n"

            ftext = "\nDisclaimer:\nThis file uploaded ONLY here,"
            ftext += "\nwe logged only fact of error and date,"
            ftext += "\nwe respect your privacy,"
            ftext += "\nyou may not report this error if you've"
            ftext += "\nany confidential data here, no one will see your data\n\n"

            ftext += "--------BEGIN FRIDAY USERBOT TRACEBACK LOG--------"
            ftext += "\nDate: " + date
            ftext += "\nGroup ID: " + str(errors.chat_id)
            ftext += "\nSender ID: " + str(errors.sender_id)
            ftext += "\n\nEvent Trigger:\n"
            ftext += str(errors.text)
            ftext += "\n\nTraceback info:\n"
            ftext += str(traceback.format_exc())
            ftext += "\n\nError text:\n"
            ftext += str(sys.exc_info()[1])
            ftext += "\n\n--------END USERBOT TRACEBACK LOG--------"

            command = 'git log --pretty=format:"%an: %s" -5'

            ftext += "\n\n\nLast 5 commits:\n"

            process = await asyncio.create_subprocess_shell(
                command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()
            result = str(stdout.decode().strip()) + str(stderr.decode().strip())

            ftext += result

    return wrapper


async def progress(current, total, event, start, type_of_ps, file_name=None):
    """Generic progress_callback for both
    upload.py and download.py"""
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "[{0}{1}]\nProgress: {2}%\n".format(
            "".join(["█" for i in range(math.floor(percentage / 5))]),
            "".join(["░" for i in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nETA: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            await event.edit(
                "{}\nFile Name: `{}`\n{}".format(type_of_ps, file_name, tmp)
            )
        else:
            await event.edit("{}\n{}".format(type_of_ps, tmp))


def humanbytes(size):
    """Input size in bytes,
    outputs in a human readable format"""
    # https://stackoverflow.com/a/49361727/4723940
    if not size:
        return ""
    # 2 ** 10 = 1024
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def time_formatter(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + " day(s), ") if days else "")
        + ((str(hours) + " hour(s), ") if hours else "")
        + ((str(minutes) + " minute(s), ") if minutes else "")
        + ((str(seconds) + " second(s), ") if seconds else "")
        + ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    )
    return tmp[:-2]


class Loader:
    def __init__(self, func=None, **args):
        self.Config = Config
        bot.add_event_handler(func, events.NewMessage(**args))


def sudo_cmd(pattern=None, **args):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    allow_sudo = args.get("allow_sudo", False)
    # get the pattern from the decorator
    if pattern is not None:
        if pattern.startswith("\#"):
            # special fix for snip.py
            args["pattern"] = re.compile(pattern)
        else:
            args["pattern"] = re.compile(Config.SUDO_COMMAND_HAND_LER + pattern)
            reg = Config.SUDO_COMMAND_HAND_LER[1]
            cmd = (reg + pattern).replace("$", "").replace("\\", "").replace("^", "")
            try:
                SUDO_LIST[file_test].append(cmd)
            except:
                SUDO_LIST.update({file_test: [cmd]})
    args["outgoing"] = True
    # should this command be available for other users?
    if allow_sudo:
        args["from_users"] = list(Config.SUDO_USERS)
        # Mutually exclusive with outgoing (can only set one of either).
        args["incoming"] = True
        del args["allow_sudo"]
    # error handling condition check
    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True
    # add blacklist chats, UB should not respond in these chats
    args["blacklist_chats"] = True
    black_list_chats = list(Config.UB_BLACK_LIST_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats
    # add blacklist chats, UB should not respond in these chats
    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        args["allow_edited_updates"]
        del args["allow_edited_updates"]
    # check if the plugin should listen for outgoing 'messages'
    return events.NewMessage(**args)


async def edit_or_reply(event, text, parse_mode=None):
    parse_mode_z = parse_mode if parse_mode else "md"
    if event.sender_id in Config.SUDO_USERS:
        reply_to = await event.get_reply_message()
        if reply_to:
            return await reply_to.reply(text, parse_mode=parse_mode_z)
        return await event.reply(text, parse_mode=parse_mode_z)
    return await event.edit(text, parse_mode=parse_mode_z)


#    Copyright (C) Midhun KM 2020
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


def assistant_cmd(add_cmd, is_args=False):
    def cmd(func):
        serena = bot.tgbot
        if is_args:
            pattern = bothandler + add_cmd + "(?: |$)(.*)"
        elif is_args == "stark":
            pattern = bothandler + add_cmd + " (.*)"
        elif is_args == "heck":
            pattern = bothandler + add_cmd
        elif is_args == "snips":
            pattern = bothandler + add_cmd + " (\S+)"
        else:
            pattern = bothandler + add_cmd + "$"
        serena.add_event_handler(
            func, events.NewMessage(incoming=True, pattern=pattern)
        )

    return cmd


def is_admin():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            serena = bot.tgbot
            sed = await serena.get_permissions(event.chat_id, event.sender_id)
            user = event.sender_id
            kek = bot.uid
            if sed.is_admin:
                await func(event)
            if event.sender_id == kek:
                pass
            elif not user:
                pass
            if not sed.is_admin:
                await event.reply("Only Admins Can Use it.")

        return wrapper

    return decorator


def is_bot_admin():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            serena = bot.tgbot
            pep = await serena.get_me()
            sed = await serena.get_permissions(event.chat_id, pep)
            if sed.is_admin:
                await func(event)
            else:
                await event.reply("I Must Be Admin To Do This.")

        return wrapper

    return decorator


def only_pro():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            kek = list(Config.SUDO_USERS)
            kek.append(bot.uid)
            if event.sender_id in kek:
                await func(event)
            else:
                await event.reply("Only Owners, Sudo Users Can Use This Command.")

        return wrapper

    return decorator


def god_only():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            moms = bot.uid
            if event.sender_id == moms:
                await func(event)
            else:
                pass

        return wrapper

    return decorator


def only_groups():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            if event.is_group:
                await func(event)
            else:
                await event.reply("This Command Only Works On Groups.")

        return wrapper

    return decorator


def only_group():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            if event.is_group:
                await func(event)
            else:
                pass

        return wrapper

    return decorator


def peru_only():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            kek = list(Config.SUDO_USERS)
            kek.append(bot.uid)
            if event.sender_id in kek:
                await func(event)
            else:
                pass

        return wrapper

    return decorator


def only_pvt():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            if event.is_group:
                pass
            else:
                await func(event)

        return wrapper

    return decorator


def start_assistant(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"fridaybot/modules/assistant/{shortname}.py")
        name = "fridaybot.modules.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        sedprint.info("Starting Your Assistant Bot.")
        sedprint.info("Assistant Sucessfully imported " + shortname)
    else:
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"fridaybot/modules/assistant/{shortname}.py")
        name = "fridaybot.modules.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.tgbot = bot.tgbot
        mod.serena = bot.tgbot
        mod.assistant_cmd = assistant_cmd
        mod.god_only = god_only()
        mod.only_groups = only_groups()
        mod.only_pro = only_pro()
        mod.pro_only = only_pro()
        mod.only_group = only_group()
        mod.is_bot_admin = is_bot_admin()
        mod.is_admin = is_admin()
        mod.peru_only = peru_only()
        mod.only_pvt = only_pvt()
        spec.loader.exec_module(mod)
        sys.modules["fridaybot.modules.assistant" + shortname] = mod
        sedprint.info("Assistant Has imported " + shortname)
