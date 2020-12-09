from telethon import events


@borg.on(events.NewMessage(pattern=r"^.note (.*)", outgoing=True))
async def test(event):
    if event.fwd_from:
        return
    uwu = event.pattern_match.group(1)
    await event.edit("Added note to notes".format(uwu))
    await borg.send_message("CɪᴘʜᴇʀX", "#notes {}".format(uwu))
