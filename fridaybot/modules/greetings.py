import random
import asyncio
from uniborg.util import friday_on_cmd

from fridaybot import CMD_HELP
from fridaybot.utils import register, edit_or_reply

GDMORNING = (
    "May this morning offer you new hope for life! May you be happy and enjoy every moment of it. Good morning!",
    "A new day has come with so many new opportunities for you. Grab them all and make the best out of your day. Here’s me wishing you a good morning!",
    "Welcome this beautiful morning with a smile on your face. I hope you’ll have a great day today. Wishing you a very good morning!",
    "Mornings come with a blank canvas. Paint it as you like and call it a day. Wake up now and start creating your perfect day. Good morning!",
    "Wake up like the sun every morning and light up the world your awesomeness. You have so many great things to achieve today. Good morning!",
)
GDNIGHT = (
    "Have a very, good night, friend! You are wonderful!",
    "Friend, you do not hesitate to get things done! Take tonight to relax and do more, tomorrow!",
    "Rest soundly tonight, friend!",
    "Good night to a friend who is the best! Get your forty winks!",
    "Let there be no troubles, dear friend! Have a Good Night!",
)

GDNOON = (
    "Good afternoon!",
    "Forget about yesterday, think about tommorow.. The victory will be yours.",
    "Do what you have to do right now.. Good Afternoon.",
)



@friday.on(friday_on_cmd(pattern=r"gmt$"))
async def morning(event):
    if event.fwd_from:
        return    
    txt = random.choice(GDMORNING)
    await friday.edit_or_reply(event, txt)



@friday.on(friday_on_cmd(pattern=r"gnoon$"))
async def noon(event):
    if event.fwd_from:
        return    
    txt = random.choice(GDNOON)
    await friday.edit_or_reply(event, txt)



@friday.on(friday_on_cmd(pattern=r"gnt$"))
async def night(event):
    if event.fwd_from:
        return    
    txt = random.choice(GDNIGHT)
    await friday.edit_or_reply(event, txt)



@friday.on(friday_on_cmd(pattern=r"gdm$"))
async def gm(event):
    if event.fwd_from:
        return    
    await friday.edit_or_reply(
        event,
        "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･\n╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮\n╭━┳━┳━┳╯┃╭━━┳━┳┳┳━┳╋╋━┳┳━╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃╋┃╭┫┃┃┃┃┃┃┃╋┃\n┣╮┣━┻━┻━╯╰┻┻┻━┻╯╰┻━┻┻┻━╋╮┃\n╰━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･",
    )


@friday.on(friday_on_cmd(pattern=r"stysafe$"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("""
 

┏━━┳┓╋╋╋╋╋╋┏━━┓╋╋┏━┓
┃━━┫┗┳━┓┏┳┓┃━━╋━┓┃━╋━┓
┣━━┃┏┫╋┗┫┃┃┣━━┃╋┗┫┏┫┻┫
┗━━┻━┻━━╋┓┃┗━━┻━━┻┛┗━┛
╋╋╋╋╋╋╋╋┗━┛ 𝒲ℯ𝒶𝓇 𝒶 𝓂𝒶𝓈𝓀 😷
        """)


@friday.on(friday_on_cmd(pattern=r"gdn$"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("""
        ｡♥️｡･ﾟ♡ﾟ･｡♥️｡･｡･｡･｡♥️｡･
    ╱╱╱╱╱╱╱╭╮╱╱╱╭╮╱╭╮╭╮
    ╭━┳━┳━┳╯┃╭━┳╋╋━┫╰┫╰╮
    ┃╋┃╋┃╋┃╋┃┃┃┃┃┃╋┃┃┃╭┫
    ┣╮┣━┻━┻━╯╰┻━┻╋╮┣┻┻━╯
    ╰━╯╱╱╱╱╱╱╱╱╱╱╰━╯
        ｡♥️｡･ﾟ♡ﾟ･｡♥️° ♥️｡･ﾟ♡ﾟ
        """)

@friday.on(friday_on_cmd(pattern=r"gdbye$"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 11)

    await event.edit("Thanks for contacting me..\n I'm Going to leave now...")
    animation_chars = [
        "**Bye  🙏\n Ending this chat 😒**",
        "**I'm leaving this chat now  🙏**",
        "You can again contact me anytime you like",
        "**Have a Good Day.. **",
        "Many thanks for chatting with me.. 🙏\n I'm Leaving this chat now..😜 \n Have a good day..\n\n✌️ **LEFT THE CHAT** ✌️",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])



CMD_HELP.update(
    {
        "greetings": ".gdn \
\nUsage: Say Good Night \n\n .gdm \
\nUsage: Say Good Morning \n\n .gnt \
\nUsage: A random Good night text \n\n .gmt \
\nUsage: A random Good Morning text \n\n .stysafe \
\nUsage: Say #StaySafe \n\n .gdbye \
\nUsage: Better way to say Good Bye"
    }
)
