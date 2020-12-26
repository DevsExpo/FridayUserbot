import requests
from yahoo_fin import stock_info as si

from fridaybot import CMD_HELP
from fridaybot.utils import admin_cmd


@friday.on(admin_cmd(pattern="liveprice (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    try:
        a = si.get_live_price(input_str)

        def get_symbol(symbol):
            url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(
                symbol
            )
            result = requests.get(url).json()
            for x in result["ResultSet"]["Result"]:
                if x["symbol"] == symbol:
                    return x["name"]

        lmao = input_str.upper()
        company = get_symbol(lmao)
        if company == None:
            await event.edit(
                f"<b><u>Stock Information Gathered Successfully</b></u> \n\n<b>Live Price of <code>{lmao}</code> is:-  $</b> <code>{a}</code> USD",
                parse_mode="HTML",
            )
        else:
            await event.edit(
                f"<b><u>Stock Information Gathered Successfully</b></u> \n\n<b>Live Price of <code>{company}</code> is:-  $</b> <code>{a}</code> USD",
                parse_mode="HTML",
            )
    except AssertionError:
        await event.edit("There Is No Such Ticker.")


CMD_HELP.update(
    {
        "stock_price": "**Stock Price**\
\n\n**Syntax : **`.liveprice <Share Ticker>`\
\n**Usage :** Shows Live Price Of Given Shares.\
\n\n**Example : **`.liveprice tsla`\
\nThis above syntax shows Tesla's share price in USD."
    }
)
