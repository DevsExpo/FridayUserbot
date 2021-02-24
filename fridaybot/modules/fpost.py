# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
""" Command: .fpost word

credit: @pureindialover"""

import string

from uniborg.util import friday_on_cmd

msg_cache = {}


@friday.on(friday_on_cmd(pattern=r"fpost\s+(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    text = event.pattern_match.group(1)
    destination = await event.get_input_chat()

    for c in text.lower():
        if c not in string.ascii_lowercase:
            continue
        if c not in msg_cache:
            async for msg in borg.iter_messages(None, search=c):
                if msg.raw_text.lower() == c and msg.media is None:
                    msg_cache[c] = msg
                    break
        await borg.forward_messages(destination, msg_cache[c])
