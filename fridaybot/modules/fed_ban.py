from fridaybot.function import fetch_feds
from fridaybot.modules.sql_helper.feds_sql import (
    add_fed,
    get_all_feds,
    is_fed_indb,
    rmfed,
)
from fridaybot.utils import friday_on_cmd

chnnl_grp = Config.FBAN_GROUP


@friday.on(friday_on_cmd(pattern="fadd ?(.*)"))
async def _(event):
    nolol = 0
    yeslol = 0
    await event.edit("`Processing..`")
    lol_s = event.pattern_match.group(1)
    if lol_s == None:
        await event.edit("`Give FeD ID`")
        return
    elif lol_s == " ":
        await event.edit("`Give FeD ID`")
        return
    elif lol_s == "all":
        hmm = await fetch_feds(event, borg)
        for i in hmm:
            try:
                if is_fed_indb(i):
                    nolol += 1
                elif not is_fed_indb(i):
                    add_fed(i)
                    yeslol += 1
            except:
                pass
        await event.edit(f"`Added {yeslol} Feds To DB, Failed To Add {nolol} Feds.`")
    elif is_fed_indb(lol_s):
        await event.edit("`Fed Already Found On DataBase.`")
        return
    elif not is_fed_indb(lol_s):
        add_fed(lol_s)
        await event.edit("`Done ! Added This Fed To DataBase`")


@friday.on(friday_on_cmd(pattern="frm ?(.*)"))
async def _(event):
    lol_s = event.pattern_match.group(1)
    await event.edit("`Processing..`")
    lol = get_all_feds()
    if lol_s == None:
        await event.edit("`Give FeD ID`")
        return
    elif lol_s == " ":
        await event.edit("`Give FeD ID`")
        return
    elif lol_s == "all":
        for sedm in lol:
            rmfed(sedm.feds)
        await event.edit("`Done, Cleared. All Fed Database.")
    elif is_fed_indb(lol_s):
        rmfed(lol_s)
        await event.edit("`Done, Removed This FeD From DB`")
    elif not is_fed_indb(lol_s):
        await event.edit("`This Fed Not Found On Db.`")


@friday.on(friday_on_cmd(pattern="fban ?(.*)"))
async def _(event):
    lol_s = event.pattern_match.group(1)
    if lol_s == None:
        await event.edit("`No user Found To Fban.`")
        return
    all_fed = get_all_feds()
    errors = 0
    len_feds = len(all_fed)
    if len_feds == 0:
        await event.edit("`No Fed IN DB, Add One To Do So.`")
        return
    await event.edit(f"`FBanning in {len_feds} Feds.`")
    try:
        await borg.send_message(chnnl_grp, "/start")
    except Exception as e:
        await event.edit("**Errors** : " + str(e))
        return
    for teamz in all_fed:
        try:
            await borg.send_message(chnnl_grp, "/joinfed " + teamz.feds)
            await borg.send_message(chnnl_grp, "/fban " + lol_s)
            await asyncio.sleep(5)
        except:
            errors += 1
    await event.edit(
        f"**Fban Completed** \nTotal Sucess : `{errors - len_feds}` \nTotal Errors : `{errors}` \nTotal Fed Len : `{len_feds}`"
    )


@friday.on(friday_on_cmd(pattern="unfban ?(.*)"))
async def _(event):
    lol_s = event.pattern_match.group(1)
    if lol_s == None:
        await event.edit("`No user Found To Fban.`")
        return
    all_fed = get_all_feds()
    errors = 0
    len_feds = len(all_fed)
    await event.edit(f"`UnFBanning in {len_feds} Feds.`")
    try:
        await borg.send_message(chnnl_grp, "/start")
    except Exception as e:
        await event.edit("**Errors** : " + str(e))
        return
        for teamz in all_fed:
            try:
                await borg.send_message(chnnl_grp, "/unfban " + lol_s)
                await asyncio.sleep(5)
            except:
                errors += 1
    await event.edit(
        f"**Un-Fban Completed** \nTotal Sucess : `{errors - len_feds}` \nTotal Errors : `{errors}` \nTotal Fed Len : `{len_feds}`"
    )
