import secrets

from fridaybot import sclient
from fridaybot.utils import admin_cmd

json_codes = {
    'nsX01': 'Pornography - High Risk',
    'nsX02': 'Spammer - High Risk',
    'nsX03': 'Spam Adding Users - High Risk',
    'nsX04': 'Raid Participants - High Risk',
    'nsX05': 'Licence violation - Low Risk',
    'nsX06': 'Spam Bot - High Risk',
    'nsX07': 'Flood - High Risk',
    'nsX08': 'Malware - High Risk',
    'nsX09': 'PM Spam - High Risk',
    'nsX10': 'Power Misuser - Medium Risk',
    'nsX11': 'Multiple Risks - Extreme Risk',
    'nsX12': 'Scam - Extreme Risk'
}


@borg.on(admin_cmd(pattern="nspban(?: |$)(.*)"))
async def oki(event):
    if event.fwd_from:
        return
    await event.edit("`Processing...`")
    extra = None
    args = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user = await borg.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif args:
        args = event.pattern_match.group(1).split(" ", 1)
        userz = args[0]
        if userz.isnumeric():
            user = int(userz)
        else:
            try:
                userm = await event.client(GetFullUserRequest(userz))
                user = userm.user.id
            except:
                await event.edit("<i>No User Found.</i>", parse_mode="HTML")
                return
        if len(args) == 2:
            extra = args[1]
        if not json_codes.get(extra):
            await event.edit('`Please Use Valid Ban Codes.`')
            return
        if not user:
            await event.edit("Reply To User Or Mention a User.")
            return
    try:
        sclient.ban(user, extra)
        await borg.send_message("nospamplusfed", f"/fban {user} {extra} {json_codes[extra]}")
        await event.edit(
            f"**User :** `{user}` \n**Reason :** `{extra} {json_codes[extra]}` \n**Banned Sucessfully !**"
        )
    except Exception as e:
        await event.edit("**Errors : **" + str(e))


@borg.on(admin_cmd(pattern="nspuban(?: |$)(.*)"))
async def oka(event):
    if event.fwd_from:
        return
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
            try:
                userm = await event.client(GetFullUserRequest(userz))
                user = userm.user.id
            except:
                await event.edit("<i>No User Found.</i>", parse_mode="HTML")
                return
        if not user:
            await event.edit("Reply To User Or Mention a User.")
            return
    try:
        gensys2 = sclient.unban(user)
        await borg.send_message("nospamplusfed", f"/unfban {user}")
        await event.edit(f"**User :** `{user}` \n**UnBanned Sucessfully !**")
    except Exception as e:
        await event.edit("**Errors : **" + str(e))

@borg.on(admin_cmd(pattern="generatetoken"))
async def tokens(event):
    if event.fwd_from:
        return
    await event.edit("`Processing...`")
    okbabe = secrets.token_urlsafe(16)
    try:
        skynet = sclient.new_token(okbabe)
        await event.edit(f"**New Token** \n**Token** : `{okbabe}`")
    except Exception as e:
        await event.edit("**Errors : **" + str(e))
