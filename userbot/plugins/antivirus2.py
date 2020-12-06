# Lots of lub to @r4v4n4 for gibing the base <3
""" cmd is .anti """

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.utils import friday_on_cmd
from userbot import CMD_HELP

@friday.on(friday_on_cmd("anti ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("```reply to a media message```")
        return
    chat = "@VirusYabBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("`Scanning by CɪᴘʜᴇʀX Antivirus Algorithm...` ")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=397530575)
            )
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please remove my restrictions and try again```")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await event.edit(
                f"**Antivirus scan was completed**\n {response.message.message}"
            )
            # await event.edit(("`Antivirus scan was completed.`\n`Yeah, I got the final results.`\n ") + response + response.replace("------------ADS------------\nدریافت فالوور، لایک و ممبر رایگان\n\n@ViewFakBot", ""))


CMD_HELP.update(
    {
        "antivirus2": "`.anti` reply to a file:\
      \nUse - Scans the file with antivirus.\
      "
    }
)
