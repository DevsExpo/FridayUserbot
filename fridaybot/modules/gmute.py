import asyncio

from fridaybot.modules.sql_helper.mute_sql import is_muted
from fridaybot.modules.sql_helper.mute_sql import mute
from fridaybot.modules.sql_helper.mute_sql import unmute


@command(outgoing=True, pattern=r"^.gmute ?(\d+)?")
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Unexpected Issues Or Ugly Errors May Occur!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit(
            "Please Reply To A User Or Add Their Into The Command To Gmute Them."
        )
    event.chat_id
    await event.get_chat()
    if is_muted(userid, "gmute"):
        return await event.edit("This User Is Already Gmuted!")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("Successfully Gmuted That Nigga!")


@command(outgoing=True, pattern=r"^.ungmute ?(\d+)?")
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Unexpected Issues Or Ugly Errors May Occur!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit(
            "Please Reply To A User Or Add Their Into The Command To Ungmute Them."
        )
    event.chat_id
    if not is_muted(userid, "gmute"):
        return await event.edit("This User Is Not Gmuted!")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("Successfully Ungmuted That Nigga!")


@command(outgoing=True, pattern=r"^.gmute ?(\d+)?", allow_sudo=True)
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Unexpected Issues Or Ugly Errors May Occur!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit(
            "Please Reply To A User Or Add Their Into The Command To Gmute Them."
        )
    event.chat_id
    await event.get_chat()
    if is_muted(userid, "gmute"):
        return await event.edit("This User Is Already Gmuted!")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("Successfully Gmuted That Nigga")


@command(outgoing=True, pattern=r"^.ungmute ?(\d+)?", allow_sudo=True)
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Unexpected Issues Or Ugly Errors May Occur!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit(
            "Please Reply To A User Or Add Their Into The Command To Ungmute Them."
        )
    event.chat_id
    if not is_muted(userid, "gmute"):
        return await event.edit("This User Is Not Gmuted")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("Successfully Ungmuted That Nigga")


@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()
