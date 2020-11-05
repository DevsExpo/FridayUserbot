from telethon import events

from userbot import ALIVE_NAME, bot

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = (
    "https://filetolinktelegrambot.herokuapp.com/1996057911608/VID_20200723_004420.mp4"
)
pm_caption = "`➥ CɪᴘʜᴇʀX Super Technology Assistant Bot is:` **Online**\n\n"
pm_caption += "➥ **System Status**\n"
pm_caption += "`➥ Telethon Version:` **6.0.9**\n`Python:` **3.8.5**\n"
pm_caption += "`➥ Database Status:` **AWS Working Properly**\n"
pm_caption += "**➥ Current Branch** : `Master`\n"
pm_caption += "**➥ CɪᴘʜᴇʀX OS** : `Kali GNU/Linux Rolling x86_64`\n"
pm_caption += f"**➥ My Boss** : [CɪᴘʜᴇʀX](https://t.me/Hackintush)\n"
pm_caption += "**✨ CɪᴘʜᴇʀX is the best ✨**"

# only Owner Can Use it
@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def friday(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
