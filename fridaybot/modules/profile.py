"""Profile Updation Commands
.pbio <Bio>
.pname <Name>
.ppic"""
import os
import asyncio
from telethon.tl import functions
from uniborg.util import friday_on_cmd
from fridaybot import CMD_HELP
from telethon import functions, types 


@friday.on(friday_on_cmd(pattern="a2c(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    hmmk = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        hmm = await event.get_reply_message()
        id_s = hmm.sender_id    
    elif event.pattern_match.group(1):
        id_s = event.pattern_match.group(1)
    elif event.is_private:
        id_s = await event.get_input_chat()
    if not id_s:
        await event.edit("`Reply To User To Add Him In Contact.`")
        return
    user_s = await event.client.get_entity(id_s)
    if user_s.last_name is None:
        sed_m = " "
    else:
        sed_m = user_s.last_name
    await event.client(functions.contacts.AddContactRequest(
        id=id_s, 
        first_name=user_s.first_name, 
        last_name=sed_m, 
        phone='123456', 
        add_phone_privacy_exception=True)) 
    star = await event.edit("**Added To Contacts SucessFully**")
    await asyncio.sleep(3)
    await star.delete()   


@friday.on(friday_on_cmd(pattern="pbio (.*)"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    bio = event.pattern_match.group(1)
    try:
        await borg(
            functions.account.UpdateProfileRequest(about=bio)  # pylint:disable=E0602
        )
        await event.edit("Succesfully changed my profile bio")
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))


@friday.on(friday_on_cmd(pattern="pname ((.|\n)*)"))  # pylint:disable=E0602,W0703
async def _(event):
    if event.fwd_from:
        return
    names = event.pattern_match.group(1)
    first_name = names
    last_name = ""
    if "\\n" in names:
        first_name, last_name = names.split("\\n", 1)
    try:
        await borg(
            functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                first_name=first_name, last_name=last_name
            )
        )
        await event.edit("My name was changed successfully")
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))


@friday.on(friday_on_cmd(pattern="ppic"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    await event.edit("Downloading Profile Picture to my local ...")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):  # pylint:disable=E0602
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)  # pylint:disable=E0602
    photo = None
    try:
        photo = await borg.download_media(  # pylint:disable=E0602
            reply_message, Config.TMP_DOWNLOAD_DIRECTORY  # pylint:disable=E0602
        )
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))
    else:
        if photo:
            await event.edit("now, Uploading to @Telegram ...")
            file = await borg.upload_file(photo)  # pylint:disable=E0602
            try:
                await borg(
                    functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                        file
                    )
                )
            except Exception as e:  # pylint:disable=C0103,W0703
                await event.edit(str(e))
            else:
                await event.edit("My profile picture was succesfully changed")
    try:
        os.remove(photo)
    except Exception as e:  # pylint:disable=C0103,W0703
        logger.warn(str(e))  # pylint:disable=E0602


CMD_HELP.update(
    {
        "profile": "**Profile**\
\n\n**Syntax : **`.pbio <text>`\
\n**Usage :** Changes your bio with given text.\
\n\n**Syntax : **`.pname <text>`\
\n**Usage :** Changes your name with given text.\
\n\n**Syntax : **`.ppic <reply to a picture>`\
\n**Usage :** changes your profile pic with replyed pic."
    }
)
