from telegraph import Telegraph
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP
from userbot.utils import admin_cmd

telegraph = Telegraph()
mee = telegraph.create_account(short_name="yohohehe")


@borg.on(admin_cmd(pattern="purl ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("**Reply to any document.**")
        return
    reply_message = await event.get_reply_message()
    chat = "@FiletolinkTGbot"
    reply_message.sender
    await event.edit("**Making public url...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1011636686)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("```Please unblock bot```")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )


@borg.on(admin_cmd(pattern="limits ?(.*)"))
async def _(event):
    bot = "@SpamBot"
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/start")
                danish = await conv.get_response()
                await borg.send_message(event.chat_id, danish.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` bot `and retry!")


@borg.on(admin_cmd(pattern="reader ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("**Reply to a URL.**")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("**Reply to a url message.**")
        return
    chat = "@chotamreaderbot"
    reply_message.sender
    await event.edit("**Making instant view...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=272572121)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("Please unblock bot")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )


CMD_HELP.update(
    {
        "bots": ".purl (reply to file)\nUse - Get a direct download link of that file/doc/pic/vid\
        \n\n.reader (reply to url)\nUse - Open that url in telegraph .\
        \n\n.recognize (reply to any media)\nUse - send details about it.\
        \n\n.limits\nUse - Check if you are limited by telegram."
    }
)
