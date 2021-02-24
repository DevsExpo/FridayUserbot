
import io
import sys
import traceback
from fridaybot import CMD_HELP

from fridaybot.utils import friday_on_cmd, edit_or_reply



@friday.on(friday_on_cmd(pattern="math ?(.*)"))
async def _(car):
    if car.fwd_from:
        return
    cmd = car.text.split(" ", maxsplit=1)[1]
    event = await friday.edit_or_reply(car, "Calculating ...")
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    san = f"print({cmd})"
    try:
        await aexec(san, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Sorry I can't find result for the given equation"
    final_output = "**EQUATION**: `{}` \n\n **SOLUTION**: \n`{}` \n".format(
        cmd, evaluation
    )
    await event.edit(final_output)


async def aexec(code, event):
    exec(f"async def __aexec(event): " + "".join(f"\n {l}" for l in code.split("\n")))
    return await locals()["__aexec"](event)


CMD_HELP.update(
    {
        "calc": "**Plugin : **`math`\
        \n\n**Syntax : **`.math expression` \
        \n**Function : **solves the given maths equation by BODMAS rule. "
    }
)
