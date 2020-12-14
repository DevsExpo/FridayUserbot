# Original complied by @Hackintush

import asyncio
import time
from collections import deque

from telethon import events
from uniborg.util import friday_on_cmd

from userbot import CMD_HELP
from userbot.utils import friday_on_cmd, register


@friday.on(events.NewMessage(pattern=r"\.slash", outgoing=True))
async def kek(keks):
    """ Check yourself ;)"""
    uio = ["/", "\\"]
    for i in range(1, 15):
        time.sleep(0.3)
        await keks.edit(":" + uio[i % 2])


@friday.on(events.NewMessage(pattern=r"\.para", outgoing=True))
async def kek(keks):
    """ Check yourself ;)"""
    uio = [")", "("]
    for i in range(1, 15):
        time.sleep(0.3)
        await keks.edit(":" + uio[i % 2])


@friday.on(events.NewMessage(pattern=r"\.question", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("?¿?¿?¿"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.oof", outgoing=True))
async def Oof(e):
    t = "Oof"
    for j in range(15):
        t = t[:-1] + "of"
        await e.edit(t)


@friday.on(events.NewMessage(pattern=r"\.motion", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 20)
    animation_chars = ["▮", "▯", "▬", "▭", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@friday.on(events.NewMessage(pattern=r"\.square", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 20)
    animation_chars = ["◧", "◨", "◧", "◨", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@friday.on(events.NewMessage(pattern=r"\.up", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 20)
    animation_chars = ["╹", "╻", "╹", "╻", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@friday.on(events.NewMessage(pattern=r"\.round", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 20)
    animation_chars = ["⚫", "⬤", "●", "∘", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@friday.on(events.NewMessage(pattern=r"\.cipherx", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 11)
    animation_chars = [
        "**===================**\n      **CɪᴘʜᴇʀX Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 10%\n\n    ●○○○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 5.9%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 8.13GB\n    **🔹used:** 33.77GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 158.98GB\n    **🔹recv:** 146.27GB\n    **🔹sent_packets:** 84518799\n    **🔹recv_packets:** 159720314\n\n\n**===================**\n",
        "**===================**\n      **CɪᴘʜᴇʀX Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 30%\n\n    ●●●○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 20.4%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 7.18GB\n    **🔹used:** 28.26GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 146.27GB\n    **🔹recv:** 124.33GB\n    **🔹sent_packets:** 54635686\n    **🔹recv_packets:** 143565654\n\n\n**===================**\n",
        "**===================**\n      **CɪᴘʜᴇʀX Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 60%\n\n    ●●●●●●○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 60.9%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 6.52GB\n    **🔹used:** 35.78GB\n    **🔹total:** 60.0GB\n    \n    ●●●○○○○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 124.33GB\n    **🔹recv:** 162.48GB\n    **🔹sent_packets:** 25655655\n    **🔹recv_packets:** 165289456\n\n\n**===================**\n",
        "**===================**\n      **CɪᴘʜᴇʀX Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 100%\n\n    ●●●●●●●●●●\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 100.0%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 9.81GB\n    **🔹used:** 30.11GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 162.48GB\n    **🔹recv:** 175.75GB\n    **🔹sent_packets:** 56565435\n    **🔹recv_packets:** 135345655\n\n\n**===================**\n",
        "**===================**\n      **CɪᴘʜᴇʀX Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 70%\n\n    ●●●●●●●○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 80.4%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 5.76GB\n    **🔹used:** 29.35GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 175.75GB\n    **🔹recv:** 118.55GB\n    **🔹sent_packets:** 36547698\n    **🔹recv_packets:** 185466554\n\n\n**===================**\n",
        "**===================**\n      **CɪᴘʜᴇʀX Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 60%\n\n    ●●●●●●○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 62.9%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 8.23GB\n    **🔹used:** 33.32GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 118.55GB\n    **🔹recv:** 168.65GB\n    **🔹sent_packets:** 24786554\n    **🔹recv_packets:** 156745865\n\n\n**===================**\n",
        "**===================**\n      **CɪᴘʜᴇʀX Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 30%\n\n    ●●●○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 30.6%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 9.75GB\n    **🔹used:** 36.54GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 168.65GB\n    **🔹recv:** 128.35GB\n    **🔹sent_packets:** 56565435\n    **🔹recv_packets:** 1475823589\n\n\n**===================**\n",
        "**===================**\n      **CɪᴘʜᴇʀX Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 10%\n\n    ●○○○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 10.2%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 10.20GB\n    **🔹used:** 25.40GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 128.35GB\n    **🔹recv:** 108.31GB\n    **🔹sent_packets:** 54635686\n    **🔹recv_packets:** 157865426\n\n\n**===================**\n",
        "**===================**\n      **CɪᴘʜᴇʀX Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 100%\n\n    ●●●●●●●●●●\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 100.0%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 5.25GB\n    **🔹used:** 31.14GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 108.31GB\n    **🔹recv:** 167.17GB\n    **🔹sent_packets:** 84518799\n    **🔹recv_packets:** 124575356\n\n\n**===================**\n",
        "**===================**\n      **CɪᴘʜᴇʀX Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 70%\n\n    ●●●●●●●○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 76.2%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 8.01GB\n    **🔹used:** 33.27GB\n    **🔹total:** 60.0GB\n    \n    ●●●○○○○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 167.17GB\n    **🔹recv:** 158.98GB\n    **🔹sent_packets:** 36547698\n    **🔹recv_packets:** 165455856\n\n\n**===================**\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@friday.on(friday_on_cmd("joon"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 13)
    animation_chars = [
        "J",
        "Jo",
        "Joo",
        "Jooo",
        "Joooo",
        "Joooooo",
        "Jooooooo",
        "Joooooooo",
        "Jooooooooo",
        "Joooooooooo",
        "Jooooooooooo",
        "Joooooooooooo",
        "Jooooooooooooo",
        "Joooooooooooooon",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 13])


@friday.on(friday_on_cmd("bigoof"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "nope":
    await event.edit(
        "┏━━━┓╋╋╋╋┏━━━┓ \n┃┏━┓┃╋╋╋╋┃┏━┓┃ \n┃┃╋┃┣┓┏┓┏┫┃╋┃┃ \n┃┃╋┃┃┗┛┗┛┃┃╋┃┃ \n┃┗━┛┣┓┏┓┏┫┗━┛┃ \n┗━━━┛┗┛┗┛┗━━━┛"
    )
    animation_chars = [
        "╭━━━╮╱╱╱╭━╮ \n┃╭━╮┃╱╱╱┃╭╯ \n┃┃╱┃┣━━┳╯╰╮ \n┃┃╱┃┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃┃┃ \n╰━━━┻━━╯╰╯ ",
        "╭━━━╮╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃┃┃ \n ╰━━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━╯╰╯",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 40])


@friday.on(events.NewMessage(pattern=r"\.ok", outgoing=True))
async def Ok(e):
    t = "Ok"
    for j in range(15):
        t = t[:-1] + "k"
        await e.edit(t)


@friday.on(events.NewMessage(pattern=r"\.meme", outgoing=True))
async def meme(event):
    if event.fwd_from:
        return
    memeVar = event.text
    sleepValue = 8
    memeVar = memeVar[6:]

    await event.edit("-------------" + memeVar)
    await event.edit("------------" + memeVar + "-")
    await event.edit("-----------" + memeVar + "--")
    await event.edit("----------" + memeVar + "---")
    await event.edit("---------" + memeVar + "----")
    await event.edit("--------" + memeVar + "-----")
    await event.edit("-------" + memeVar + "------")
    await event.edit("------" + memeVar + "-------")
    await event.edit("-----" + memeVar + "--------")
    await event.edit("----" + memeVar + "---------")
    await event.edit("---" + memeVar + "----------")
    await event.edit("--" + memeVar + "-----------")
    await event.edit("-" + memeVar + "------------")
    await event.edit(memeVar + "-------------")
    await event.edit(memeVar)
    await asyncio.sleep(sleepValue)


@friday.on(friday_on_cmd("think"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 288)

    # await event.edit(input_str)
    await event.edit("thinking")
    animation_chars = [
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "Thinking... 🤔",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 72])


@friday.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 27)

    input_str = event.pattern_match.group(1)

    if input_str == "snake":

        await event.edit(input_str)

        animation_chars = [
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "◻️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "◻️◻️◻️️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "◻️◻️◻️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "‎◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️",
            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️",
            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◻️◻️",
            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◻️◻️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◻️◻️◻️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◻️◻️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◼️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◻️◼️◻️◼️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 27])


@friday.on(friday_on_cmd(pattern=r"police"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 64)

    await event.edit("Police")

    animation_chars = [
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "[CɪᴘʜᴇʀX](https://t.me/Hackintush) **Police Service Here**",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])


@friday.on(friday_on_cmd("gangestar ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Everybody")
        await asyncio.sleep(0.3)
        await event.edit("was")
        await asyncio.sleep(0.2)
        await event.edit("Gangestar")
        await asyncio.sleep(0.5)
        await event.edit("Until ")
        await asyncio.sleep(0.2)
        await event.edit("I")
        await asyncio.sleep(0.3)
        await event.edit("Arrived")
        await asyncio.sleep(0.3)
        await event.edit("🔥")
        await asyncio.sleep(0.3)
        await event.edit("Everybody was Gangestar Until I Arrived 🔥")


@friday.on(events.NewMessage(pattern=r"\.flower", outgoing=True))
async def meme(event):
    if event.fwd_from:
        return
    flower = " 🌹"
    sleepValue = 5

    await event.edit(flower + "        ")
    await event.edit(flower + flower + "       ")
    await event.edit(flower + flower + flower + "      ")
    await event.edit(flower + flower + flower + flower + "     ")
    await event.edit(flower + flower + flower + flower + flower + "    ")
    await event.edit(
        flower + flower + flower + flower + flower + flower + flower + "   "
    )
    await event.edit(
        flower + flower + flower + flower + flower + flower + flower + flower + "  "
    )
    await event.edit(
        flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + " "
    )
    await event.edit(
        flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
    )
    await asyncio.sleep(sleepValue)


@friday.on(events.NewMessage(pattern=r"\.tlol", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🤔🧐🤔🧐🤔🧐"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.teeth", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😐😬😐😬😐😬"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.gym", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.run", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🚶🏃🚶🏃🚶🏃🚶🏃"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.candy", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🍦🍧🍩🍪🎂🍰🧁🍫🍬🍭"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.kiss", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😗😚😘😗😚😘😗😚😘"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.butterfly", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🦋✨🦋✨🦋✨🦋✨"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.box", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🟥🟧🟨🟩🟦🟪🟫⬛⬜"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.clock", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.moon", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.earth", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.smile", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🙂🙃🙂🙃🙂🙃"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.laugh", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😄😁😄😁😄😁"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.cat", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😺😸😹😺😸😹😺😸😹"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.poker", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😐😑😐😑😐😑"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.wow", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😧😦😧😦😧😦"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.monkey", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🙉🙈🙉🙈🙉🙈"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.starheart", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😍🤩😍🤩😍🤩"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.wink", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😶😉😶😉😶😉"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(friday_on_cmd("her ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 64)
    await event.edit("loveu")
    animation_chars = [
        "😀",
        "👩‍🎨",
        "😁",
        "😂",
        "🤣",
        "😃",
        "😄",
        "😅",
        "😊",
        "☺",
        "🙂",
        "🤔",
        "🤨",
        "😐",
        "😑",
        "😶",
        "😣",
        "😥",
        "😮",
        "🤐",
        "😯",
        "😴",
        "😔",
        "😕",
        "☹",
        "🙁",
        "😖",
        "😞",
        "😟",
        "😢",
        "😭",
        "🤯",
        "💔",
        "❤️",
        "I Love You ❤️",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 64])


@friday.on(events.NewMessage(pattern=r"\.dance", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    range(0, 5)
    await event.edit("Connecting..")
    animation_chars = [
        "⠀⠀⠀⣶⣿⣶\n⠀⠀⠀⣿⣿⣿⣀\n⠀⣀⣿⣿⣿⣿⣿⣿\n⣶⣿⠛⣭⣿⣿⣿⣿\n⠛⠛⠛⣿⣿⣿⣿⠿\n⠀⠀⠀⠀⣿⣿⣿\n⠀⠀⣀⣭⣿⣿⣿⣿⣀\n⠀⠤⣿⣿⣿⣿⣿⣿⠉\n⠀⣿⣿⣿⣿⣿⣿⠉\n⣿⣿⣿⣿⣿⣿\n⣿⣿⣶⣿⣿\n⠉⠛⣿⣿⣶⣤\n⠀⠀⠉⠿⣿⣿⣤\n⠀⠀⣀⣤⣿⣿⣿\n⠀⠒⠿⠛⠉⠿⣿\n⠀⠀⠀⠀⠀⣀⣿⣿\n⠀⠀⠀⠀⣶⠿⠿⠛\n",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿\n⠀⠀⣶⠀⠀⣀⣤⣶⣤⣉⣿⣿⣤⣀\n⠤⣤⣿⣤⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣀\n⠀⠛⠿⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⠉⠛⠿⣿⣤\n⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⠛⠀⠀⠀⣶⠿\n⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣤⠀⣿⠿\n⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⠿⠉⠉\n⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⠿\n⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠉\n⠀⠀⠀⠀⠀⠀⠀⠀⣛⣿⣭⣶⣀\n⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⠀⣶⠿\n⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⠿\n⠀⠀⠀⠀⠀⠀⠀⠛⠿⠛\n",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶\n⠀⠀⠀⠀⠀⣀⣀⠀⣶⣿⣿⠶\n⣶⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤\n⠀⠉⠶⣶⣀⣿⣿⣿⣿⣿⣿⣿⠿⣿⣤⣀\n⠀⠀⠀⣿⣿⠿⠉⣿⣿⣿⣿⣭⠀⠶⠿⠿\n⠀⠀⠛⠛⠿⠀⠀⣿⣿⣿⣉⠿⣿⠶\n⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠒\n⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⣿⣿⣿⠛⣭⣭⠉\n⠀⠀⠀⠀⠀⣿⣿⣭⣤⣿⠛\n⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿⣭\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⠿⣶⣤\n⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⣶⣶⠿⠿⠿\n⠀⠀⠀⠀⠀⠀⣿⠛\n⠀⠀⠀⠀⠀⠀⣭⣶\n",
        "⠀⠀⠀⠀⠀⠀⣶⣿⣶\n⠀⠀⠀⣤⣤⣤⣿⣿⣿\n⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣶\n⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⠀⠀⣿⣉⣿⣿⣿⣿⣉⠉⣿⣶\n⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿\n⠀⣤⣿⣿⣿⣿⣿⣿⣿⠿⠀⣿⣶\n⣤⣿⠿⣿⣿⣿⣿⣿⠿⠀⠀⣿⣿⣤\n⠉⠉⠀⣿⣿⣿⣿⣿⠀⠀⠒⠛⠿⠿⠿\n⠀⠀⠀⠉⣿⣿⣿⠀⠀⠀⠀⠀⠀⠉\n⠀⠀⠀⣿⣿⣿⣿⣿⣶\n⠀⠀⠀⠀⣿⠉⠿⣿⣿\n⠀⠀⠀⠀⣿⣤⠀⠛⣿⣿\n⠀⠀⠀⠀⣶⣿⠀⠀⠀⣿⣶\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠉\n",
        "⠀⠀⠀⠀⠀⠀⣤⣶⣶\n⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣀⣀\n⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿\n⣤⣶⣀⠿⠶⣿⣿⣿⠿⣿⣿⣿⣿\n⠉⠿⣿⣿⠿⠛⠉⠀⣿⣿⣿⣿⣿\n⠀⠀⠉⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣤⣤\n⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿\n⠀⠀⠀⠀⣀⣿⣿⣿⠿⠉⠀⠀⣿⣿⣿⣿\n⠀⠀⠀⠀⣿⣿⠿⠉⠀⠀⠀⠀⠿⣿⣿⠛\n⠀⠀⠀⠀⠛⣿⣿⣀⠀⠀⠀⠀⠀⣿⣿⣀\n⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠿⣿⣿\n⠀⠀⠀⠀⠀⠉⣿⣿⠀⠀⠀⠀⠀⠀⠉⣿\n⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣀⣿\n⠀⠀⠀⠀⠀⠀⣀⣿⣿\n⠀⠀⠀⠀⠤⣿⠿⠿⠿\n",
    ]


@friday.on(friday_on_cmd("cheart ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("❤️")
        await asyncio.sleep(0.3)
        await event.edit("💙")
        await asyncio.sleep(0.3)
        await event.edit("💛")
        await asyncio.sleep(0.3)
        await event.edit("💚")
        await asyncio.sleep(0.3)
        await event.edit("🧡")
        await asyncio.sleep(0.3)
        await event.edit("💜")
        await asyncio.sleep(0.3)
        await event.edit("🤎")
        await asyncio.sleep(0.3)
        await event.edit("🖤")
        await asyncio.sleep(0.3)
        await event.edit("🤍")
        await asyncio.sleep(0.3)
        await event.edit("💜")
        await asyncio.sleep(0.3)
        await event.edit("🤎")
        await asyncio.sleep(0.3)
        await event.edit("🤍")
        await asyncio.sleep(0.3)
        await event.edit("🧡")
        await asyncio.sleep(0.3)
        await event.edit("💚")
        await asyncio.sleep(0.3)
        await event.edit("💛")
        await asyncio.sleep(0.3)
        await event.edit("💙")
        await asyncio.sleep(0.3)
        await event.edit("❤️")
        await asyncio.sleep(0.3)
        await event.edit("💝")


@friday.on(friday_on_cmd("finger ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("🖕🏻")
        await asyncio.sleep(0.3)
        await event.edit("🖕")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏼")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏽")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏾")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏿")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏾")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏽")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏼")
        await asyncio.sleep(0.3)
        await event.edit("🖕")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏻")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏽")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏾")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏿")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏾")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏽")
        await asyncio.sleep(0.3)
        await event.edit("🖕")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏼")


@friday.on(friday_on_cmd("billy ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("👍")
        await asyncio.sleep(0.6)
        await event.edit("👍🏻")
        await asyncio.sleep(0.6)
        await event.edit("👍🏼")
        await asyncio.sleep(0.6)
        await event.edit("👍🏽")
        await asyncio.sleep(0.6)
        await event.edit("👍🏾")
        await asyncio.sleep(0.6)
        await event.edit("👍🏿")
        await asyncio.sleep(0.6)
        await event.edit("👍🏾")
        await asyncio.sleep(0.6)
        await event.edit("👍🏽")
        await asyncio.sleep(0.6)
        await event.edit("👍🏼")
        await asyncio.sleep(0.6)
        await event.edit("👍🏻")


@friday.on(friday_on_cmd("agree ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("👌")
        await asyncio.sleep(0.6)
        await event.edit("👌🏻")
        await asyncio.sleep(0.6)
        await event.edit("👌🏼")
        await asyncio.sleep(0.6)
        await event.edit("👌🏽")
        await asyncio.sleep(0.6)
        await event.edit("👌🏾")
        await asyncio.sleep(0.6)
        await event.edit("👌🏿")
        await asyncio.sleep(0.6)
        await event.edit("👌🏾")
        await asyncio.sleep(0.6)
        await event.edit("👌🏽")
        await asyncio.sleep(0.6)
        await event.edit("👌🏼")
        await asyncio.sleep(0.6)
        await event.edit("👌🏻")


@friday.on(events.NewMessage(pattern=r"\.angry", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😡🤬😡🤬😡🤬"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.sad", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😒😏😒😏😒😏"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.amaze", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😳😲😳😲😳😲"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.omg", outgoing=True))
async def _(event):

    if event.fwd_from:
        return
    deq = deque(list("🙄😳🙄😳🙄😳"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.tongue", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😛😝😛😝😛😝"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.sun", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🔅🔆🔅🔆🔅🔆"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.speaker", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🔈🔊🔈🔊🔈🔊"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.heart", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("💖💝💖💝💖💝💖💝"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(friday_on_cmd("heart$"))
# @register(outgoing=True, pattern="^.heart$")
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.sand", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("⏳⌛️⏳⌛️⏳⌛️"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.storm", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🌧⛈🌧⛈🌧⛈"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.floodwarn", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("💙💛💓💔💘💕💜💚💝💞💟"))
    for _ in range(64):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.rain", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("☁️⛈Ř/~\İŇ🌬⚡🌪"))
    for _ in range(64):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.brain", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 14)
    animation_chars = [
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           (> ^_^)>🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           <(^_^ <)🗑",
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 14])


@friday.on(events.NewMessage(pattern=r"\.dump", outgoing=True))
async def _(message):
    try:
        obj = message.pattern_match.group(1)
        if len(obj) != 3:
            raise IndexError
        inp = " ".join(obj)
    except IndexError:
        inp = "🥞 🎂 🍫"
    u, t, g, o, s, n = inp.split(), "🗑", "<(^_^ <)", "(> ^_^)>", "⠀ ", "\n"
    h = [(u[0], u[1], u[2]), (u[0], u[1], ""), (u[0], "", "")]
    for something in reversed(
        [
            y
            for y in (
                [
                    "".join(x)
                    for x in (
                        f + (s, g, s + s * f.count(""), t),
                        f + (g, s * 2 + s * f.count(""), t),
                        f[:i] + (o, f[i], s * 2 + s * f.count(""), t),
                        f[:i] + (s + s * f.count(""), o, f[i], s, t),
                        f[:i] + (s * 2 + s * f.count(""), o, f[i], t),
                        f[:i] + (s * 3 + s * f.count(""), o, t),
                        f[:i] + (s * 3 + s * f.count(""), g, t),
                    )
                ]
                for i, f in enumerate(reversed(h))
            )
        ]
    ):
        for something_else in something:
            await asyncio.sleep(0.3)
            try:
                await message.edit(something_else)
            except errors.MessageIdInvalidError:
                return


@friday.on(friday_on_cmd("good ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            ".     😍😊😍😊😍😍\n 😊😍😍😍😍😊😍😊\n  😍😊                     😊😊\n 😍😍\n😍😊                😊😍😊😍\n😍😊                😍😊😊😊\n😍😊                        😊😍\n   😊😊                      😍😍\n     😍😊😍😍😍😊😊😍  \n          😊😊😊😍😍😊 "
        )
        await asyncio.sleep(0.5)
        await event.edit(
            ".           😍😊😊😊😍\n 😍😊😍😍😊😍😊\n   😍😊                   😊😍\n 😍😊                       😍😊\n😊😍                         😍😍\n😊😊                         😍😍\n 😊😊                       😍😍\n   😊😊                   😍😊\n      😍😍😍😍😍😍😊\n            😊😊😍😍😍"
        )
        await asyncio.sleep(0.5)
        await event.edit(
            ".           😊😊😍😊😊\n     😊😍😍😍😊😍😊\n   😊😍                   😍😊\n 😊😊                       😍😊\n😍😍                         😍😊\n😍😍                         😊😊\n 😍😊                       😍😍\n   😊😍                   😊😊\n      😊😊😍😍😊😊😊\n            😍😊😊😊😊"
        )
        await asyncio.sleep(0.5)
        await event.edit(
            "😊😍😊😍😊😍😊\n😍😍😍😊😍😍😍😊\n😍😊                      😊😊\n😊😊                         😊😊\n😍😊                         😊😍\n😍😍                         😊😊\n😍😊                         😊😊\n😊😍                      😍😊\n😊😍😍😍😊😊😊😊\n😊😊😊😍😍😊😍\n\n"
        )
        await asyncio.sleep(0.5)
        await event.edit(
            "😍😊                              😍😍\n😊😍😊                      😍😊😊\n😍😊😍😊            😊😊😊😍\n😊😊    😊😊    😊😊    😊😊\n😊😊        😊😊😊        😍😍\n😊😊             😍             😍😊\n😍😊                              😍😊\n😊😍                              😊😊\n😍😍                              😊😊\n😊😊                              😍😊"
        )
        await asyncio.sleep(0.5)
        await event.edit(
            ".           😍😊😊😊😍\n 😍😊😍😍😊😍😊\n   😍😊                   😊😍\n 😍😊                       😍😊\n😊😍                         😍😍\n😊😊                         😍😍\n 😊😊                       😍😍\n   😊😊                   😍😊\n      😍😍😍😍😍😍😊\n            😊😊😍😍😍"
        )
        await asyncio.sleep(0.5)
        await event.edit(
            "😍😍😍😊😍😊😍\n😍😊😍😍😊😊😊😊\n😍😊                     😍😍\n😊😍                     😍😍\n😊😍😍😍😊😊😊😊\n😍😊😍😍😊😍😍\n😊😊    😍😊\n😍😍         😍😊\n😊😊              😊😊\n😊😊                  😍😊"
        )
        await asyncio.sleep(0.5)
        await event.edit(
            "😊😍                           😍😍\n😍😍😊                       😊😍\n😊😊😍😍                 😍😊\n😍😍  😊😊               😍😊\n😍😊     😊😊            😊😊\n😊😍         😊😊        😍😊\n😊😍             😍😍    😍😍\n😊😍                 😊😍😊😊\n😍😊                     😊😍😊\n😍😊                          😊😍"
        )
        await asyncio.sleep(0.5)
        await event.edit(
            "😊😊😊😍😊😍\n😊😍😊😍😍😍\n          😍😍\n          😍😍\n          😍😊\n          😍😊\n          😊😊\n          😊😊\n😍😊😍😊😊\n😊😍😍😊😊😊"
        )
        await asyncio.sleep(0.5)
        await event.edit(
            "😊😍                           😍😍\n😍😍😊                       😊😍\n😊😊😍😍                 😍😊\n😍😍  😊😊               😍😊\n😍😊     😊😊            😊😊\n😊😍         😊😊        😍😊\n😊😍             😍😍    😍😍\n😊😍                 😊😍😊😊\n😍😊                     😊😍😊\n😍😊                          😊😍"
        )
        await asyncio.sleep(0.5)
        await event.edit(
            ".     😍😊😍😊😍😍\n 😊😍😍😍😍😊😍😊\n  😍😊                     😊😊\n 😍😍\n😍😊                😊😍😊😍\n😍😊                😍😊😊😊\n😍😊                        😊😍\n   😊😊                      😍😍\n     😍😊😍😍😍😊😊😍  \n          😊😊😊😍😍😊 "
        )
        await asyncio.sleep(0.5)
        await event.edit("GOOD MORNING ,HAVE A NICE DAY 😊")


@friday.on(events.NewMessage(pattern=r"\.snake", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 27)
    animation_chars = [
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "‎◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◼️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◼️◻️◼️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 27])


@friday.on(events.NewMessage(pattern=r"\.human", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 27)
    animation_chars = [
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛🚗\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛🚗⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛🚗⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🚗⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛🚗⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛🚗⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n🚗⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜😊⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬛⬜⬛\n⬛⬛⬜⬛⬛⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛😊⬛⬜⬛\n⬛⬛⬜⬜⬜⬛⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬛⬜⬜⬜⬛⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜😊⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 27])


@friday.on(events.NewMessage(pattern=r"\.mc", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 64)
    animation_chars = [
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◻️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◻️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◻️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◻️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◻️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◻️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◻️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◻️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◻️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◻️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◻️◼️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◻️◻️◻️◼️\n◼️◼️◼️◼️◼️",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 64])


@friday.on(events.NewMessage(pattern=r"\.solar", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 64)
    animation_chars = [
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 64])


@friday.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 300)

    input_str = event.pattern_match.group(1)

    if input_str == "smoon":

        await event.edit(input_str)

        animation_chars = [
            "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
            "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",
            "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
            "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
            "🌓🌓🌓🌓🌓\n🌓🌓🌓🌓🌓\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
            "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
            "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
            "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 300])


@friday.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "tmoon":

        await event.edit(input_str)

        animation_chars = [
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 100])


@friday.on(friday_on_cmd(pattern=r"lmoon"))
async def test(event):
    if event.fwd_from:
        return
    await event.edit(
        "🌕🌕🌕🌕🌕🌕🌕🌕\n🌕🌕🌖🌔🌖🌔🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌖🌓🌗🌔🌕🌕\n🌕🌕🌗🌑🌑🌓🌕🌕\n🌕🌕🌗👀🌑🌓🌕🌕\n🌕🌕🌘👄🌑🌓🌕🌕\n🌕🌕🌗🌑🌑🌒🌕🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌕🌘🌑🌑🌑🌑🌒🌕\n🌖🌑🌑🌑🌑🌑🌑🌔\n🌕🤜🏻🌑🌑🌑🌑🤛🏻🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌘🌑🌑🌑🌑🌑🌑🌒\n🌕🌕🌕🌕🌕🌕🌕🌕"
    )


@friday.on(friday_on_cmd(pattern=r"town"))
async def test(event):
    if event.fwd_from:
        return
    await event.edit(
        """☁☁🌞      ☁           ☁
       ☁  ✈         ☁    🚁    ☁    ☁        ☁          ☁     ☁   ☁

🏬🏨🏫🏢🏤🏥🏦🏪🏫
              🌲/     l🚍\🌳👭
           🌳/  🚘 l  🏃 \🌴 👬                       👬  🌴/            l  🚔    \🌲
      🌲/   🚖     l               \
   🌳/🚶           |   🚍         \ 🌴🚴🚴
🌴/                    |                     \🌲"""
    )


@friday.on(events.NewMessage(pattern=r"\.bombs", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n")
    await asyncio.sleep(1)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n")
    await asyncio.sleep(0.5)
    await event.edit("RIP...")


@friday.on(events.NewMessage(pattern=r"\.plane", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("✈-------------")
    await event.edit("-✈------------")
    await event.edit("--✈-----------")
    await event.edit("---✈----------")
    await event.edit("----✈---------")
    await event.edit("-----✈--------")
    await event.edit("------✈-------")
    await event.edit("-------✈------")
    await event.edit("--------✈-----")
    await event.edit("---------✈----")
    await event.edit("----------✈---")
    await event.edit("-----------✈--")
    await event.edit("------------✈-")
    await event.edit("-------------✈")
    await asyncio.sleep(3)
    await event.delete()


@friday.on(friday_on_cmd(pattern="lalol"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(
        "😂\n😂\n😂\n😂\n😂😂😂😂\n\n   😂😂😂\n 😂         😂\n😂           😂\n 😂         😂\n   😂😂😂\n\n😂\n😂\n😂\n😂\n😂😂😂😂"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 ")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💓💓")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔❤️❤️")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💓💓")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💜💜𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💜💜")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💓💓")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💛💛𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💛💛")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓??𝒆𝒏𝒅𝒔💓💓")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💚💚𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💚💚")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💓💓")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("🧡🧡𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔🧡🧡")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💓💓")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💙💙")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💜💜𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💜💜")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💚💚𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💚💚")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💛💛𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💛💛")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("🖤🖤𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔🖤🖤")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💙💙")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💜💜𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💜💜")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💚💚𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💚💚")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💛💛𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💛💛")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💝💝𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💝💝")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💕💕𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💕💕")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💖💖𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💖💖")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💕💕𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💕💕")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💝💝𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💝💝")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💕💕𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💕💕")


@friday.on(friday_on_cmd(pattern=r"figcar"))
async def car(event):
    if event.fwd_from:
        return
    await event.edit(
        "┈╱▔▔▔▔▔▔▔▔╲┈┈┈┈\n ╱▔▔▔▔▔▔▔▔╲╱┈┈┈┈\n▏┳╱╭╮┓┏┏┓▕╱▔▔╲┈\n▏┃╱┃┃┃┃┣▏▕▔▔╲╱▏\n▏┻┛╰╯╰╯┗┛▕▕▉▕╱╲\n▇▇▇▇▇▇▇▇▇▇▔▔▔╲▕\n▇▇╱▔╲▇▇▇▇▇╱▔╲▕╱\n┈┈╲▂╱┈┈┈┈┈╲▂╱▔┈"
    )


@friday.on(friday_on_cmd(pattern=r"figkiller"))
async def car(event):
    if event.fwd_from:
        return
    await event.edit("_/﹋\_\n" "(҂`_´)\n" "<,︻╦╤─ ҉ - -\n" "_/﹋\_\n")


@register(outgoing=True, pattern="^.figgun$")
async def figgun(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "........___________________\n"
            "....../ `-___________--_____|] - - - - - -\n"
            " - - ░ ▒▓▓█D \n"
            "...../==o;;;;;;;;______.:/\n"
            ".....), -.(_(__) /\n"
            "....// (..) ), —\n"
            "...//___//\n"
        )


# ================= CONSTANT =================


GAMBAR_TITIT = """
🍆🍆
🍆🍆🍆
  🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
          🍆🍆🍆
      🍆🍆🍆🍆
 🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆       🍆🍆
"""

# ===========================================


@register(outgoing=True, pattern=r"^\.(?:penis|dick)\s?(.)?")
async def emoji_penis(e):
    emoji = e.pattern_match.group(1)
    titid = GAMBAR_TITIT
    if emoji:
        titid = titid.replace("🍆", emoji)
    await e.edit(titid)


@register(outgoing=True, pattern="^.figlol$")
async def figlol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "`\n╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱ `"
            "`\n╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱ `"
            "`\n╱┃┗━━┓┃╰━╯┃┃┗━━┓╱ `"
            "`\n╱┗━━━┛╰━━━╯┗━━━┛╱ `"
        )


@register(outgoing=True, pattern="^.figlmao$")
async def figlol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "`\n┏┓┈╭━━╮╭━━╮╭━━╮`"
            "`\n┃┃┈┃┃┃┃┃╭╮┃┃╭╮┃`"
            "`\n┃┗┓┃┃┃┃┃┏┓┃┃╰╯┃`"
            "`\n┗━┛┗┻┻┛┗┛┗┛╰━━╯`"
        )


@register(outgoing=True, pattern="^.fighi$")
async def fighi(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "\n╔┓┏╦━╦┓╔┓╔━━╗" "\n║┗┛║┗╣┃║┃║X X║" "\n║┏┓║┏╣┗╣┗╣╰╯║" "\n╚┛┗╩━╩━╩━╩━━╝"
        )


@register(outgoing=True, pattern="^.figno$")
async def figtrump(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "\n███╗░░██╗░█████╗░"
            "\n████╗░██║██╔══██╗"
            "\n██╔██╗██║██║░░██║"
            "\n██║╚████║██║░░██║"
            "\n██║░╚███║╚█████╔╝"
            "\n╚═╝░░╚══╝░╚════╝░"
        )


@register(outgoing=True, pattern="^.figtrump$")
async def figtrump(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "\n⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⡉⣉⡛⣛⠿⣿⣿⣿⣿⣿⣿⣿⣿"
            "\n⣿⣿⣿⡿⠋⠁⠄⠄⠄⠄⠄⢀⣸⣿⣿⡿⠿⡯⢙⠿⣿⣿⣿⣿"
            "\n⣿⣿⡿⠄⠄⠄⠄⠄⡀⡀⠄⢀⣀⣉⣉⣉⠁⠐⣶⣶⣿⣿⣿⣿"
            "\n⣿⣿⡇⠄⠄⠄⠄⠁⣿⣿⣀⠈⠿⢟⡛⠛⣿⠛⠛⣿⣿⣿⣿⣿"
            "\n⣿⣿⡆⠄⠄⠄⠄⠄⠈⠁⠰⣄⣴⡬⢵⣴⣿⣤⣽⣿⣿⣿⣿⣿"
            "\n⣿⣿⡇⠄⢀⢄⡀⠄⠄⠄⠄⡉⠻⣿⡿⠁⠘⠛⡿⣿⣿⣿⣿⣿"
            "\n⣿⡿⠃⠄⠄⠈⠻⠄⠄⠄⠄⢘⣧⣀⠾⠿⠶⠦⢳⣿⣿⣿⣿⣿"
            "\n⣿⣶⣤⡀⢀⡀⠄⠄⠄⠄⠄⠄⠻⢣⣶⡒⠶⢤⢾⣿⣿⣿⣿⣿"
            "\n⣿⡿⠋⠄⢘⣿⣦⡀⠄⠄⠄⠄⠄⠉⠛⠻⠻⠺⣼⣿⠟⠛⠿⣿"
            "\n⠋⠁⠄⠄⠄⢻⣿⣿⣶⣄⡀⠄⠄⠄⠄⢀⣤⣾⣿⡀⠄⠄⠄⢹"
            "\n⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣷⡤⠄⠰⡆⠄⠄⠈⠛⢦⣀⡀⡀⠄"
            "\n⠄⠄⠄⠄⠄⠄⠈⢿⣿⠟⡋⠄⠄⠄⢣⠄⠄⠄⠄⠄⠈⠹⣿⣀"
            "\n⠄⠄⠄⠄⠄⠄⠄⠘⣷⣿⣿⣷⠄⠄⢺⣇⠄⠄⠄⠄⠄⠄⠸⣿"
            "\n⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⡇⠄⠄⠸⣿⡄⠄⠈⠁⠄⠄⠄⣿"
            "\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⡇⠄⠄⠄⢹⣧⠄⠄⠄⠄⠄⠄⠘"
        )


@register(outgoing=True, pattern="^.figputin$")
async def figputin(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣵⣿⣿⣿⠿⡟⣛⣧⣿⣯⣿⣝⡻⢿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⠋⠁⣴⣶⣿⣿⣿⣿⣿⣿⣿⣦⣍⢿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⢷⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⢼⣿⣿⣿⣿\n"
            "⢹⣿⣿⢻⠎⠔⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿\n"
            "⢸⣿⣿⠇⡶⠄⣿⣿⠿⠟⡛⠛⠻⣿⡿⠿⠿⣿⣗⢣⣿⣿⣿⣿\n"
            "⠐⣿⣿⡿⣷⣾⣿⣿⣿⣾⣶⣶⣶⣿⣁⣔⣤⣀⣼⢲⣿⣿⣿⣿\n"
            "⠄⣿⣿⣿⣿⣾⣟⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⢟⣾⣿⣿⣿⣿\n"
            "⠄⣟⣿⣿⣿⡷⣿⣿⣿⣿⣿⣮⣽⠛⢻⣽⣿⡇⣾⣿⣿⣿⣿⣿\n"
            "⠄⢻⣿⣿⣿⡷⠻⢻⡻⣯⣝⢿⣟⣛⣛⣛⠝⢻⣿⣿⣿⣿⣿⣿\n"
            "⠄⠸⣿⣿⡟⣹⣦⠄⠋⠻⢿⣶⣶⣶⡾⠃⡂⢾⣿⣿⣿⣿⣿⣿\n"
            "⠄⠄⠟⠋⠄⢻⣿⣧⣲⡀⡀⠄⠉⠱⣠⣾⡇⠄⠉⠛⢿⣿⣿⣿\n"
            "⠄⠄⠄⠄⠄⠈⣿⣿⣿⣷⣿⣿⢾⣾⣿⣿⣇⠄⠄⠄⠄⠄⠉⠉\n"
            "⠄⠄⠄⠄⠄⠄⠸⣿⣿⠟⠃⠄⠄⢈⣻⣿⣿⠄⠄⠄⠄⠄⠄⠄\n"
            "⠄⠄⠄⠄⠄⠄⠄⢿⣿⣾⣷⡄⠄⢾⣿⣿⣿⡄⠄⠄⠄⠄⠄⠄\n"
            "⠄⠄⠄⠄⠄⠄⠄⠸⣿⣿⣿⠃⠄⠈⢿⣿⣿⠄⠄⠄⠄⠄⠄⠄\n"
        )


@register(outgoing=True, pattern="^.figchina$")
async def figchina(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "⣿⣿⣿⣿⠟⠋⢁⢁⢁⢁⢁⢁⢁⢁⠈⢻⢿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⡀⠭⢿⣿⣿⣿⣿\n"
            "⣿⣿⣿⡟⠄⢀⣾⣿⣿⣿⣷⣶⣿⣷⣶⣶⡆⠄⠄⠄⣿⣿⣿⣿\n"
            "⣿⣿⣿⡇⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⢸⣿⣿⣿⣿\n"
            "⣿⣿⣿⣇⣼⣿⣿⠿⠶⠙⣿⡟⠡⣴⣿⣽⣿⣧⠄⢸⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣾⣿⣿⣟⣭⣾⣿⣷⣶⣶⣴⣶⣿⣿⢄⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⣿⡟⣩⣿⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣹⡋⠘⠷⣦⣀⣠⡶⠁⠈⠁⠄⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣍⠃⣴⣶⡔⠒⠄⣠⢀⠄⠄⠄⡨⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⣦⡘⠿⣷⣿⠿⠟⠃⠄⠄⣠⡇⠈⠻⣿⣿⣿⣿\n"
            "⣿⣿⣿⡿⠟⠋⢁⣷⣠⠄⠄⠄⠄⣀⣠⣾⡟⠄⠄⠄⠄⠉⠙⠻\n"
            "⡿⠟⠁⠄⠄⠄⢸⣿⣿⡯⢓⣴⣾⣿⣿⡟⠄⠄⠄⠄⠄⠄⠄⠄\n"
            "⠄⠄⠄⠄⠄⠄⣿⡟⣷⠄⠹⣿⣿⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄\n"
            "⠄⠄⠄⠄⠄⣸⣿⡷⡇⠄⣴⣾⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
            "⠄⠄⠄⠄⠄⣿⣿⠃⣦⣄⣿⣿⣿⠇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
            "⠄⠄⠄⠄⢸⣿⠗⢈⡶⣷⣿⣿⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
        )


@register(outgoing=True, pattern="^.figthink$")
async def figthink(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "⠀⠀⠀⠀⢀⣀⣀⣀\n"
            "⠀⠀⠀⠰⡿⠿⠛⠛⠻⠿⣷\n"
            "⠀⠀⠀⠀⠀⠀⣀⣄⡀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⡀\n"
            "⠀⠀⠀⠀⠀⢸⣿⣿⣷⠀⠀⠀⠀⠛⠛⣿⣿⣿⡛⠿⠷\n"
            "⠀⠀⠀⠀⠀⠘⠿⠿⠋⠀⠀⠀⠀⠀⠀⣿⣿⣿⠇\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁\n"
            "⠀\n"
            "⠀⠀⠀⠀⣿⣷⣄⠀⢶⣶⣷⣶⣶⣤⣀\n"
            "⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠈⠙⠻⠗\n"
            "⠀⠀⠀⣰⣿⣿⣿⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⡄\n"
            "⠀⣠⣾⣿⣿⣿⣥⣶⣶⣿⣿⣿⣿⣿⠿⠿⠛⠃\n"
            "⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄\n"
            "⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁\n"
            "⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁\n"
            "⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟\n"
        )


@register(outgoing=True, pattern="^.figdick$")
async def figdick(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠲⢄\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⠁⠀⠀⠀⠀⢱\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⠀⠀⠀⠀⠀⠀⠀⣸\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⠀⠀⠀⠀⢀⡠⠖⠁\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⠁⠀⠀\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣯⣿⣿⣿⣿⣿⠇⠀⠀⠀\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⣻⣿⣿⣿⣿⣯⠏⠀⠀⠀⠀\n"
            "⠀⠀⠀⠀⠀⠀⠀⣠⠾⣽⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀\n"
            "⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀\n"
            "⠀⠀⠀⠀⣴⣻⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀\n"
            "⠀⠀⣠⢾⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
            "⠀⣼⣷⣿⣿⣿⣿⣿⣿⣟⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
            "⢸⢿⣿⣿⣿⣿⣿⣿⣿⣯⣻⡟⡆⠀⠀⠀⠀⠀⠀⠀⠀\n"
            "⠸⣿⣿⣿⣿⣿⣿⣿⣿⣹⣿⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀\n"
            "⠀⠹⣟⣿⣿⣿⣿⡿⣷⡿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀\n"
            "⠀⠀⠈⠛⠯⣿⡯⠟⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        )


@register(outgoing=True, pattern="^.fighappyfrog$")
async def fighappyfrog(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "⠄⠄⠄⠄⠄⣀⣀⣤⣶⣿⣿⣶⣶⣶⣤⣄⣠⣴⣶⣿⣶⣦⣄⠄\n"
            "⠄⣠⣴⣾⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦\n"
            "⢠⠾⣋⣭⣄⡀⠄⠙⠻⣿⣿⡿⠛⠋⠉⠉⠉⠙⠛⠿⣿⣿⣿⣿\n"
            "⡎⡟⢻⣿⣷⠄⠄⠄⠄⡼⣡⣾⣿⣿⣦⠄⠄⠄⠄⠄⠈⠛⢿⣿\n"
            "⡇⣷⣾⣿⠟⠄⠄⠄⢰⠁⣿⣇⣸⣿⣿⠄⠄⠄⠄⠄⠄⠄⣠⣼\n"
            "⣦⣭⣭⣄⣤⣤⣴⣶⣿⣧⡘⠻⠛⠛⠁⠄⠄⠄⠄⣀⣴⣿⣿⣿\n"
            "⢉⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿\n"
            "⡿⠛⠛⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⡇⠄⠄⢀⣀⣀⠄⠄⠄⠄⠉⠉⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⠈⣆⠄⠄⢿⣿⣿⣷⣶⣶⣤⣤⣀⣀⡀⠄⠄⠉⢻⣿⣿⣿⣿⣿\n"
            "⠄⣿⡀⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠄⢠⣿⣿⣿⣿⣿\n"
            "⠄⣿⡇⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄⢀⣼⣿⣿⣿⣿⣿\n"
            "⠄⣿⡇⠄⠠⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿\n"
            "⠄⣿⠁⠄⠐⠛⠛⠛⠉⠉⠉⠉⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⠄⠻⣦⣀⣀⣀⣀⣀⣤⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋\n"
        )


@register(outgoing=True, pattern="^.figdeadfrog$")
async def figdeadfrog(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⡇⠄⣿⣿⣿⡿⠋⣉⣉⣉⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⠃⠄⠹⠟⣡⣶⢟⣛⣛⡻⢿⣦⣩⣤⣬⡉⢻⣿⣿⣿⣿\n"
            "⣿⣿⣿⠄⢀⢤⣾⣿⣿⣿⡿⠿⠿⠿⢮⡃⣛⡻⢿⠈⣿⣿⣿⣿\n"
            "⣿⡟⢡⣴⣯⣿⣿⣿⠤⣤⣭⣶⣶⣶⣮⣔⡈⠛⢓⠦⠈⢻⣿⣿\n"
            "⠏⣠⣿⣿⣿⣿⣿⣿⣯⡪⢛⠿⢿⣿⣿⣿⡿⣼⣿⣿⣮⣄⠙⣿\n"
            "⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⡭⠴⣶⣶⣽⣽⣛⡿⠿⠿⠇⣿\n"
            "⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣷⣝⣛⢛⢋⣥⣴⣿⣿\n"
            "⣿⣿⣿⣿⣿⢿⠱⣿⣛⠾⣭⣛⡿⢿⣿⣿⣿⣿⣿⡀⣿⣿⣿⣿\n"
            "⠑⠽⡻⢿⣮⣽⣷⣶⣯⣽⣳⠮⣽⣟⣲⠯⢭⣿⣛⡇⣿⣿⣿⣿\n"
            "⠄⠄⠈⠑⠊⠉⠟⣻⠿⣿⣿⣿⣷⣾⣭⣿⠷⠶⠂⣴⣿⣿⣿⣿\n"
            "⠄⠄⠄⠄⠄⠄⠄⠁⠙⠒⠙⠯⠍⠙⢉⣡⣶⣿⣿⣿⣿⣿⣿⣿\n"
            "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        )


@register(outgoing=True, pattern="^.fuck$")
async def gtfo(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "\n...................................../´¯/) "
            "\n...................................,/¯../ "
            "\n.................................../.../ "
            "\n................................../´.¯/"
            "\n................................./´¯./"
            "\n...............................,/¯../ "
            "\n.............................../.../ "
            "\n............................../´¯./"
            "\n............................./´¯./"
            "\n...........................,/¯../ "
            "\n.........................../.../ "
            "\n........................../´¯./"
            "\n........................./´¯./"
            "\n.......................,/¯../ "
            "\n......................./.../ "
            "\n....................../´¯./"
            "\n....................,/¯../ "
            "\n.................../..../ "
            "\n............./´¯/'...'/´¯¯`·¸ "
            "\n........../'/.../..../......./¨¯\ "
            "\n........('(...´...´.... ¯~/'...') "
            "\n.........\.................'...../ "
            "\n..........''...\.......... _.·´ "
            "\n............\..............( "
            "\n..............\.............\..."
        )


@friday.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 60)

    input_str = event.pattern_match.group(1)

    if input_str == "jagh":

        await event.edit(input_str)

        animation_chars = [
            "8✊️===D",
            "8=✊️==D",
            "8==✊️=D",
            "8===✊️D",
            "8==✊️=D",
            "8=✊️==D",
            "8✊️===D",
            "8===✊️D💦",
            "8==✊️=D💦💦",
            "8=✊️==D💦💦💦",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 8])


CMD_HELP.update(
    {
        "cipherXfun": "List of All Available Fun Commands.\
\n\n.slash\
\n\n.para\
\n\n.question\
\n\n.oof\
\n\n.motion\
\n\n.square\
\n\n.up\
\n\n.round\
\n\n.cipherx\
\n\n.joon\
\n\n.bigoof\
\n\n.ok\
\n\n.meme\
\n\n.think\
\n\n.snake\
\n\n.police\
\n\n.gangestar\
\n\n.flower\
\n\n.tlol\
\n\n.teeth\
\n\n.gym\
\n\n.run\
\n\n.candy\
\n\n.kiss\
\n\n.butterfly\
\n\n.box\
\n\n.clock\
\n\n.moon\
\n\n.earth\
\n\n.smile\
\n\n.laugh\
\n\n.cat\
\n\n.poker\
\n\n.wow\
\n\n.monkey\
\n\n.starheart\
\n\n.wink\
\n\n.her\
\n\n.dance\
\n\n.cheart\
\n\n.finger\
\n\n.billy\
\n\n.agree\
\n\n.angry\
\n\n.sad\
\n\n.amaze\
\n\n.omg\
\n\n.tongue\
\n\n.sun\
\n\n.speaker\
\n\n.heart\
\n\n.sand\
\n\n.storm\
\n\n.floodwarn\
\n\n.rain\
\n\n.brain\
\n\n.dump\
\n\n.good\
\n\n.snake\
\n\n.human\
\n\n.solar\
\n\n.smoon\
\n\n.tmoon\
\n\n.lmoon\
\n\n.town\
\n\n.bombs\
\n\n.lalol\
\n\n.lit\
\n\n.love\
\n\n.my\
\n\n.hi\
\n\n.figcar\
\n\n.figkiller\
\n\n.figgun\
\n\n.penis;dick\
\n\n.figlol\
\n\n.figlmao\
\n\n.fighi\
\n\n.figno\
\n\n.figtrump\
\n\n.figputin\
\n\n.figchina\
\n\n.figthink\
\n\n.figdick\
\n\n.fighappyfrog\
\n\n.figdeadfrog\
\n\n.fuck\
\n\n.jagh"
    }
)
