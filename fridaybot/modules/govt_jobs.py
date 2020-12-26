import requests
from bs4 import BeautifulSoup

from fridaybot import CMD_HELP
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd


@friday.on(friday_on_cmd(pattern=r"govtjob"))
@friday.on(sudo_cmd(pattern="govtjob", allow_sudo=True))
async def _(givejob):

    res = ""

    def getdata(url):
        r = requests.get(url)
        return r.text

    await edit_or_reply(givejob, "Trying To Fetch Jobs...")

    htmldata = getdata("https://www.sarkariresult.com/latestjob.php")

    soup = BeautifulSoup(htmldata, "html.parser")

    for li in soup.find_all("div", id="post"):
        res += li.get_text()

    lmao = "Information About Government Jobs Gathered Successfully\n\n" + str(res)

    with open("jobs.txt", "w") as job:
        job.write(lmao)
    await givejob.client.send_file(
        givejob.chat_id,
        "jobs.txt",
        reply_to=givejob.id,
    )


CMD_HELP.update(
    {
        "govtjob": "**Government Job**\
\n\n**Syntax : **`.govtjob`\
\n**Usage :** Gathers information about all the open government jobs."
    }
)
