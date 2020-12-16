# Modified by @Hackintush
import asyncio

from telethon import events

from userbot import CMD_HELP

SHUTDOWN = "https://filetolinktelegrambot.herokuapp.com/41750275203384/voice.ogg"
STARTUP = "https://filetolinktelegrambot.herokuapp.com/41767455072568/funny.gif.mp4"


@friday.on(events.NewMessage(pattern=r"\.fhack", outgoing=True))
async def _(event):
    await event.client.send_file(
        event.chat_id,
        STARTUP,
        caption="`You will be Hacked in a Moment by CɪᴘʜᴇʀX Bot.`",
        voice_note=True,
    ),
    await event.client.send_file(
        event.chat_id, SHUTDOWN, caption="`Hacking in progress...`", voice_note=True
    )
    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 11)

    animation_chars = [
        "`Connecting To CɪᴘʜᴇʀX Server...`",
        "`Target Selected.`",
        "`Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n`Looking for Telegram Data...`\nETA: 0m, 20s",
        "`Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n`Found SD Directory...`\n`Looking for Telegram Data : ✅`\nETA: 0m, 10s",
        "`Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n`Searching for Databases....`\n`Looking for Telegram Data : ✅`\n`Found Telegram Database Directory : ✅ `\nETA: 0m, 15s",
        "`Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`\n`Found msgstore.db.crypt12...`\n`Looking for Telegram Data : ✅`\n`Found Telegram Database Directory : ✅ `\n`Searching for Databases : ✅ `\nETA: 0m, 09s",
        "`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n`Trying to Decrypt...`\n`Looking for Telegram Data : ✅`\n`Found Telegram Database Directory : ✅\n`Searching for Databases : ✅`\n`Found msgstore.db.crypt12 :  ✅`\n`⚠️ error occurred ..`\nETA: 0m, 25s",
        "`Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `\n`Decryption successful!`\n`Looking for Telegram Data : ✅`\n`⚠️ error occurred ..`\n`Found Telegram Database Directory : ✅`\n`⚠️ Error Occurred ...`\n`Searching for Databases : ✅`\n`Found msgstore.db.crypt12 :  ✅`\nETA: 0m, 25s",
        "`Hacking... 84%\n█████████████████████▒▒▒▒ `\n`Scanning file...`\n`Looking for Telegram Data : ✅`\n`⚠️ error occurred ..`\n`Found Telegram Database Directory : ✅`\n`⚠️ Error Occurred ..`\n`⚠️ Error Occurred ...`\n`Searching for Databases : ✅`\n`Found msgstore.db.crypt12 :  ✅`\n`Scanning File :  ✅`\nETA: 0m, 16s",
        "`Hacking... 100%\n` 98% HACKED`",
        "`Targeted Account Hacked By CɪᴘʜᴇʀX`\n\n`_______________________`\n`result ... :)`\n\n`Chatlist : ✅`\n`Calls : ✅`\n`groups : ✅`\n `Contacts : ✅`\n`Channel : ✅`\n`Deleted Messages : ❌`\n`Edited Messages : ❌`\n`All API Tokens : ✅`",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])


CMD_HELP.update(
    {
        "fhack": "**Fhack**\
\n\n**Syntax : **`.fhack`\
\n**Usage :** Fun Hacking Plugin"
    }
)
