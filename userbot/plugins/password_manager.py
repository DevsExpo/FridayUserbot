import os.path

from userbot import CMD_HELP
from userbot.utils import friday_on_cmd, sudo_cmd

sedpath = "./cipherx/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)


@friday.on(friday_on_cmd("savepass ?(.*)"))
@friday.on(sudo_cmd("savepass ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    ujwal = input_str.split(":")
    usermail = ujwal[0]
    passwd = ujwal[1]
    webo = ujwal[2]
    if os.path.exists("./cipherx/info.pablo"):
        file = open("./cipherx/info.pablo", "a")
    else:
        file = open("./cipherx/info.pablo", "x")
        file.close()
        file = open("./cipherx/info.pablo", "a")

    userName = usermail
    password = passwd
    website = webo

    usrnm = "UserName: " + userName + "\n"
    pwd = "Password: " + password + "\n"
    web = "Website: " + website + "\n"

    file.write("---------------------------------\n")
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write("---------------------------------\n")
    file.write("\n")
    file.close
    await event.edit(
        f"<b><u>Password Saved Successfully</b></u>",
        parse_mode="HTML",
    )


@friday.on(friday_on_cmd(pattern=r"viewpass"))
async def hi(event):
    if event.fwd_from:
        return
    file = open("./cipherx/info.pablo", "r")
    content = file.read()
    file.close()
    await event.edit(
        f"<b><u>Here are your Saved Passwords</u></b>\n<code>{content}</code>",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "password_manager": "**Password Manager**\
\n\n**Syntax : **`.savepass email:password:website`\
\n**Usage :** Saves the email, password and website.\
\n\n**Syntax : **`.viewpass`\
\n**Usage :** View all your saved emails and passwords.\
\n\n**Example : **`.savepass myemail@gmail.com:mypassword:netflix.com`\
\nThis above syntax is saving my Netflix account email and password."
    }
)
