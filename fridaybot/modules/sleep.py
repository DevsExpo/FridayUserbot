""" Userbot module for other small commands. """

from random import randint
from time import sleep

from fridaybot.events import register


@register(outgoing=True, pattern="^.sleep( [0-9]+)?$")
async def sleepybot(time):
    """ For .sleep command, let the userbot snooze for a few second. """
    message = time.text
    if not message[0].isalpha() and message[0] not in ("/", "#", "@", "!"):
        if " " not in time.pattern_match.group(1):
            await time.reply("Syntax: `.sleep [seconds]`")
        else:
            counter = int(time.pattern_match.group(1))
            await time.edit("`Ok Boss, I'm Going To Sleep...😴`")
            sleep(2)
            if LOGGER:
                await time.client.send_message(
                    LOGGER_GROUP,
                    "You Put The Bot To Sleep For " + str(counter) + " seconds",
                )
            sleep(counter)
