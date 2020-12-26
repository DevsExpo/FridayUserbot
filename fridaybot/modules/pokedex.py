#    Copyright (C) @chsaiujwal 2020
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

from pokedex import pokedex

from fridaybot import CMD_HELP
from fridaybot.utils import admin_cmd


@friday.on(admin_cmd(pattern="pokedex (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    pokedx = pokedex.Pokedex()
    pokemen = pokedx.get_pokemon_by_name(input_str)
    pokemon = pokemen[0]
    name = str(pokemon.get("name"))
    number = str(pokemon.get("number"))
    species = str(pokemon.get("species"))
    typo = pokemon.get("types")
    types = ""
    for tu in typo:
        types += str(tu) + ",  "

    lol = pokemon.get("abilities")
    lmao = lol.get("normal")
    ok = ""
    for ty in lmao:
        ok = str(ty) + ",  "

    kk = lol.get("hidden")
    hm = ""
    for pq in kk:
        hm += str(pq) + ",  "
    hell = pokemon.get("eggGroups")
    uio = ""
    for x in hell:
        uio += str(x) + ",  "

    height = pokemon.get("height")
    weight = pokemon.get("weight")
    yes = pokemon.get("family")
    Id = str(yes.get("id"))
    evo = str(yes.get("evolutionStage"))
    pol = yes.get("evolutionLine")
    xy = ""
    for p in pol:
        xy += str(p) + ",  "

    start = pokemon.get("starter")
    if start == False:
        start = "No"
    elif start == True:
        start = "True"
    else:
        pass

    leg = pokemon.get("legendary")

    if leg == False:
        leg = "No"
    elif leg == True:
        leg = "True"
    else:
        pass

    myt = pokemon.get("mythical")
    if myt == False:
        myt = "No"
    elif myt == True:
        myt = "True"
    else:
        pass
    ultra = pokemon.get("ultraBeast")

    if ultra == False:
        ultra = "No"
    elif ultra == True:
        ultra = "True"
    else:
        pass

    megA = pokemon.get("mega")

    if megA == False:
        megA = "No"
    elif megA == True:
        megA = "True"
    else:
        pass

    gEn = pokemon.get("gen")
    link = pokemon.get("sprite")
    des = pokemon.get("description")

    # hope = await borg(event.chat_id, link)
    caption = f"<b><u>Pokemon Information Gathered Successfully</b></u>\n\n\n<b>Name:-   {name}\nNumber:-  {number}\nSpecies:- {species}\nType:- {types}\n\n<u>Abilities</u>\nNormal Abilities:- {ok}\nHidden Abilities:- {hm}\nEgg Group:-  {uio}\nHeight:- {height}\nWeight:- {weight}\n\n<u>Family</u>\nID:- {Id}\nEvolution Stage:- {evo}\nEvolution Line:- {xy}\nStarter:- {start}\nLegendary:- {leg}\nMythical:- {myt}\nUltra Beast:- {ultra}\nMega:- {megA}\nGen:-  {gEn}\nDescription:-  {des}</b>"

    await borg.send_message(
        event.chat_id,
        caption,
        parse_mode="HTML",
        file=link,
        force_document=False,
        silent=True,
    )
    await event.delete()


CMD_HELP.update(
    {
        "pokedex": "**Pokedex**\
\n\n**Syntax : **`.pokedex <pokemon name>`\
\n**Usage :** Gives Information About Given Pokemon.\
\n\n**Example : **`.pokedex pikachu`\
\nThis above syntax gives Information about Pikachu"
    }
)
