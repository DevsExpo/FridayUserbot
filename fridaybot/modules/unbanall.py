from time import sleep

from telethon.tl import functions
from telethon.tl.types import ChannelParticipantsKicked
from uniborg.util import friday_on_cmd


@friday.on(friday_on_cmd(pattern="unbanall ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str:
        logger.info("TODO: Not yet Implemented")
    else:
        if event.is_private:
            return False
        await event.edit("Searching Participant Lists.")
        p = 0
        async for i in borg.iter_participants(
            event.chat_id, filter=ChannelParticipantsKicked, aggressive=True
        ):
            rights = ChatBannedRights(until_date=0, view_messages=False)
            try:
                await borg(
                    functions.channels.EditBannedRequest(event.chat_id, i, rights)
                )
            except FloodWaitError as ex:
                logger.warn("Sleeping For {} Seconds".format(ex.seconds))
                sleep(ex.seconds)
            except Exception as ex:
                await event.edit(str(ex))
            else:
                p += 1
        await event.edit("{} : {} Unbanned!".format(event.chat_id, p))
