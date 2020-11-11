#    Copyright (C) Midhun KM 2020
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
import emoji
from googletrans import Translator


@assistant_cmd("tr", is_args=True)
async def _(event):
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "en"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await tgbot.send_message(event.chat_id,
                                 "`.tr LanguageCode` as reply to a message")
        return
    text = emoji.demojize(text.strip())
    lan = lan.strip()
    translator = Translator()
    translated = translator.translate(text, dest=lan)
    after_tr_text = translated.text
    output_str = (
        f"**Translated By Friday Assistant Bot** \n"
        f"Source {translated.src} \nTranslation {lan} \nWhat I Can Translate From This {after_tr_text}"
    )
    try:
        await tgbot.send_message(event.chat_id, output_str)
    except Exception:
        await tgbot.send_message(event.chat_id, "Something Went Wrong 🤔")
