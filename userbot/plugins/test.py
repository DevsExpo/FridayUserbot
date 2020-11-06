from uniborg.util import friday_on_cmd


@friday.on(friday_on_cmd(pattern=r"test"))
async def test(event):
    if event.fwd_from:
        return
    await event.edit("Test Successfull. Boss !")
