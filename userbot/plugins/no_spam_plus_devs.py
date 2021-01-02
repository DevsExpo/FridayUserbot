import secrets

from userbot import sclient
from userbot.utils import admin_cmd

json_codes = {
    "nsX01": "Pornography - High Risk",
    "nsX02": "Spammer - High Risk",
    "nsX03": "Spam Adding Users - High Risk",
    "nsX04": "Raid Participants - High Risk",
    "nsX05": "Licence violation - Low Risk",
    "nsX06": "Spam Bot - High Risk",
    "nsX07": "Flood - High Risk",
    "nsX08": "Malware - High Risk",
    "nsX09": "PM Spam - High Risk",
    "nsX10": "Power Misuser - Medium Risk",
    "nsX11": "Multiple Risks - Extreme Risk",
}


@borg.on(admin_cmd(pattern="nspban(?: |$)(.*)"))
async def oki(event):
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
            await event.edit("`Please Use Valid Ban Codes.`")
            return
        if not user:
            await event.edit("Reply To User or Mention a User.")
            return
    try:
        sclient.ban(user, extra)
        await borg.send_message(
            "CɪᴘʜᴇʀX Anti-Spam Algorithm", f"/fban {user} {extra} {json_codes[extra]}"
        )
        await event.edit(
            f"**User :** `{user}` \n**Reason :** `{extra} {json_codes[extra]}` \n**Banned Sucessfully !**"
        )
    except Exception as e:
        await event.edit("**Errors : **" + str(e))


@borg.on(admin_cmd(pattern="nspuban(?: |$)(.*)"))
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
            try:
                userm = await event.client(GetFullUserRequest(userz))
                user = userm.user.id
            except:
                await event.edit("<i>No Users Found.</i>", parse_mode="HTML")
                return
        if not user:
            await event.edit("Reply To User or Mention a User.")
            return
    try:
        sclient.unban(user)
        await borg.send_message("CɪᴘʜᴇʀX Anti-Spam Algorithm", f"/unfban {user}")
        await event.edit(f"**User :** `{user}` \n**UnBanned Sucessfully !**")
    except Exception as e:
        await event.edit("**Errors : **" + str(e))


@borg.on(admin_cmd(pattern="generatetoken"))
async def tokens(event):
    await event.edit("`Processing...`")
    okbabe = secrets.token_urlsafe(16)
    try:
        sclient.new_token(okbabe)
        await event.edit(f"**New Token** \n**Token** : `{okbabe}`")
    except Exception as e:
        await event.edit("**Errors : **" + str(e))
