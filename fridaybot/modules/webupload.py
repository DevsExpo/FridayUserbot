# credits: SNAPDRAGON (@s_n_a_p_s)

import asyncio
import time
from fridaybot.utils import friday_on_cmd
from fridaybot import CMD_HELP


@borg.on(friday_on_cmd(pattern="(webupload|wu) (anonfiles|transfer|filebin|anonymousfiles|megaupload|bayfiles|ninja)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("`Processing ...`")
    PROCESS_RUN_TIME = 100
    sedlyf = event.pattern_match.group(1)
    if '//' in sedlyf:
        selected_transfer, file_name = selected_transfer.split("//", 1)
    else:
        if not event.reply_to_msg_id:
            await event.edit("**Failed !, Reply To File Or Give File Path**")
            return
        selected_transfer = event.pattern_match.group(1)
        reply = await event.get_reply_message()
        file_name = await borg.download_media(reply.media, Config.TEMP_DOWNLOAD_DIRECTORY)
    CMD_WEB = {
        "anonfiles": 'curl -F "file=@{}" https://anonfiles.com/api/upload',
        "transfer": 'curl --upload-file "{}" https://transfer.sh/{os.path.basename(file_name)}',
        "filebin": 'curl -X POST --data-binary "@test.png" -H "filename: {}" "https://filebin.net"',
        "anonymousfiles": 'curl -F file="@{}" https://api.anonymousfiles.io/',
        "megaupload": 'curl -F "file=@{}" https://megaupload.is/api/upload',
        "ninja": "curl -i -F file=@{} https://tmp.ninja/api.php?d=upload-tool",
        "bayfiles": 'curl -F "file=@{}" https://bayfiles.com/api/upload',
    }
    try:
        selected_one = CMD_WEB[selected_transfer].format(file_name)
    except:
        await event.edit("Invalid selected Transfer. Do .ahelp webupload to Know More.")
        return
    cmd = selected_one
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    k = stdout.decode()
    if len(k) >= 4096:
        out_file = k
        url = "https://del.dog/documents"
        r = requests.post(url, data=out_file.encode("UTF-8")).json()
        url2 = f"https://del.dog/{r['key']}"
        starky = f"Check Json Respose [Here]({url2})"
    else:
        starky = k
    await event.edit(starky)


CMD_HELP.update(
    {
        "webupload": "**Webupload**\
\n\n**Syntax : **`.webupload <anonfiles/transfer/filebin/anonymousfiles/megaupload/bayfiles><reply to the file you want to upload>`\
\n**Usage :** upload file in the website and provides Download link."
    }
)
