# Advanced Antivirus  Scanner Pligin Made by @Hackintush
# All Credits Belong to CɪᴘʜᴇʀX.
# Copy with Credit
import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP
from userbot import bot as cipherx
from userbot.utils import admin_cmd as cipherx_on_cmd

bot = "@VirusYabBot"


@cipherx.on(cipherx_on_cmd("ment ?(.*)"))
async def _(event):
    reply = await event.get_reply_message()
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("Reply to any user message.")
        return
    if not reply_message.media:
        await event.edit("Reply to file")
        return
    chat = "@VirusYabBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("Reply to actual user's message.")
        return
    await event.edit("Scanning...")
    async with borg.conversation(chat) as conv:
        try:
            await conv.send_message(reply_message)
            await asyncio.sleep(2)
            reply = await conv.get_response()
            final = reply.text
            await borg.send_message(
                event.chat_id, final.rsplit("\n", 4)[0], reply_to=reply.id
            )
        except YouBlockedUserError:
            await event.edit("Error: Unblock bot and retry!")


CMD_HELP.update(
    {
        "antivirus 2": "Antivirus 2\
        \n\nSyntax : .ment <reply to file>\
        \nUsage : Scans files Max 300 MB."
    }
)
