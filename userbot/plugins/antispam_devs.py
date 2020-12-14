import secrets

from userbot import sclient
from userbot.utils import admin_cmd

"""This Is Only For Devs Of AntispamInc, Needs Root Permissions // @AntispamInc"""


@borg.on(admin_cmd(pattern="benheck(?: |$)(.*)"))
async def oki(event):
    await event.edit("`Processing...`")
    extra = None
    args = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif args:
        args = event.pattern_match.group(1).split(" ", 1)
        userz = args[0]
        if userz.isnumeric():
            user = int(userz)
        else:
            await event.edit("Provide User-ID Not Username.")
            return
        if len(args) == 2:
            extra = args[1]
        if extra == None:
            await event.edit("Reason Can't Be None")
            return
        elif extra == "":
            await event.edit("Reason Can't Be None")
            return
        if not user:
            await event.edit("Reply To User Or Mention a User.")
            return
    try:
        sclient.ban(user, extra)
        await borg.send_message("CɪᴘʜᴇʀX Anti-Spam Algorithm", f"/fban {user} {extra}")
        await event.edit(
            f"**User :** `{user}` \n**Reason :** `{extra}` \n**Banned Sucessfully !**"
        )
    except Exception as e:
        await event.edit("Errors : " + str(e))


@borg.on(admin_cmd(pattern="heck(?: |$)(.*)"))
async def oka(event):
    await event.edit("`Processing...`")
    args = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user = await event.client.get_entity(previous_message.sender_id)
    elif args:
        userz = args
        if userz.isnumeric():
            user = int(userz)
        else:
            await event.edit("Fuck, Gib ID")
            return
        if not user:
            await event.edit("Reply To User Or Mention a User.")
            return
    gensys2 = sclient.unban(user)
    await borg.send_message("CɪᴘʜᴇʀX Anti-Spam Algorithm", f"/unfban {user}")
    if gensys2["error"] == True:
        await event.edit("Error : " + gensys2["full"])
    else:
        await event.edit(f"**User :** `{user}` \n**UnBanned Sucessfully !**")


@borg.on(admin_cmd(pattern="nt"))
async def tokens(event):
    await event.edit("`Processing...`")
    okbabe = secrets.token_urlsafe(16)
    skynet = sclient.new_token(okbabe)
    if skynet["error"] == True:
        await event.edit("Error : " + gensys2["full"])
    else:
        await event.edit(f"**New Token** \n**Token** : `{okbabe}`")


@borg.on(admin_cmd(pattern="massbenheck(?: |$)(.*)"))
async def oki(event):
    lmaoded = []
    lol = event.pattern_match.group(1)
    stark = lol.split(" ", 1)
    noteme = stark[0]
    errorz = ""
    lolsed = stark[1]
    async for user in borg.iter_participants(noteme):
        lmaoded.append(user.id)
    for i in lmaoded:
        try:
            sclient.ban(i, lolsed)
            await borg.send_message("CɪᴘʜᴇʀX Anti-Spam Algorithm", f"/fban {i} {lolsed}")
        except:
            errorz += 1
        await event.edit(
            f"**User :** `{i}` \n**Banned Sucessfully !** \n**Failed :** `{len(errorz)}`"
        )
    await event.edit("**DONE !**")
