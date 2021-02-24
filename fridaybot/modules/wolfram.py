#    Copyright (C) 2021 by @InukaAsith
#    This programme is a part of Friday Userbot project
#
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


from requests import get
from telethon import *
from telethon.tl import functions, types
from telethon.tl.types import *
import os
import subprocess
from fridaybot.Configs import Config
import requests
from gtts import gTTS, gTTSError
from fridaybot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
from fridaybot.utils import friday_on_cmd


WOLFRAM_ID = Config.WOLFRAM_ID
IBM_WATSON_CRED_URL = Config.IBM_WATSON_CRED_URL
IBM_WATSON_CRED_PASSWORD = Config.IBM_WATSON_CRED_PASSWORD

@friday.on(friday_on_cmd("fridayask (.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        i = event.pattern_match.group(1)
        appid = WOLFRAM_ID
        server = f"https://api.wolframalpha.com/v1/spoken?appid={appid}&i={i}"
        res = get(server)
        if "Wolfram Alpha did not understand" in res.text:
            await event.edit(
                "Sorry, Friday's AI systems couldn't recognized your question.."
            )
            return
        await event.edit(f"**{i}**\n\n" + res.text, parse_mode="markdown")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        required_file_name = await borg.download_media(
            previous_message, TEMP_DOWNLOAD_DIRECTORY
        )
        if IBM_WATSON_CRED_URL is None or IBM_WATSON_CRED_PASSWORD is None:
            await event.edit(
                "You need to set the required ENV variables for this module. \nModule stopping"
            )
        else:
            headers = {
                "Content-Type": previous_message.media.document.mime_type,
            }
            data = open(required_file_name, "rb").read()
            response = requests.post(
                IBM_WATSON_CRED_URL + "/v1/recognize",
                headers=headers,
                data=data,
                auth=("apikey", IBM_WATSON_CRED_PASSWORD),
            )
            r = response.json()
            if "results" in r:

                results = r["results"]
                transcript_response = ""
                for alternative in results:
                    alternatives = alternative["alternatives"][0]
                    transcript_response += " " + str(alternatives["transcript"])
                if transcript_response != "":
                    string_to_show = "{}".format(transcript_response)
                    appid = WOLFRAM_ID
                    server = f"https://api.wolframalpha.com/v1/spoken?appid={appid}&i={string_to_show}"
                    res = get(server)
                    answer = res.text
                    try:
                        tts = gTTS(answer, tld="com", lang="en")
                        tts.save("results.mp3")
                    except AssertionError:
                        return
                    except ValueError:
                        return
                    except RuntimeError:
                        return
                    except gTTSError:
                        return
                    with open("results.mp3", "r"):
                        await borg.send_file(
                            event.chat_id,
                            "results.mp3",
                            voice_note=True,
                            reply_to=event.id,
                        )
                    os.remove("results.mp3")
                    os.remove(required_file_name)
                elif (
                    transcript_response == "Wolfram Alpha did not understand your input"
                ):
                    try:
                        answer = "Sorry, Friday's AI system can't understand you.."
                        tts = gTTS(answer, tld="com", lang="en")
                        tts.save("results.mp3")
                    except AssertionError:
                        return
                    except ValueError:
                        return
                    except RuntimeError:
                        return
                    except gTTSError:
                        return
                    with open("results.mp3", "r"):
                        await borg.send_file(
                            event.chat_id,
                            "results.mp3",
                            voice_note=True,
                            reply_to=event.id,
                        )
                    os.remove("results.mp3")
                    os.remove(required_file_name)
            else:
                await event.edit("API Failure !")
                os.remove(required_file_name)

                



CMD_HELP.update(
    {
        "wolfram": "**Wolfram**\
\n\n**Syntax : **`.fridayask <question>`\
\n**Usage :** Get Answers For The Questions\
\n**Example : **`.fridayask where is Taj Mahal Located?`\
\n\n**Syntax :** `.fridayask <reply to voice audio>`\
\n**Syntax : **Reply to a voice query and get the results in voice output.\
\n**Note : ** The question should be a meaningful one otherwise you will get no response !"
    }
)