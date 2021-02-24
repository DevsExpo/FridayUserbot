#    Copyright (C) @DevsExpo 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from telethon import functions
from fridaybot.utils import friday_on_cmd
from telethon import functions
from fridaybot import CMD_HELP
from telethon.tl.types import Channel, Chat, User
from fridaybot.utils import friday_on_cmd
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd
import asyncio
import datetime
from datetime import datetime
from telethon import events
from telethon.tl import functions, types
import io
import os
from fridaybot import CMD_HELP
from fridaybot.Configs import Config
from fridaybot.modules.sql_helper.broadcast_sql import (
    add_chnnl_in_db,
    already_added,
    get_all_chnnl,
    rm_channel,
)
import asyncio
import html
from telethon.tl import functions
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd
loggy_grp = Config.PRIVATE_GROUP_ID
from fridaybot import CMD_HELP

global USER_AFK
global afk_time
global last_afk_message
global afk_start
global afk_end
USER_AFK = {}
afk_time = None
last_afk_message = {}
afk_start = {}

@friday.on(friday_on_cmd(pattern="invite ?(.*)"))
@friday.on(sudo_cmd(pattern="invite ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    id_f = event.pattern_match.group(1)
    kk = await friday.edit_or_reply(event, "`Processing...`")
    if event.is_private:
        await kk.edit("`This Plugin Only Works In Groups!`")
        return
    user_id = int(id_f) if id_f.isdigit() else str(id_f)
    if event.is_group:
        try:
            await kk.edit(f"`Trying To Add {user_id} !`")
            await event.client(
                        functions.messages.AddChatUserRequest(
                            chat_id=event.chat_id, user_id=user_id, fwd_limit=0
                        )
                    )
        except Exception as e:
            await kk.edit(f"`Failed To Add : {user_id} ! \nReason : {e}`")
            return
    else:
        try:
            await kk.edit(f"`Trying To Add {user_id} !`")
            await event.client(
                        functions.channels.InviteToChannelRequest(
                            channel=event.chat_id, users=[user_id]
                        )
                    )
        except Exception as e:
            await kk.edit(f"`Failed To Add : {user_id} ! \nReason : {e}`")
            return
        
afk_cmd = str(Config.COMMAND_HAND_LER) + "afk ?(.*)"
@friday.on(
    events.NewMessage(pattern=afk_cmd, outgoing=True)
)
async def _(event):
    if event.fwd_from:
        return
    global USER_AFK
    global afk_time
    global last_afk_message
    global afk_start
    global afk_end
    global reason
    USER_AFK = {}
    afk_time = None
    last_afk_message = {}
    afk_end = {}
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    reason = event.pattern_match.group(1)
    if not USER_AFK:
        last_seen_status = await event.client(
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            afk_time = datetime.datetime.now()
        USER_AFK = f"yes: {reason}"
        if reason:
            await borg.send_message(
                event.chat_id,
                f"**My Master Seems To Be Too Busy 👀.** \n__He Going Afk Because Of__ `{reason}`",
            )
        else:
            await borg.send_message(event.chat_id, f"**I Am Busy And I Am Going Afk**.")
        await asyncio.sleep(5)
        await event.delete()
        try:
            await borg.send_message(
                Config.PRIVATE_GROUP_ID,
                f"#AfkLogger Afk Is Active And Reason is {reason}",
            )
        except Exception as e:
            logger.warn(str(e))

@friday.on(events.NewMessage(outgoing=True))
async def set_not_afk(event):
    global USER_AFK  
    global afk_time  
    global last_afk_message  
    global afk_start
    global afk_end
    back_alive = datetime.now()
    afk_end = back_alive.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message = event.message.message
    if ".afk" not in current_message and "yes" in USER_AFK:  
        shite = await borg.send_message(
            event.chat_id,
            "__Pro is Back Alive__\n**No Longer afk.**\n `I Was afk for:``"
            + total_afk_time
            + "`",
        )
        try:
            await borg.send_message(  
                Config.PRIVATE_GROUP_ID,  
                "#AfkLogger User is Back Alive ! No Longer Afk ",
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await borg.send_message(  
                event.chat_id,
                "Please set `PRIVATE_GROUP_ID` "
                + "for the proper functioning of afk functionality "
                + "Please Seek Support in @FridayOT\n\n `{}`".format(str(e)),
                reply_to=event.message.id,
                silent=True,
            )
        await asyncio.sleep(10)
        await shite.delete()
        USER_AFK = {}  
        afk_time = None  


@friday.on(
    events.NewMessage(  
        incoming=True, func=lambda e: bool(e.mentioned or e.is_private)
    )
)
async def on_afk(event):
    if event.fwd_from:
        return
    global USER_AFK  
    global afk_time  
    global last_afk_message  
    global afk_start
    global afk_end
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    afk_since = "**a while ago**"
    current_message_text = event.message.message.lower()
    if "afk" in current_message_text:
        return False
    if USER_AFK and not (await event.get_sender()).bot:  
        if afk_time:  
            now = datetime.datetime.now()
            datime_since_afk = now - afk_time  
            time = float(datime_since_afk.seconds)
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                afk_since = "**Yesterday**"
            elif days > 1:
                if days > 6:
                    date = now + datetime.timedelta(
                        days=-days, hours=-hours, minutes=-minutes
                    )
                    afk_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-days)
                    wday.strftime("%A")
            elif hours > 1:
                f"`{int(hours)}h{int(minutes)}m` **ago**"
            elif minutes > 0:
                f"`{int(minutes)}m{int(seconds)}s` **ago**"
            else:
                f"`{int(seconds)}s` **ago**"
        msg = None
        message_to_reply = (f"I Am **[AFK]** Right Now. \n**Last Seen :** `{total_afk_time}`\n**Reason** : `{reason}`" if reason else f"I Am **[AFK]** Right Now. \n**Last Seen :** `{total_afk_time}`")
        msg = await event.reply(message_to_reply)
        await asyncio.sleep(10)
        # Spechide Bad
        await msg.delete()
        if event.chat_id in last_afk_message:  
            await last_afk_message[event.chat_id].delete()  
        last_afk_message[event.chat_id] = msg  


CMD_HELP.update(
    {
        "afk": ".afk <Reason> \
\nUsage: Gets You Afk"
    }
)
CMD_HELP.update(
    {
        "add": "**Add**\
\n\n**Syntax : **`.add <user_id or user-name>`\
\n**Usage :** Adds User To Group"
    }
)

@friday.on(friday_on_cmd(pattern="badd ?(.*)"))
@friday.on(sudo_cmd(pattern="badd ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_chnnl = event.pattern_match.group(1)
    sed = 0
    oks = 0
    if input_chnnl == "all":
        poppo = await friday.edit_or_reply(event, "`Adding All Channel TO DB.`")
        addall = [
            d.entity
            for d in await event.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in addall:
            try:
                if i.broadcast:
                    if i.creator or i.admin_rights:
                        if already_added(i.id):
                            oks += 1
                        else:
                            add_chnnl_in_db(i.id)
                            sed += 1
            except BaseException:
                pass
        await poppo.edit(f"Process Completed. Added {sed} Channel To List. Failed {oks} Due to already Added !")
        return
    elif input_chnnl == "":
        if event.is_channel and event.is_group:
            input_chnnl = event.chat_id
        else:
            await friday.edit_or_reply(event, "Please Give Group / Channel ID !")
            return
    if already_added(input_chnnl):
        await friday.edit_or_reply(event, "This Channel Already Found in Database.")
        return
    if not already_added(input_chnnl):
        add_chnnl_in_db(input_chnnl)
        M = f"Fine. I have Added {input_chnnl} To DataBase."
        Ml = f"Added {input_chnnl} To DB"
        await friday.edit_or_reply(event, M)
        await borg.send_message(loggy_grp, Ml)


@friday.on(friday_on_cmd(pattern="brm ?(.*)"))
@friday.on(sudo_cmd(pattern="brm ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_chnnl = event.pattern_match.group(1)
    all_chnnl = get_all_chnnl()
    if input_chnnl == "all":
        for channelz in all_chnnl:
            rm_channel(channelz.chat_id)
        await friday.edit_or_reply(event, "Fine. Cleared All Channel Database")
        return
    if input_chnnl == "":
        if event.is_channel and event.is_group:
            input_chnnl = event.chat_id
        else:
            await friday.edit_or_reply(event, "Please Give Group / Channel ID")
            return
    if already_added(input_chnnl):
        rm_channel(input_chnnl)
        await friday.edit_or_reply(event, f"Fine. I have Removed {input_chnnl} From DataBase.")
        await borg.send_message(loggy_grp, f"Removed {input_chnnl} From DB")
    elif not already_added(input_chnnl):
        await friday.edit_or_reply(event, 
            "Are You Sure? , You Haven't Added This Group / Channel To Database"
        )


@friday.on(friday_on_cmd(pattern="broadcast$"))
@friday.on(sudo_cmd(pattern="broadcast$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    poppo = await friday.edit_or_reply(event, "**Fine. Broadcasting in Progress. Kindly Wait !**")
    sedpath = Config.TMP_DOWNLOAD_DIRECTORY
    all_chnnl = get_all_chnnl()
    if len(all_chnnl) == 0:
        await poppo.edit("No Channel Or Group Found On Database. Please Check Again")
        return
    total_errors = 0
    total_count = 0
    errorno = ""
    total_chnnl = len(all_chnnl)
    if event.reply_to_msg_id:
        hmm = await event.get_reply_message()
    else:
        await poppo.edit("Reply To Some Message.")
        return
    if hmm and hmm.media:
        for channelz in all_chnnl:
            try:
                await borg.send_file(int(channelz.chat_id), file=hmm.media, caption=hmm.text)
                total_count += 1
            except Exception as e:
                total_errors += 1
        if os.path.exists(ok):
            os.remove(ok)
    elif hmm and hmm.text:
        for channelz in all_chnnl:
            try:
                await borg.send_message(int(channelz.chat_id), hmm.text)
                total_count += 1
            except Exception as e:
                total_errors += 1
    elif hmm.message.poll:
        await poppo.edit("`Bruh, This Can't Be Broadcasted!`")
        return
    await poppo.edit(
        f"BroadCast Success In : {total_count} \nFailed In : {total_errors} \nTotal Channel In DB : {total_chnnl}"
    )
    try:
        await borg.send_message(
            loggy_grp,
            f"BroadCast Success In : {total_count} \nFailed In : {total_errors} \nTotal Channel In DB : {total_chnnl}",
        )
    except:
        pass

@friday.on(friday_on_cmd(pattern="bforward$"))
@friday.on(sudo_cmd(pattern="bforward$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    all_chnnl = get_all_chnnl()
    if len(all_chnnl) == 0:
        await friday.edit_or_reply(event, "No Channel Or Group Found On Database. Please Check Again")
        return
    total_errors = 0
    total_count = 0
    errorno = ""
    total_chnnl = len(all_chnnl)
    if event.reply_to_msg_id:
        hmm_k = await event.get_reply_message()
    else:
        await friday.edit_or_reply(event, "Reply To Some Message.")
        return
    for forbard in all_chnnl:
        try:
            await hmm_k.forward_to(forbard.chat_id)
            total_count += 1
        except:
            total_errors += 1
    poppo = await friday.edit_or_reply(event, 
        f"Forward Success in {total_count} And Failed In {total_errors} And Total Channel In Db is {total_chnnl}"
    )
    try:
        await borg.send_message(
            loggy_grp,
            f"Forward Success in {total_count} And Failed In {total_errors} And Total Channel In Db is {total_chnnl}",
        )
    except:
        pass

@friday.on(friday_on_cmd(pattern="bstat$"))
@friday.on(sudo_cmd(pattern="bstat$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    total_chnnl = get_all_chnnl()
    chnnl_list = ""
    for starked in total_chnnl:
        try:
            chnnl_list += ("==> {} \n").format(starked.chat_id)
        except Exception:
            pass
    with io.BytesIO(str.encode(chnnl_list)) as tedt_file:
        tedt_file.name = "dbchnnllist.txt"
        await borg.send_file(
            event.chat_id,
            tedt_file,
            force_document=True,
            caption="Total Channel In DB.",
            allow_cache=False,
        )


CMD_HELP.update(
    {
        "broadcast": "**broadcast**\
        \n\n**Syntax : **`.badd <channel_id>`\
        \n**Usage :** Adds the given channel/group to database.\
        \n\n**Syntax : **`.badd all`\
        \n**Usage :** Adds all the channel/groups to database where you are admin.\
        \n\n**Syntax : **`.brm <channel_id>`\
        \n**Usage :** Removes the Specified Channel From database.\
        \n\n**Syntax : **`.brm all`\
        \n**Usage :** Removes Everything From DataBase.\
        \n\n**Syntax : **`.broadcast <Reply-To-Msg>`\
        \n**Usage :**  Broadcasts To All Channel in DB, Even Supports Media.\
        \n\n**Syntax : **`.bforward <Reply-To-Msg>`\
        \n**Usage :** Forwards To All Channel in Database.\
        \n\n**Syntax : **`.bstat`\
        \n**Usage :** Shows list of channels/groups in database."
    }
)
#!/usr/bin/env python3
# -*- coding: utf-8 -*
# (c) Shrimadhav U K


@borg.on(friday_on_cmd(pattern="cr (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    try:
        input_entity = await event.client.get_entity(input_str)
    except Exception:
        await event.edit("`Hmm...`")
        return
    else:
        await event.edit(get_restriction_string(input_entity))


def get_restriction_string(a) -> str:
    # logger.info(a.stringify())
    b = ""
    c = ""
    if isinstance(a, Channel):
        c = f"[{a.title}](https://t.me/c/{a.id}/{2})"
    elif isinstance(a, User):
        c = f"[{a.first_name}](tg://user?id={a.id})"
    elif isinstance(a, Chat):
        c = f"{a.title}"
        b = f"{c}: __basic groups do not have restriction in Telegram__, **to the best of our knowledge**"
        return b
    else:
        c = "something wnorgings while checking restriction_reason 😒😒"
    if a.restriction_reason is None or len(a.restriction_reason) == 0:
        b = f"{c}: **Good News**! No Limitations are currently applied to this Group / Channel / Bot"
    else:
        tmp_string = f"{c} has the following restriction_reason(s): \n"
        for a_r in a.restriction_reason:
            tmp_string += f"👉 {a_r.reason}-{a_r.platform}: {a_r.text}\n\n"
        b = tmp_string
    # b += "\n\n" + Translation.POWERED_BY_SE
    return b
    
@friday.on(friday_on_cmd(pattern="clone ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    replied_user, error_i_a = await get_full_user(event)
    if replied_user is None:
        await event.edit(str(error_i_a))
        return False
    user_id = replied_user.user.id
    profile_pic = await event.client.download_profile_photo(
        user_id, Config.TMP_DOWNLOAD_DIRECTORY
    )
    # some people have weird HTML in their names
    first_name = html.escape(replied_user.user.first_name)
    # https://stackoverflow.com/a/5072031/4723940
    # some Deleted Accounts do not have first_name
    if first_name is not None:
        # some weird people (like me) have more than 4096 characters in their names
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.user.last_name
    # last_name is not Manadatory in @Telegram
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
        last_name = "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
    # giving myself credits cause y not
    user_bio = replied_user.about
    if user_id == 1263617196:
        await event.edit("Sorry, can't clone my Dev")
        await asyncio.sleep(3)
        return
    if user_bio is not None:
        user_bio = html.escape(replied_user.about)
    await borg(functions.account.UpdateProfileRequest(first_name=first_name))
    await borg(functions.account.UpdateProfileRequest(last_name=last_name))
    await borg(functions.account.UpdateProfileRequest(about=user_bio))
    pfile = await borg.upload_file(profile_pic)  # pylint:disable=E060
    await borg(
        functions.photos.UploadProfilePhotoRequest(pfile)  
    )
    # message_id_to_reply = event.message.reply_to_msg_id
    # if not message_id_to_reply:
    #    message_id_to_reply = event.message.id
    # await borg.send_message(
    #  event.chat_id,
    #  "Hey ? Whats Up !",
    #  reply_to=message_id_to_reply,
    #  )
    await event.delete()
    await borg.send_message(
        event.chat_id, "**LET US BE AS ONE**", reply_to=reply_message
    )


async def get_full_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(
                    previous_message.forward.sender_id
                    or previous_message.forward.channel_id
                )
            )
            return replied_user, None
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
            return replied_user, None
    else:
        input_str = None
        try:
            input_str = event.pattern_match.group(1)
        except IndexError as e:
            return None, e
        if event.message.entities is not None:
            mention_entity = event.message.entities
            probable_user_mention_entity = mention_entity[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            else:
                try:
                    user_object = await event.client.get_entity(input_str)
                    user_id = user_object.id
                    replied_user = await event.client(GetFullUserRequest(user_id))
                    return replied_user, None
                except Exception as e:
                    return None, e
        elif event.is_private:
            try:
                user_id = event.chat_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e
        else:
            try:
                user_object = await event.client.get_entity(int(input_str))
                user_id = user_object.id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e


CMD_HELP.update(
    {
        "clone": "**Clone**\
\n\n**Syntax : **`.clone <@username/tag anyone>`\
\n**Usage :** Get Telegram Profile Picture and other information and set as own profile."
    }
)
    
