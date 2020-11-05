# Lots of lub to @r4v4n4 for gibing the base <3
""" cmd is .scan """

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.utils import friday_on_cmd


@friday.on(friday_on_cmd("scan ?(.*)", allow_sudo=True))
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
    chat = "@DrWebBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit(
        " **covid19 will end with the end of 2020 from the globe.** `still let me check this thing.`"
    )
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=161163358)
            )
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock the virus scan bot and try again```")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            if response.text.startswith("Select"):
                await event.edit(
                    "`Please go to` Virus Scan Bot `and select your language.`"
                )
            else:
                await event.edit(
                    f"`Antivirus scan was completed.`\n**covid19 will end with the end of 2020 from the globe.**\n`Yeah, I got the final results.`\n {response.message.message}"
                )
