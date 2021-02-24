from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from uniborg.util import friday_on_cmd
from fridaybot.function import convert_to_image, crop_vid, runcmd
from fridaybot import CMD_HELP


@friday.on(friday_on_cmd("mask ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await convert_to_image(event, borg)
    chat = "@hazmat_suit_bot"
    sed = await event.edit("Making mask")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=905164246)
            )
            await borg.send_file(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("```Please unblock @hazmat_suit_bot and try again```")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await sed.delete()
            await borg.send_file(event.chat_id, response.message.media)


CMD_HELP.update(
    {
        "mask": "**Mask**\
\n\n**Syntax : **`.mask <reply to image>`\
\n**Usage :** This funny plugin masks the image."
    }
)
