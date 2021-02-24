from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from uniborg.util import friday_on_cmd

from fridaybot import CMD_HELP


@friday.on(friday_on_cmd("sg ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    holy = "Name History [@SangMataInfo_bot] \n"
    if not reply_message.text:
        await event.edit("```reply to text message```")
        return
    chat = "@SangMataInfo_bot"
    sw = reply_message.sender_id
    kk = reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @SangMataInfo_bot and try again```")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            await borg.send_message("@SangMataInfo_bot", "/search_id " + str(sw))
            response1 = await response
            response2 = await response
            if response2.text.startswith("No records"):
                await event.edit("Yes, You Heard Right, No Records Found.")
                return
            response3 = await response
            holy += "Name History \n" + str(response2.text) + "\nUsername History \n" + str(response3.text)
            await event.edit(holy)
        else:
            await event.edit(f"{response.message.message}")


@friday.on(friday_on_cmd("fakemail ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```reply to text message```")
        return
    chat = "@fakemailbot"
    reply_message.sender
    await event.edit("```Processing```")
    link = f"/generate"
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=177914997)
            )
            await conv.send_message(link)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @fakemailbot and try again```")
            return
        if response.text.startswith("send"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await event.edit(f"{response.message.message}")


@friday.on(friday_on_cmd("ub ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```reply to text message```")
        return
    chat = "@uploadbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=97342984)
            )
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @uploadbot and try again```")
            return
        if response.text.startswith("Hi!,"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await event.edit(f"{response.message.message}")


@friday.on(friday_on_cmd("gid ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```reply to text message```")
        return
    chat = "@getidsbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=186675376)
            )
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @getidsbot and try again```")
            return
        if response.text.startswith("Hello,"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await event.edit(f"{response.message.message}")


@friday.on(friday_on_cmd("urban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```reply to text message```")
        return
    chat = "@UrbanDictionaryBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=185693644)
            )
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @UrbanDictionaryBot and try again```")
            return
        if response.text.startswith("Hello,"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await event.edit(f"{response.message.message}")


CMD_HELP.update(
    {
        "sangmata": "**Sangmata**\
\n\n**Syntax : **`.sg <reply to someone's message>`\
\n**Usage :** gets name history of the person.\
\n\n**Syntax : **`.fakemail <reply to someone's message>`\
\n**Usage :** Gets you fake email to use.\
\n\n**Syntax : **`.ub <reply to a link>`\
\n**Usage :** Download from given link and uploades in telegram.\
\n\n**Syntax : **`.gid <reply to someone's message>`\
\n**Usage :** gets id and info of the person.\
\n\n**Syntax : **`.urban <reply to text>`\
\n**Usage :** Gets you meaning of replyed text."
    }
)
