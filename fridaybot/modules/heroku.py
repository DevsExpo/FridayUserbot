# Copyright (C) 2020 Adek Maulana.
# All rights reserved.
"""
   Heroku manager for your fridaybot
"""
import asyncio
import math
import os

import heroku3
import requests

from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd

Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"


@friday.on(friday_on_cmd(pattern="usage$", outgoing=True))
@friday.on(sudo_cmd(pattern="usage$", allow_sudo=True))
async def dyno_usage(dyno):
    """
    Get your account Dyno Usage
    """
    await edit_or_reply(dyno, "`Trying To Fetch Dyno Usage....`")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {Var.HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await edit_or_reply(
            dyno, "`Error: something bad happened`\n\n" f">.`{r.reason}`\n"
        )
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]
    """ - Used - """
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    """ - Current - """
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)

    await asyncio.sleep(1.5)

    return await edit_or_reply(
        dyno,
        "**Dyno Usage Data**:\n\n"
        f"✗ **APP NAME =>** `{Var.HEROKU_APP_NAME}` \n"
        f"✗ **Usage in Hours And Minutes =>** `{AppHours}h`  `{AppMinutes}m`"
        f"✗ **Usage Percentage =>** [`{AppPercentage} %`]\n"
        "\n\n"
        "✗ **Dyno Remaining This Months 📆:**\n"
        f"✗ `{hours}`**h**  `{minutes}`**m** \n"
        f"✗ **Percentage :-** [`{percentage}`**%**]",
    )


@friday.on(friday_on_cmd(pattern="logs$", outgoing=True))
@friday.on(sudo_cmd(pattern="logs$", allow_sudo=True))
async def _(givelogs):
    try:
        Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
        app = Heroku.app(Var.HEROKU_APP_NAME)
    except:
        return await givelogs.reply(
            " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku var !"
        )
    await edit_or_reply(givelogs, "`Trying To Fetch Logs...`")
    with open("logs.txt", "w") as log:
        log.write(app.get_log())
    await givelogs.client.send_file(
        givelogs.chat_id,
        "logs.txt",
        reply_to=givelogs.id,
        caption="Logs Collected Using Heroku \n For More Support Visit @FridayOT",
    )
    await edit_or_reply(givelogs, "`Logs Send Sucessfully ! `")
    await asyncio.sleep(5)
    await givelogs.delete()
    return os.remove("logs.txt")
