# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
# You can find misc modules, which dont fit in anything xD

""" Userbot module for other small commands. """

from random import randint
from time import sleep
from fridaybot.utils import friday_on_cmd
from fridaybot import CMD_HELP
from fridaybot.function.events import register


@friday.on(friday_on_cmd(pattern="rndm"))
async def randomise(items):
    if items.fwd_from:
        return
    """ For .random command, get a random item from the list of items. """
    if not items.text[0].isalpha() and items.text[0] not in ("/", "#", "@", "!"):
        itemo = (items.text[8:]).split()
        index = randint(1, len(itemo) - 1)
        await items.edit(
            "**Query: **\n`"
            + items.text[8:]
            + "`\n**Output: **\n`"
            + itemo[index]
            + "`"
        )

@friday.on(friday_on_cmd(pattern="sleep( [0-9]+)?$"))
async def sleepybot(time):
    if time.fwd_from:
        return
    """ For .sleep command, let the fridaybot snooze for a few second. """
    message = time.text
    if not message[0].isalpha() and message[0] not in ("/", "#", "@", "!"):
        if " " not in time.pattern_match.group(1):
            await time.reply("Syntax: `.sleep [seconds]`")
        else:
            counter = int(time.pattern_match.group(1))
            await time.edit("`I am sulking and snoozing....`")
            sleep(2)
            if LOGGER:
                await time.client.send_message(
                    LOGGER_GROUP,
                    "You put the bot to sleep for " + str(counter) + " seconds",
                )
            sleep(counter)


CMD_HELP.update(
    {
        "misc": "**Misc**\
\n\n**Syntax : **`.random <mention text or numbers>`\
\n**Usage :** This plugin picks random text or number from given texts or numbers.\
\n\n**Syntax : **`.sleep <time in seconds>`\
\n**Usage :** Bot sleeps for given time."
    }
)
