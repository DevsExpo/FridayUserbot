# @TechnoAyanOfficial
# Big Thanks To Spechide and ItWaze

"""Corona: Avaible commands: .covid <cname>
"""
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="covid ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@NovelCoronaBot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1124136160)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Boss! Please Unblock (@NovelCoronaBot) ```")
            return
        if response.text.startswith("Country"):
            await event.edit("😶**Country Not Found**😅")
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)
