#    Copyright (C) @chsaiujwal 2020-2021
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


import requests
from fridaybot import CMD_HELP
from fridaybot.utils import admin_cmd
from fridaybot.Configs import Config

@friday.on(admin_cmd(pattern="fpl"))
async def _(event):
    if event.fwd_from:
        return
    
    if Config.FOOTBALL_API_KEY is None:
      await event.edit("Need to get an API key from https://rapidapi.com/api-sports/api/api-football-beta\nModule stopping!")
      return
    
    appo = Config.FOOTBALL_API_KEY
    url = "https://api-football-beta.p.rapidapi.com/standings"
    querystring = {"season":"2020","league":"39"}
    headers = {'x-rapidapi-key': appo,'x-rapidapi-host': "api-football-beta.p.rapidapi.com"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    a = response.json()
    b = a.get("response")
    c = b[0]
    d = c.get('league')
    e = d.get('name')
    f = d.get("country")
    logo = d.get("logo")
    season = d.get("season")
    g = d.get("standings")
    h = g[0]
    i = h[0]
    rank = i.get("rank")
    k = i.get("team")
    nomo = k.get("name")

    pont = i.get("points")
    kk = i.get("all")
    pl = kk.get("played")
    wein = kk.get("win")
    yqw= kk.get("draw")
    pol = kk.get("lose")
    nex = h[1]
    new = nex.get("rank")
    np = nex.get("team")
    nee = np.get("name")
    popo = nex.get("points")
    oloq = nex.get("all")
    pl1 = oloq.get("played")
    wein1 = oloq.get("win")
    yqw1 = oloq.get("draw")
    pol1 = oloq.get("lose")


    nex2 = h[2]
    new2 = nex2.get("rank")
    np2 = nex2.get("team")
    nee2 = np2.get("name")
    popo2 = nex2.get("points")
    oloq2 = nex2.get("all")
    pl2 = oloq2.get("played")
    wein2 = oloq2.get("win")
    yqw2 = oloq2.get("draw")
    pol2 = oloq2.get("lose")

    nex3 = h[3]
    new3 = nex3.get("rank")
    np3 = nex3.get("team")
    nee3 = np3.get("name")
    popo3 = nex3.get("points")
    oloq3 = nex3.get("all")
    pl3 = oloq3.get("played")
    wein3 = oloq3.get("win")
    yqw3 = oloq3.get("draw")
    pol3 = oloq3.get("lose")

    nex4 = h[4]
    new4 = nex4.get("rank")
    np4 = nex4.get("team")
    nee4 = np4.get("name")
    popo4 = nex4.get("points")
    oloq4 = nex4.get("all")
    pl4 = oloq4.get("played")
    wein4 = oloq4.get("win")
    yqw4 = oloq4.get("draw")
    pol4 = oloq4.get("lose")


    caption = f"""<b>{e}</b>
<b>Country:- {f}
season = {season}

Standings
Rank:- {rank}
Name:- {nomo}
points:- {pont}
Played:- {pl}
win:- {wein} 
Draw:- {yqw}
Lose:- {pol}

Rank:- {new}
Name:- {nee}
points:- {popo}
Win:- {wein1}
Draw:- {yqw1}
Lose:- {pol1}

Rank:- {new2}
Name:- {nee2}
points:- {popo2}
Win:- {wein2}
Draw:- {yqw2}
Lose:- {pol2}

Rank:- {new3}
Name:- {nee3}
points:- {popo3}
Win:- {wein3}
Draw:- {yqw3}
Lose:- {pol3}

Rank:- {new4}
Name:- {nee4}
points:- {popo4}
Win:- {wein4}
Draw:- {yqw4}
Lose:- {pol4}</b>
"""

    await borg.send_message(
        event.chat_id,
        caption,
        parse_mode="HTML",
        file=logo,
        force_document=False,
        silent=True,
    )
    await event.delete()

@friday.on(admin_cmd(pattern="ffl"))
async def _(event):
    if event.fwd_from:
        return
    
    if Config.FOOTBALL_API_KEY is None:
      await event.edit("Need to get an API key from https://rapidapi.com/api-sports/api/api-football-beta\nModule stopping!")
      return
    
    appo = Config.FOOTBALL_API_KEY
    url = "https://api-football-beta.p.rapidapi.com/standings"
    querystring = {"season":"2020","league":"61"}
    headers = {'x-rapidapi-key': appo,'x-rapidapi-host': "api-football-beta.p.rapidapi.com"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    a = response.json()
    b = a.get("response")
    c = b[0]
    d = c.get('league')
    e = d.get('name')
    f = d.get("country")
    logo = d.get("logo")
    season = d.get("season")
    g = d.get("standings")
    h = g[0]
    i = h[0]
    rank = i.get("rank")
    k = i.get("team")
    nomo = k.get("name")

    pont = i.get("points")
    kk = i.get("all")
    pl = kk.get("played")
    wein = kk.get("win")
    yqw= kk.get("draw")
    pol = kk.get("lose")
    nex = h[1]
    new = nex.get("rank")
    np = nex.get("team")
    nee = np.get("name")
    popo = nex.get("points")
    oloq = nex.get("all")
    pl1 = oloq.get("played")
    wein1 = oloq.get("win")
    yqw1 = oloq.get("draw")
    pol1 = oloq.get("lose")


    nex2 = h[2]
    new2 = nex2.get("rank")
    np2 = nex2.get("team")
    nee2 = np2.get("name")
    popo2 = nex2.get("points")
    oloq2 = nex2.get("all")
    pl2 = oloq2.get("played")
    wein2 = oloq2.get("win")
    yqw2 = oloq2.get("draw")
    pol2 = oloq2.get("lose")

    nex3 = h[3]
    new3 = nex3.get("rank")
    np3 = nex3.get("team")
    nee3 = np3.get("name")
    popo3 = nex3.get("points")
    oloq3 = nex3.get("all")
    pl3 = oloq3.get("played")
    wein3 = oloq3.get("win")
    yqw3 = oloq3.get("draw")
    pol3 = oloq3.get("lose")

    nex4 = h[4]
    new4 = nex4.get("rank")
    np4 = nex4.get("team")
    nee4 = np4.get("name")
    popo4 = nex4.get("points")
    oloq4 = nex4.get("all")
    pl4 = oloq4.get("played")
    wein4 = oloq4.get("win")
    yqw4 = oloq4.get("draw")
    pol4 = oloq4.get("lose")


    caption = f"""<b>{e}</b>
<b>Country:- {f}
season = {season}

Standings
Rank:- {rank}
Name:- {nomo}
points:- {pont}
Played:- {pl}
win:- {wein} 
Draw:- {yqw}
Lose:- {pol}

Rank:- {new}
Name:- {nee}
points:- {popo}
Win:- {wein1}
Draw:- {yqw1}
Lose:- {pol1}

Rank:- {new2}
Name:- {nee2}
points:- {popo2}
Win:- {wein2}
Draw:- {yqw2}
Lose:- {pol2}

Rank:- {new3}
Name:- {nee3}
points:- {popo3}
Win:- {wein3}
Draw:- {yqw3}
Lose:- {pol3}

Rank:- {new4}
Name:- {nee4}
points:- {popo4}
Win:- {wein4}
Draw:- {yqw4}
Lose:- {pol4}</b>
"""

    await borg.send_message(
        event.chat_id,
        caption,
        parse_mode="HTML",
        file=logo,
        force_document=False,
        silent=True,
    )
    await event.delete()

@friday.on(admin_cmd(pattern="fuefa$"))
async def _(event):
    if event.fwd_from:
        return
    
    if Config.FOOTBALL_API_KEY is None:
      await event.edit("Need to get an API key from https://rapidapi.com/api-sports/api/api-football-beta\nModule stopping!")
      return
    
    appo = Config.FOOTBALL_API_KEY
    url = "https://api-football-beta.p.rapidapi.com/standings"
    querystring = {"season":"2020","league":"2"}
    headers = {'x-rapidapi-key': appo,'x-rapidapi-host': "api-football-beta.p.rapidapi.com"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    a = response.json()
    b = a.get("response")
    c = b[0]
    d = c.get('league')
    e = d.get('name')
    f = d.get("country")
    logo = d.get("logo")
    season = d.get("season")
    g = d.get("standings")
    h = g[0]
    i = h[0]
    rank = i.get("rank")
    k = i.get("team")
    nomo = k.get("name")

    pont = i.get("points")
    kk = i.get("all")
    pl = kk.get("played")
    wein = kk.get("win")
    yqw= kk.get("draw")
    pol = kk.get("lose")
    nex = h[1]
    new = nex.get("rank")
    np = nex.get("team")
    nee = np.get("name")
    popo = nex.get("points")
    oloq = nex.get("all")
    pl1 = oloq.get("played")
    wein1 = oloq.get("win")
    yqw1 = oloq.get("draw")
    pol1 = oloq.get("lose")


    nex2 = h[2]
    new2 = nex2.get("rank")
    np2 = nex2.get("team")
    nee2 = np2.get("name")
    popo2 = nex2.get("points")
    oloq2 = nex2.get("all")
    pl2 = oloq2.get("played")
    wein2 = oloq2.get("win")
    yqw2 = oloq2.get("draw")
    pol2 = oloq2.get("lose")

    nex3 = h[3]
    new3 = nex3.get("rank")
    np3 = nex3.get("team")
    nee3 = np3.get("name")
    popo3 = nex3.get("points")
    oloq3 = nex3.get("all")
    pl3 = oloq3.get("played")
    wein3 = oloq3.get("win")
    yqw3 = oloq3.get("draw")
    pol3 = oloq3.get("lose")


    caption = f"""<b>{e}</b>
<b>Country:- {f}
season = {season}

Standings
Rank:- {rank}
Name:- {nomo}
points:- {pont}
Played:- {pl}
win:- {wein} 
Draw:- {yqw}
Lose:- {pol}

Rank:- {new}
Name:- {nee}
points:- {popo}
Win:- {wein1}
Draw:- {yqw1}
Lose:- {pol1}

Rank:- {new2}
Name:- {nee2}
points:- {popo2}
Win:- {wein2}
Draw:- {yqw2}
Lose:- {pol2}

Rank:- {new3}
Name:- {nee3}
points:- {popo3}
Win:- {wein3}
Draw:- {yqw3}
Lose:- {pol3}
"""

    await borg.send_message(
        event.chat_id,
        caption,
        parse_mode="HTML",
        file=logo,
        force_document=False,
        silent=True,
    )
    await event.delete()


CMD_HELP.update(
    {
        "football": "**Football**\
\n\n**Syntax : **`.fpl`\
\n**Usage :** Shows Premier League's Standings.\
\n\n**Syntax : **`.ffl`\
\n**Usage :** Shows French Ligue1 Standings.\
\n\n**Syntax : **`.fuefa`\
\n**Usage :** Shows UEFA championship Standings."
    }
)
