"""QuotLy: Avaible commands: .qbot
"""
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import bot
from userbot.utils import admin_cmd


# @register(outgoing=True, pattern="^.q(?: |$)(.*)")
@borg.on(admin_cmd(pattern=r"q(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```İstənilən istifadəçi mesajına cavab verin.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```İstənilən istifadəçi mesajına cavab verin.```")
        return
    chat = "@QuotLyBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```İstənilən istifadəçi mesajına cavab verin.```")
        return
    await event.edit("```Hazırlanır...```")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1031952739)
            )
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply(
                "```Xahiş edirəm @QuotLyBot-un blokundan çıxartın və yenidən cəhd edin```"
            )
            return
        if response.text.startswith("Hi!"):
            await event.edit(
                "```İrəli gizlilik ayarlarınızı xeyirxahlıqla söndürə bilərsinizmi?```"
            )
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)
