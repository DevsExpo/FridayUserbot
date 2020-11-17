""" Get the Bots in any chat*
Syntax: .bots"""
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantsBots

from fridaybot.utils import friday_on_cmd


@friday.on(friday_on_cmd("bots ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Bots In This Chat** : \n"
    input_str = event.pattern_match.group(1)
    to_write_chat = await event.get_input_chat()
    chat = None
    if not input_str:
        chat = to_write_chat
    else:
        mentions = "Bots In {} Chat : \n".format(input_str)
        try:
            chat = await borg.get_entity(input_str)
        except Exception as e:
            await event.edit(str(e))
            return None
    try:
        async for x in borg.iter_participants(chat, filter=ChannelParticipantsBots):
            if isinstance(x.participant, ChannelParticipantAdmin):
                mentions += "\n ⚜️ [{}](tg://user?id={}) `{}`".format(
                    x.first_name, x.id, x.id
                )
            else:
                mentions += "\n [{}](tg://user?id={}) `{}`".format(
                    x.first_name, x.id, x.id
                )
    except Exception as e:
        mentions += " " + str(e) + "\n"
    await event.edit(mentions)
