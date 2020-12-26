import asyncio
import math
import os

import heroku3
import requests

from fridaybot.function.heroku_helper import HerokuHelper
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd

Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"


@friday.on(friday_on_cmd(pattern="(logs|log)"))
@friday.on(sudo_cmd(pattern="(logs|log)", allow_sudo=True))
async def giblog(event):
    herokuHelper = HerokuHelper(Var.HEROKU_APP_NAME, Var.HEROKU_API_KEY)
    logz = herokuHelper.getLog()
    with open("logs.txt", "w") as log:
        log.write(logz)
    await borg.send_file(
        event.chat_id, "logs.txt", caption=f"**Logs Of {Var.HEROKU_APP_NAME}**"
    )


@friday.on(friday_on_cmd(pattern="(rerun|restarts)"))
@friday.on(sudo_cmd(pattern="(restart|restarts)", allow_sudo=True))
async def restart_me(event):
    herokuHelper = HerokuHelper(Var.HEROKU_APP_NAME, Var.HEROKU_API_KEY)
    await event.edit("`App is Restarting. This is May Take Upto 10Min.`")
    herokuHelper.restart()


@friday.on(friday_on_cmd(pattern="usage$"))
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


@friday.on(
    friday_on_cmd(pattern="(set|get|del) var(?: |$)(.*)(?: |$)([\s\S]*)", outgoing=True)
)
@friday.on(
    sudo_cmd(pattern="(set|get|del) var(?: |$)(.*)(?: |$)([\s\S]*)", allow_sudo=True)
)
async def variable(var):
    """
    Manage most of ConfigVars setting, set new var, get current var,
    or delete var...
    """
    if Var.HEROKU_APP_NAME is not None:
        app = Heroku.app(Var.HEROKU_APP_NAME)
    else:
        return await edit_or_reply(
            var, "`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**"
        )
    exe = var.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "get":
        await edit_or_reply(var, "`Getting information...`")
        await asyncio.sleep(1.5)
        try:
            variable = var.pattern_match.group(2).split()[0]
            if variable in heroku_var:
                return await edit_or_reply(
                    var,
                    "**ConfigVars**:" f"\n\n`{variable} = {heroku_var[variable]}`\n",
                )
            else:
                return await edit_or_reply(
                    var, "**ConfigVars**:" f"\n\n`Error:\n-> {variable} don't exists`"
                )
        except IndexError:
            configs = prettyjson(heroku_var.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                if len(result) >= 4096:
                    await var.client.send_file(
                        var.chat_id,
                        "configs.json",
                        reply_to=var.id,
                        caption="`Output too large, sending it as a file`",
                    )
                else:
                    await edit_or_reply(
                        var,
                        "`[HEROKU]` ConfigVars:\n\n"
                        "================================"
                        f"\n```{result}```\n"
                        "================================",
                    )
            os.remove("configs.json")
            return
    elif exe == "set":
        await edit_or_reply(var, "`Setting information...`")
        variable = var.pattern_match.group(2)
        if not variable:
            return await edit_or_reply(var, ">`.set var <ConfigVars-name> <value>`")
        value = var.pattern_match.group(3)
        if not value:
            variable = variable.split()[0]
            try:
                value = var.pattern_match.group(2).split()[1]
            except IndexError:
                return await edit_or_reply(var, ">`.set var <ConfigVars-name> <value>`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await edit_or_reply(
                var, f"**{variable}**  `successfully changed to`  ->  **{value}**"
            )
        else:
            await edit_or_reply(
                var, f"**{variable}**  `successfully added with value`  ->  **{value}**"
            )
        heroku_var[variable] = value
    elif exe == "del":
        await edit_or_reply(var, "`Getting information to deleting variable...`")
        try:
            variable = var.pattern_match.group(2).split()[0]
        except IndexError:
            return await edit_or_reply(
                var, "`Please specify ConfigVars you want to delete`"
            )
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await edit_or_reply(var, f"**{variable}**  `successfully deleted`")
            del heroku_var[variable]
        else:
            return await edit_or_reply(var, f"**{variable}**  `is not exists`")


@friday.on(friday_on_cmd(pattern="shp ?(.*)"))
async def lel(event):
    cpass, npass = event.pattern_match.group(1).split(" ", 1)
    await event.edit("`Changing You Pass`")
    accountm = Heroku.account()
    accountm.change_password(cpass, npass)
    await event.edit(f"`Done !, Changed You Pass to {npass}")


@friday.on(friday_on_cmd(pattern="acolb (.*)"))
async def sf(event):
    hmm = event.pattern_match.group(1)
    app = Heroku.app(Var.HEROKU_APP_NAME)
    collaborator = app.add_collaborator(user_id_or_email=hmm, silent=0)
    await event.edit("`Sent Invitation To Accept Your Collab`")


@friday.on(friday_on_cmd(pattern="tfa (.*)"))
async def l(event):
    hmm = event.pattern_match.group(1)
    app = Heroku.app(Var.HEROKU_APP_NAME)
    transfer = app.create_transfer(recipient_id_or_name=hmm)


@friday.on(friday_on_cmd(pattern="kd (.*)"))
async def killdyno(event):
    app = Heroku.app(Var.HEROKU_APP_NAME)
    await event.edit("`Dyno Is Off. Manually Turn it On Later`")
    app.kill_dyno("bash start.sh")


def prettyjson(obj, indent=2, maxlinelength=80):
    """Renders JSON content with indentation and line splits/concatenations to fit maxlinelength.
    Only dicts, lists and basic types are supported"""

    items, _ = getsubitems(
        obj,
        itemkey="",
        islast=True,
        maxlinelength=maxlinelength - indent,
        indent=indent,
    )
    return indentitems(items, indent, level=0)
