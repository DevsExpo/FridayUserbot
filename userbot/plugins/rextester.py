#    Copyright (C) 2020

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


from rextester_py import rexec

from userbot import CMD_HELP
from userbot.Configs import Config
from userbot.utils import admin_cmd


@bot.on(admin_cmd(pattern="rex"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Processing ...")
    evtxt = event.text.split(" ", maxsplit=1)[1]
    try:
        lang = evtxt.split("//", maxsplit=1)[0]
        cmd = evtxt.split("//", maxsplit=1)[1]
    except BaseException:
        return await event.edit(
            f"Syntax - \n`{Config.COMMAND_HAND_LER}rex language//code`\nLanguages can be found [here](https://github.com/nitanmarcel/rextester_py#languages)."
        )

    try:
        res = rexec(lang, cmd, None).results
        err = rexec(lang, cmd, None).errors
        wrns = rexec(lang, cmd, None).warnings
        # statt = rexec(lang, cmd, None).stats
    except Exception as e:
        if str(e) == "Unknown language":
            return await event.edit(
                "**ERROR**:\n`Unknown Language!!\nCheck available languages `[here](https://github.com/nitanmarcel/rextester_py#languages)"
            )
        return await event.edit(f"**ERROR:**\n`{str(e)}`")
    out = f"**CɪᴘʜᴇʀX Ⲃⲟⲧ Rⲉⲭⲧⲉⲋⲧⲉʀ**\n\n**Ⳑⲁⲛⳋυⲁⳋⲉ:** `{lang}`\n**Ⲥⲟⲇⲉ:** `{cmd}`\n\n**Ⲟυⲧⲣυⲧ:** `{res}`\n\n"
    if err is not None:
        out += f"**Error:** `{err}`\n\n"
    if wrns is not None:
        out += f"**Warnings:** `{wrns}`\n\n"
    # reducing time taken...
    # out += f"**Stats:** `{statt}`"

    await event.edit(out)


CMD_HELP.update(
    {
        "rextester": ".rex <language>//<codes>\
        \nUse - Run codes of any language inside telegram. Available languages can be found [here](https://github.com/nitanmarcel/rextester_py#languages)."
    }
)
