
import asyncio
import time
from userbot.utils import friday_on_cmd
from userbot import CMD_HELP


@borg.on(friday_on_cmd(pattern="^.webupload ?(.+?|) (?:--)(anonfiles|transfer|filebin|anonymousfiles|megaupload|bayfiles|ninja)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("`Processing ...`")
    PROCESS_RUN_TIME = 100
    input_str = event.pattern_match.group(1)
    selected_transfer = event.pattern_match.group(2)
    if input_str:
        file_name = input_str
    else:
        reply = await event.get_reply_message()
        file_name = await borg.download_media(reply.media, Var.TEMP_DOWNLOAD_DIRECTORY)
    CMD_WEB = {
        "anonfiles": 'curl -F "file=@{}" https://anonfiles.com/api/upload',
        "transfer": 'curl --upload-file "{}" https://transfer.sh/{os.path.basename(file_name)}',
        "filebin": 'curl -X POST --data-binary "@test.png" -H "filename: {}" "https://filebin.net"',
        "anonymousfiles": 'curl -F file="@{}" https://api.anonymousfiles.io/',
        "megaupload": 'curl -F "file=@{}" https://megaupload.is/api/upload',
        "ninja": "curl -i -F file=@{} https://tmp.ninja/api.php?d=upload-tool",
        "bayfiles": '.exec curl -F "file=@{}" https://bayfiles.com/api/upload',
    }
    try:
        selected_one = CMD_WEB[selected_transfer].format(file_name)
    except KeyError:
        await event.edit("Invalid selected transfer. Do .ahelp webupload to know more.")
    cmd = selected_one
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    await event.edit(f"{stdout.decode()}")


CMD_HELP.update(
    {
        "webupload": "**Webupload**\
\n\n**Syntax : **`.webupload --<anonfiles/transfer/filebin/anonymousfiles/megaupload/bayfiles><reply to the file you want to upload>`\
\n**Usage :** upload file in the website and provides Download link."
    }
)
