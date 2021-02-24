from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd
import requests

@friday.on(friday_on_cmd(pattern="runcode ?(.*)"))
@friday.on(sudo_cmd(pattern="runcode ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        ommhg = await friday.edit_or_reply(event, "Reply To The Code idiot.")
        return
    input_str = event.pattern_match.group(1)
    if input_str == None:
      ommhg = await friday.edit_or_reply(event, "Which Language is That? select a language from here. c#, vb.net, f#, java, python, c (gcc), c++ (gcc), php, pascal, objective-c, haskell, ruby, perl, lua, nasm, sql server, javascript, lisp, prolog, go, scala, scheme, node.js, python 3, octave, c (clang), c++ (clang), c++ (vc++), c (vc), d, r, tcl, mysql, postgresql, oracle, swift, bash, ada, erlang, elixir, ocaml, kotlin, brainfuck, fortran")
      return
    langs = ["c#", "vb.net", "f#", "java", "python", "c (gcc)", "c++ (gcc)", "php", "pascal", "objective-c", "haskell", "ruby", "perl", "lua", "nasm", "sql server", "javascript", "lisp", "prolog", "go", "scala", "scheme", "node.js", "python 3", "octave", "c (clang)", "c++ (clang)", "c++ (vc++)", "c (vc)", "d", "r", "tcl", "mysql", "postgresql", "oracle", "swift", "bash", "ada", "erlang", "elixir", "ocaml", "kotlin", "brainfuck", "fortran"]
    
    input_st = input_str
    credits = "friday is the best. By Friday. Get Your Friday From @FRIDAYOT."
    
    reply_message = await event.get_reply_message()
    co = credits
    input_str = co[0]
    if input_st.lower() in langs:
      pass
    else:
      ommhg = await friday.edit_or_reply(event, "Language Not Found. select a language from here. c#, vb.net, f#, java, python, c (gcc), c++ (gcc), php, pascal, objective-c, haskell, ruby, perl, lua, nasm, sql server, javascript, lisp, prolog, go, scala, scheme, node.js, python 3, octave, c (clang), c++ (clang), c++ (vc++), c (vc), d, r, tcl, mysql, postgresql, oracle, swift, bash, ada, erlang, elixir, ocaml, kotlin, brainfuck, fortran")
      return
    
    kl = "flow language"
    if kl[0] == input_str:
      token = "5b5f0ad8-705a-4118-87d4-c0ca29939aed"
    else:
      token = "5b5f0ad8-705a-4118-87d4-c0ca29939aeb"
    dat = {
      "code":reply_message.text,
      "lang":input_st,
      "token":token
    }

    r = requests.post("https://starkapi.herokuapp.com/compiler", data = dat).json()
    
    if r.get("reason") !=None:
      a = r
      result = a.get("results")
      error = a.get("errors")
      stats = a.get("stats")
      success = a.get("success")
      warnings = a.get("warnings")
      rn = a.get("reason")
      Bobby = f"""
Results : {result}
Errors : {error}
Stats : {stats}
Success : {success}
warnings : {warnings}
Reason : {rn}
"""
    
      ommhg = await friday.edit_or_reply(event, Bobby)
      return
    
    
    a = r
    result = a.get("results")
    error = a.get("errors")
    stats = a.get("stats")
    success = a.get("success")
    warnings = a.get("warnings")
    Bobby = f"""
Results : {result}
Errors : {error}
Stats : {stats}
Success : {success}
warnings : {warnings}
"""
    
    ommhg = await friday.edit_or_reply(event, Bobby)
    
