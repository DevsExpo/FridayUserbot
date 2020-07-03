# if you change credits, you get anal cancer and get murdered by russians in 3 days.
"""
Support chatbox for pmpermit.
Used by incoming messages with trigger as /start
Will not work for already approved people.
"""
import asyncio
import io 
import telethon.sync
from telethon.tl.functions.users import GetFullUserRequest
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from telethon import events, errors, functions, types
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in heroku vars"
PREV_REPLY_MESSAGE = {}


@command(pattern=r"\/start", incoming=True)
async def _(event):
    chat_id = event.from_id
    userid = event.sender_id
    if not pmpermit_sql.is_approved(chat_id):
        chat = await event.get_chat()
        if event.fwd_from:
            return
        if event.is_private:
         
         PM = ("`مرحباً.  لقد تم ايصالك إلى القائمة المتاحة للسيد ѕᴀѕᴋᴇ ʟ̤ɾʅ丂ɹɹɹȊɹɹɹ ,`"
               f"{DEFAULTUSER}.\n"
               "__دعونا نجعل هذا سلسًا وأخبرني لماذا أنت هنا ಠ_ಠ__\n"
               "**اختر أحد الأسباب التالية لوجودك هنا (ارسل رقم خيارك):**\n\n"
               "`1`. للدردشة مع سيدي 😺\n"
               "`2`. لازعاج ʟ̤ɾʅ丂ɹɹɹȊɹɹɹ ಠ_ಠ.\n"

               "`3`. للاستفسار عن شيء ما (⌐■_■)\n"
               "`4`. لطلب شيء 🎭\n")
         ONE = ("__حسناً. تم تسجيل طلبك. لا ترسل المزيد من الرسائل المزعجه إلى أستاذي. يمكنك توقع الرد في غضون 24 سنة ضوئية. إنه رجل مشغول ، على عكسك على الأرجح(¬‿¬) .__\n\n"
                "**⚠️ سيتم حظرك والإبلاغ عنك إذا قمت بإرسال رسائل غير مرغوب فيها. ⚠️**\n\n")
         TWO = (" `███████▄▄███████████▄  \n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░█\n██████▀▀▀█░░░░██████▀  \n░░░░░░░░░█░░░░█  \n░░░░░░░░░░█░░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░░▀▀ `\n\n**رائع جداً 🌝🌿، هذا ليس منزلك. اذهب لازعاج شخص آخر. لقد تم حظرك والإبلاغ عنك حتى إشعار آخر 🎭**")
         FOUR = ("__حسناً. لم يطلع سيدي على رسالتك حتى الآن ، وعادةً ما يرد على الأشخاص ، على الرغم من ذلك ساقوم بايصال رسالتك لسيدي🌿 .__\n __سيرد عندما يعود إذا أراد ذلك ، فهناك بالفعل الكثير من الرسائل المعلقة😶__\n **من فضلك لا ترسل شيٌ أخر إلا إذا كنت ترغب في أن يتم حظره والإبلاغ عنك (●'◡'●).**")
         FIVE = ("`حسنا. يرجى الحصول على الأخلاق الأساسية لعدم إزعاج سيدي كثيرا. إذا كان يرغب في مساعدتك ، فسوف يرد عليك قريبًا 👀.`\n**لا تسأل مرارا وتكرارا وإلا سيتم حظرك والإبلاغ عنك.**")
         LWARN = ("**هذا هو التحذير الأخير الخاص بك. لا ترسل رسالة أخرى وإلا سيتم حظرك والإبلاغ عنك. كن صابر. سيدي سوف يرد عليك في اسرع وقت ممكن 🌝🌿.**\n__Use__ `/start` __to go back to the main menu.__")
     
        async with borg.conversation(chat) as conv:
         await borg.send_message(chat, PM)
         chat_id = event.from_id
         response = await conv.get_response(chat)
         y = response.text
         if y == "1":
             await borg.send_message(chat, ONE)
             response = await conv.get_response(chat)
             await event.delete()
             if not response.text == "/start":
                 await response.delete()
                 await borg.send_message(chat, LWARN)
                 response = await conv.get_response(chat)
                 await event.delete()
                 await response.delete()
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "2":
             await borg.send_message(chat, LWARN)
             response = await conv.get_response(chat)
             if not response.text == "/start":
                 await borg.send_message(chat, TWO)
                 await asyncio.sleep(3)
                 await event.client(functions.contacts.BlockRequest(chat_id))
         

         elif y == "3":
             await borg.send_message(chat, FOUR)
             response = await conv.get_response(chat)
             await event.delete()
             await response.delete()
             if not response.text == "/start":
                 await borg.send_message(chat, LWARN)
                 await event.delete()
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "4":
             await borg.send_message(chat,FIVE)
             response = await conv.get_response(chat)
             if not response.text == "/start":
                 await borg.send_message(chat, LWARN)
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         else:
             await borg.send_message(chat, "`لقد قمت بإدخال أمر غير صالح يرجى الإرسال\n🍁 /start 🍁\nمرة أخرى أو عدم إرسال رسالة أخرى إذا كنت لا ترغب في أن يتم حظرك والإبلاغ عنك🌝🌿.`")
             response = await conv.get_response(chat)
             z = response.text
             if not z == "/start":
                 await borg.send_message(chat, LWARN)
                 await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))

