#    Copyright (C) Midhun KM 2020
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
from fridaybot.utils import friday_on_cmd

loggy_grp = Config.PRIVATE_GROUP_ID


@friday.on(friday_on_cmd(pattern="badd ?(.*)"))
async def _(event):
    input_chnnl = event.pattern_match.group(1)
    sed = 0
    oks = 0
    if input_chnnl == "all":
        addall = [
            d.entity
            for d in await event.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        await event.edit("`Adding All Channel TO DB.")
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
        await event.edit(
            f"Process Completed. Added {sed} Channel To List. Failed {oks} Due to already Added !"
        )
        return
    elif input_chnnl == "":
        if event.is_channel and event.is_group:
            input_chnnl = event.chat_id
        else:
            await event.edit("Please Give Group / Channel ID !")
            return
    if already_added(input_chnnl):
        await event.edit("This Channel Already Found in Database.")
        return
    if not already_added(input_chnnl):
        add_chnnl_in_db(input_chnnl)
        await event.edit(f"Fine. I have Added {input_chnnl} To DataBase.")
        await borg.send_message(loggy_grp, f"Added {input_chnnl} To DB")


@friday.on(friday_on_cmd(pattern="brm ?(.*)"))
async def _(event):
    input_chnnl = event.pattern_match.group(1)
    all_chnnl = get_all_chnnl()
    if input_chnnl == "all":
        for channelz in all_chnnl:
            rm_channel(channelz.chat_id)
        await event.edit("Fine. Cleared All Channel Database")
        return
    if input_chnnl is "":
        if event.is_channel and event.is_group:
            input_chnnl = event.chat_id
        else:
            await event.edit("Please Give Group / Channel ID")
            return
    if already_added(input_chnnl):
        rm_channel(input_chnnl)
        await event.edit(f"Fine. I have Removed {input_chnnl} From DataBase.")
        await borg.send_message(loggy_grp, f"Removed {input_chnnl} From DB")
    elif not already_added(input_chnnl):
        await event.edit(
            "Are You Sure? , You Haven't Added This Group / Channel To Database"
        )


@friday.on(friday_on_cmd(pattern="broadcast"))
async def _(event):
    await event.edit("**Fine. Broadcasting in Progress. Kindly Wait !**")
    sedpath = Config.TMP_DOWNLOAD_DIRECTORY
    all_chnnl = get_all_chnnl()
    if len(all_chnnl) == 0:
        await event.edit("No Channel Or Group Found On Database. Please Check Again")
        return
    total_errors = 0
    total_count = 0
    errorno = ""
    total_chnnl = len(all_chnnl)
    if event.reply_to_msg_id:
        hmm = await event.get_reply_message()
    else:
        event.edit("Reply To Some Message.")
        return
    if hmm and hmm.media:
        ok = await borg.download_media(hmm.media, sedpath)
        for channelz in all_chnnl:
            try:
                await borg.send_file(int(channelz.chat_id), file=ok, caption=hmm.text)
                total_count += 1
            except Exception as e:
                total_errors += 1
                errorno += f"{e} \n"
        await borg.send_message(
            loggy_grp,
            f"Error : {total_errors}\nError : {errorno}",
        )
        if os.path.exists(ok):
            os.remove(ok)
    elif hmm and hmm.text:
        for channelz in all_chnnl:
            try:
                await borg.send_message(int(channelz.chat_id), hmm.text)
                total_count += 1
            except Exception as e:
                total_errors += 1
                errorno += f"{e} \n"
        await borg.send_message(
            loggy_grp,
            f"Error : {total_errors}\nError : {errorno}",
        )
    elif hmm.message.poll:
        await event.edit("Bruh, This Can't Be Broadcasted.")
        return
    await event.edit(
        f"BroadCast Success In : {total_count} \nFailed In : {total_errors} \nTotal Channel In DB : {total_chnnl}"
    )
    await borg.send_message(
        loggy_grp,
        f"BroadCast Success In : {total_count} \nFailed In : {total_errors} \nTotal Channel In DB : {total_chnnl}",
    )


@friday.on(friday_on_cmd(pattern="bforward"))
async def _(event):
    all_chnnl = get_all_chnnl()
    if len(all_chnnl) == 0:
        await event.edit("No Channel Or Group Found On Database. Please Check Again")
        return
    total_errors = 0
    total_count = 0
    total_chnnl = len(all_chnnl)
    if event.reply_to_msg_id:
        hmm = await event.get_reply_message()
    else:
        event.edit("Reply To Some Message.")
        return
    try:
        for forbard in all_chnnl:
            await hmm.forward_to(forbard.chat_id)
            total_count += 1
    except Exception as e:
        total_errors += 1
        try:
            logger.info(f"Error : {error_count}\nError : {e} \nUsers : {chat_id}")
        except:
            pass
    await event.edit(
        f"Forward Success in {total_count} And Failed In {total_errors} And Total Channel In Db is {total_chnnl}"
    )
    await borg.send_message(
        loggy_grp,
        f"Forward Success in {total_count} And Failed In {total_errors} And Total Channel In Db is {total_chnnl}",
    )


@friday.on(friday_on_cmd(pattern="bstat"))
async def _(event):
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
        \n\n**Syntax : **`.forward <Reply-To-Msg>`\
        \n**Usage :** Forwards To All Channel in Database.\
        \n\n**Syntax : **`.bstat`\
        \n**Usage :** Shows list of channels/groups in database."
    }
)
