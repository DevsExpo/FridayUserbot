#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

try:
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient
except BaseException:
    print("Telethon Not Found. Installing Now.")
    import os

    os.system("pip install telethon")
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient
ok = """ ____  ____  __  ____   __   _  _
(  __)(  _ \(  )(    \ / o\ ( \/ )
 ) _)  )   / )(  ) D (/    \ )  /
(__)  (__\_)(__)(____/\_/\_/(__/
"""
print(ok)
APP_ID = int(input("Enter APP ID here: \n"))
API_HASH = input("Enter API HASH here: \n")

client = TelegramClient(StringSession(), APP_ID, API_HASH)
with client:
    session_str = client.session.save()
    client.send_message("me", f"`{session_str}`")
    client.send_message(
        "THIS IS YOUR STRING SESSION \nJoin @FRIDAYOT For More Support."
    )
    print("⬆ Please Check Your Telegram Saved Message For Your String.")
