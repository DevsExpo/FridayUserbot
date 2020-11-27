#!/usr/bin/env python3
# -*- coding: utf-8 -*
# (c) Shrimadhav U K

"""Check Account Restrictions
.cr (.*)"""
from telethon.tl.types import Channel, Chat, User

from fridaybot.utils import friday_on_cmd


@borg.on(friday_on_cmd(pattern="cr (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    try:
        input_entity = await event.client.get_entity(input_str)
    except Exception:
        await event.edit("`Hmm...`")
        return
    else:
        await event.edit(get_restriction_string(input_entity))


def get_restriction_string(a) -> str:
    # logger.info(a.stringify())
    b = ""
    c = ""
    if isinstance(a, Channel):
        c = f"[{a.title}](https://t.me/c/{a.id}/{2})"
    elif isinstance(a, User):
        c = f"[{a.first_name}](tg://user?id={a.id})"
    elif isinstance(a, Chat):
        c = f"{a.title}"
        b = f"{c}: __basic groups do not have restriction in Telegram__, **to the best of our knowledge**"
        return b
    else:
        c = "something wnorgings while checking restriction_reason 😒😒"
    if a.restriction_reason is None or len(a.restriction_reason) == 0:
        b = f"{c}: **Good News**! No Limitations are currently applied to this Group / Channel / Bot"
    else:
        tmp_string = f"{c} has the following restriction_reason(s): \n"
        for a_r in a.restriction_reason:
            tmp_string += f"👉 {a_r.reason}-{a_r.platform}: {a_r.text}\n\n"
        b = tmp_string
    # b += "\n\n" + Translation.POWERED_BY_SE
    return b
