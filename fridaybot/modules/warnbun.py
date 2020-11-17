from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import friday_on_cmd

from fridaybot.utils import friday_on_cmd


@friday.on(friday_on_cmd("warn1"))
async def _(event):
    if event.fwd_from:
        return
    mentions = (
        "`You Have  1/3  Warnings...\nWatch Out!....\nReason For Warn : Not Given`"
    )
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat,
                                          filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@friday.on(friday_on_cmd("warn2"))
async def _(event):
    if event.fwd_from:
        return
    mentions = (
        "`You Have  2/3  Warnings...\nWatch Out!....\nReason For Last Warn : Not Given`"
    )
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat,
                                          filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@friday.on(friday_on_cmd("warn3"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`You Have  3/3  Warnings...\nBanned!!!....\nReason For Ban : Not Given`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat,
                                          filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@friday.on(friday_on_cmd("warn0"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`Warning Resetted By Admin...\nYou Have  0/3  Warnings`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat,
                                          filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
