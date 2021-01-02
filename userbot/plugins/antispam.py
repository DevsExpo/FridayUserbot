from telethon.events import ChatAction

from userbot import bot, sclient
from userbot.Configs import Config

"""Bans Spammers/Scammer At time Of Arrival 
If You Add Him The Bot Won't Restrict."""


@borg.on(ChatAction)
async def ok(event):
    juser = await event.get_user()
    if Config.ANTISPAM_FEATURE != "ENABLE":
        return
    if event.user_joined:
        hmmyep = await borg.get_permissions(event.chat_id, bot.uid)
        if not hmmyep.is_admin:
            return
        user = sclient.is_banned(juser.id)
        if user:
            await event.reply(
                f"**CɪᴘʜᴇʀX Anti-Spam Algorithm** \n**Detected Malicious User.** \n**User-ID :** `{juser.id}`  \n**Reason :** `{user.ban_code} - {user.reason}`"
            )
            try:
                await borg.edit_permissions(
                    event.chat_id, juser.id, view_messages=False
                )
            except:
                pass
        else:
            pass


@borg.on(ChatAction)
async def dnamg(event):
    okbruh = await borg.get_me()
    if event.user_added == okbruh.id:
        event.chat_id
        lolll = await event.get_added_by()
        added_bys = lolll.id
        lolchat = await event.get_chat()
        if lolchat.username:
            is_pvt = False
            lmao_info = lolchat.username
        else:
            is_pvt = True
            lmao_info = lolchat.id
        try:
            await event.reply(
                "**Wait, How Dare You Add Me To This Group, Without My Permission, Never Mind You Are Gonna Get Reported Lol !**"
            )
        except:
            pass
        await borg.kick_participant(event.chat_id, okbruh.id)
        await borg.send_message(
            Config.PRIVATE_GROUP_ID,
            f"**WARNING - SPAM ADDING** \nUSER : `{added_bys}` \nCHAT : `{lmao_info}` \nGROUP PRIVATE : `{is_pvt}`",
        )
