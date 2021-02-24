import re

import requests as HTTP
from bs4 import BeautifulSoup as SOUP

from fridaybot import CMD_HELP
from fridaybot.utils import admin_cmd


@friday.on(admin_cmd(pattern="rmovie (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)

    def main(emotion):
        if emotion == "Sad":
            urlhere = "http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc"

        elif emotion == "Anticipation":
            urlhere = "https://www.imdb.com/search/title/?genres=sci-fi"

        elif emotion == "Fear":
            urlhere = "http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc"

        elif emotion == "Enjoyment":
            urlhere = "http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc"

        elif emotion == "Trust":
            urlhere = "http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc"

        elif emotion == "Romantic":
            urlhere = "https://www.imdb.com/search/title/?genres=romance"

        elif emotion == "Comedy":
            urlhere = "https://www.imdb.com/search/title/?genres=comedy"

        response = HTTP.get(urlhere)

        data = response.text
        soup = SOUP(data, "lxml")
        title = soup.find_all("a", attrs={"href": re.compile(r"\/title\/tt+\d*\/")})
        return title

    emotion = input_str
    a = main(emotion)
    count = 0
    sed = ""
    if emotion == "Disgust" or emotion == "Anger" or emotion == "Surprise":
        for i in a:
            tmp = str(i).split(">;")
            if len(tmp) == 3:
                lol = tmp[1][:-3]
                sed += lol + "\n"
                if count > 13:
                    break
                count += 1

    else:
        for i in a:
            tmp = str(i).split(">")
            if len(tmp) == 3:
                lol = tmp[1][:-3]
                sed += lol + "\n"
            if count > 11:
                break
            count += 1
    await event.edit(
        f"<b><u>Below Are Your Movie Recommendations</b></u>\n\n<b>Your Emotion:- <code>{input_str}</code>\n<b>Recommended Movie List:- </b><code>{sed}</code>",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "movie_recommendation": "**Movie Recommender**\
\n\n**Syntax : **`.rmovie <emotion>`\
\n**Usage :** Recommends Movies According To Your Emotion.\
\n\n**Example : **`.rmovie Sad`\
\nThis above syntax shows recommended mobies for a sad person.\
\n\n**Note : ** Emotions are case sensitive.\
\n\n\n**Available Emotions : ** `Sad`\n`Trust`\n`Fear`\n`Enjoyment`\n`Romantic`\n`Comedy`\n`Anticipation`"
    }
)
