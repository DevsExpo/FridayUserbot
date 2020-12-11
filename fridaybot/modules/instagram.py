#Copyright (C) 2020 Patan Bot
#
#Don't Edit the maker of module plz, thanks
"""Userbot Module For Getting the Detail Of Instagram Profile"""

import io, time, aiohttp

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd

@friday.on(friday_on_cmd(pattern="insta (.*)"))
async def _(event):
    sample_url = (
        "https://www.instagram.com/{}/?__a=1"
    )
    input_str = event.pattern_match.group(1)
    async with aiohttp.ClientSession() as session:
        response_api_zero = await session.get(
            sample_url.format(input_str)
        )
    response_api = await response_api_zero.json()
    await event.edit(
        """
        **Username**: {}
        **Full Name**: {}
        **Followers**: {}
        **Following**: {}
        **Is Private**: {}
        **Total Post** : {}""".format(
            response_api["graphql"]["user"]["username"]",
            response_api["graphql"]["user"]["edge_followed_by"],
            response_api["graphql"]["user"]["edge_follow"],
            response_api["graphql"]["user"]["is_private"],
            response_api["graphql"]["user"]["edge_owner_to_timeline_media"]
        )
    )

CMD_HELP.update({
    "Instagram" : "**Instagram**\
        \n\n**Syntax: ** `.insta <username>`\
        \n**Usage :** Gives instagram information about the username."
})
