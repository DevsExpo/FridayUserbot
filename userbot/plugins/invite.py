


from userbot import *
from userbot.utils import admin_cmd
import asyncio, time, io, math, os, logging, asyncio, shutil, re, subprocess, json
from datetime import datetime
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from base64 import b64decode
from pySmartDL import SmartDL
from userbot import TEMP_DOWNLOAD_DIRECTORY, CMD_HELP, COUNTRY, TZ_NUMBER
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
FULL_SUDO = os.environ.get("FULL_SUDO", None)
from telethon.tl import functions, types
from userbot import BOTLOG_CHATID, CMD_HELP, BOTLOG, BOTLOG_CHATID, YOUTUBE_API_KEY, TEMP_DOWNLOAD_DIRECTORY, CHROME_DRIVER, GOOGLE_CHROME_BIN, bot
from telethon.tl.functions.messages import GetHistoryRequest, CheckChatInviteRequest, GetFullChatRequest
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.errors import FloodWaitError
from bs4 import BeautifulSoup
from time import sleep
from html import unescape
from urllib.parse import quote_plus
from urllib.error import HTTPError
from telethon import events
from requests import get
from html import unescape
from re import findall
from asyncio import sleep
from datetime import datetime as dt
from pytz import country_names as c_n, country_timezones as c_tz, timezone as tz
from telethon.errors.rpcerrorlist import YouBlockedUserError
import random


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.reply("`This is a private channel/group or I am banned from there`")
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or Supergroup doesn't exist`")
            return None
        except (TypeError, ValueError) as err:
            await event.reply("`Invalid channel/group`")
            return None
    return chat_info

async def get_tz(con):
    """ Get time zone of the given country. """
    if "(Uk)" in con:
        con = con.replace("Uk", "UK")
    if "(Us)" in con:
        con = con.replace("Us", "US")
    if " Of " in con:
        con = con.replace(" Of ", " of ")
    if "(Western)" in con:
        con = con.replace("(Western)", "(western)")
    if "Minor Outlying Islands" in con:
        con = con.replace("Minor Outlying Islands", "minor outlying islands")
    if "Nl" in con:
        con = con.replace("Nl", "NL")

    for c_code in c_n:
        if con == c_n[c_code]:
            return c_tz[c_code]
    try:
        if c_n[con]:
            return c_tz[con]
    except KeyError:
        return


def make_mention(user):
    if user.username:
        return f"@{user.username}"
    else:
        return inline_mention(user)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = ' '.join(names)
    return full_name
 






@borg.on(admin_cmd(pattern=r"inviteall ?(.*)"))
async def get_users(event):   
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
    else:
    	rkp = await event.edit("`processing...`")
    rk1 = await get_chatinfo(event) ; chat = await event.get_chat()
    if event.is_private:
              return await rkp.edit("`Sorry, Can add users here`")    
    s = 0 ; f = 0 ; error = 'None'   
  
    await rkp.edit("**CɪᴘʜᴇʀX Terminal Status**\n\n`Collecting Users.......`")
    async for user in event.client.iter_participants(rk1.full_chat.id):
                try:
                    if error.startswith("Too"):
                        return await rkp.edit(f"**CɪᴘʜᴇʀX Terminal Finished With Error**\n(`May Got Limit Error from telethon Please try agin Later`)\n**Error** : \n`{error}`\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people")
                    await event.client(functions.channels.InviteToChannelRequest(channel=chat,users=[user.id]))
                    s = s + 1                                                    
                    await rkp.edit(f"**CɪᴘʜᴇʀX Terminal Running...**\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people\n\n**× LastError:** `{error}`")                
                except Exception as e:
                    error = str(e) ; f = f + 1             
    return await rkp.edit(f"**CɪᴘʜᴇʀX Terminal Finished** \n\n• Successfully Invited `{s}` people \n• failed to invite `{f}` people")
