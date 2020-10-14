import re
from math import ceil

from telethon import Button
from telethon import custom
from telethon import events
from telethon import functions

from userbot import ALIVE_NAME
from userbot import CMD_LIST
from userbot.plugins import inlinestats

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Friday"
if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("Friday"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article(
                "© Userbot Help",
                text="{}\nCurrently Loaded Plugins: {}".format(
                    query, len(CMD_LIST)),
                buttons=buttons,
                link_preview=False,
            )
        if event.query.user_id == bot.uid and query == "stats":
            result = builder.article(
                title="Stats",
                text=
                f"**Showing Stats For {DEFAULTUSER}'s Friday** \nNote --> Only Owner Can Check This \n(C) @FridayOT",
                buttons=[
                    [custom.Button.inline("Show Stats ", data="terminator")],
                    [
                        Button.url(
                            "Repo ",
                            "https://github.com/StarkGang/FridayUserbot")
                    ],
                    [Button.url("Join Channel ", "t.me/Fridayot")],
                ],
            )
        if event.query.user_id == bot.uid and query == "dontpm":
            result = builder.article(
                title="PM Test",
                text=f"Hey, Let Me Know Why Are You Here",
                buttons=[
                    [
                        custom.Button.inline("For Spamming",
                                             data="dontspamnigga")
                    ],
                    [
                        custom.Button.inline("For Talking With Master",
                                             data="whattalk")
                    ],
                    [
                        custom.Button.inline("For Asking Someting",
                                             data="askme")
                    ],
                ],
            )
        await event.answer([result] if result else None)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"helpme_next\((.+?)\)")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(current_page_number + 1, CMD_LIST,
                                    "helpme")
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_popp_up_alert = "Please get your own Userbot, and don't use mine!"
            await event.answer(reply_popp_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"helpme_prev\((.+?)\)")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1,
                CMD_LIST,
                "helpme"  # pylint:disable=E0602
            )
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "Please get your own Userbot, and don't use mine!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"us_plugin_(.*)")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            plugin_name = event.data_match.group(1).decode("UTF-8")
            help_string = ""
            try:
                for i in CMD_LIST[plugin_name]:
                    help_string += i
                    help_string += "\n"
            except BaseException:
                pass
            if help_string is "":
                reply_pop_up_alert = "{} is useless".format(plugin_name)
            else:
                reply_pop_up_alert = help_string
            reply_pop_up_alert += "\n Use .unload {} to remove this plugin\n\
                  © Userbot".format(plugin_name)
            try:
                await event.answer(reply_pop_up_alert,
                                   cache_time=0,
                                   alert=True)
            except BaseException:
                halps = "Do .help {} to get the list of commands.".format(
                    plugin_name)
                await event.answer(halps, cache_time=0, alert=True)
        else:
            reply_pop_up_alert = "Please get your own Userbot, and don't use mine!"

    @tgbot.on(
        events.callbackquery.CallbackQuery(data=re.compile(b"terminator")))
    async def rip(event):
        if event.query.user_id == bot.uid:
            text = inlinestats
            await event.answer(text, alert=True)
        else:
            txt = "You Can't View My Masters Stats"
            await event.answer(txt, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(data=re.compile(b"dontspamnigga")))
    async def rip(event):
        chat_k = await event.get_chat()
        text1 = "Lmao 🤣. You Have Been Blocked :)"
        await event.edit("User Chosed A Choice")
        await borg.send_message(event.query.user_id, text1)
        await borg(functions.contacts.BlockRequest(event.query.user_id))

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"whattalk")))
    async def rip(event):
        chat_m = await event.get_chat()
        await tgbot.delete(event.chat_id)
        text2 = "Ok. Please Wait Until My Master Approves. Don't Send Another Message"
        await borg.send_message(event.query.user_id, text2)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"askme")))
    async def rip(event):
        chat_s = await event.get_chat()
        await event.edit("Request Received.")
        text3 = "Ok, Wait. You can Ask After Master Approves You"
        await borg.send_message(event.query.user_id, text3)


def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = 8
    number_of_cols = 2
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        custom.Button.inline("{} {} {}".format("🍩", x, "😬"),
                             data="us_plugin_{}".format(x))
        for x in helpable_plugins
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1], ))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[modulo_page * number_of_rows:number_of_rows *
                      (modulo_page + 1)] + [(
                          custom.Button.inline("Previous",
                                               data="{}_prev({})".format(
                                                   prefix, modulo_page)),
                          custom.Button.inline("Next",
                                               data="{}_next({})".format(
                                                   prefix, modulo_page)),
                      )]
    return pairs
