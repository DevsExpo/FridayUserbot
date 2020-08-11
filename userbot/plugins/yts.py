import os
import re
import requests
from userge import userge, Message


@userge.on_cmd("yts", about={
    'header': "YTS Movie Search.",
    'description': """To Download .torrent file from YTS.
By default it'll download first 5 matched torrents and quality is 720p.""",
    'usage': "{tr}yts [Movie name] [-limit] [-quality]",
    'examples': "{tr}yts lion king -l10 -q1080p"})
async def yts(message: Message):
    qual = None
    max_limit = 5

    input_ = message.input_or_reply_str
    get_limit = re.compile(r'-l\d*[0-9]')
    get_quality = re.compile(r'-q\d*[PpDd]')
    _movie = re.sub(r'-\w*', "", input_).strip()

    if get_limit.search(input_) is None and get_quality.search(input_) is None:
        pass
    elif get_quality.search(input_) is not None and get_limit.search(input_) is not None:
        qual = get_quality.search(input_).group().strip('-q')
        max_limit = int(get_limit.search(input_).group().strip('-l'))
    elif get_quality.search(input_):
        qual = get_quality.search(input_).group().strip('-q')
    elif get_limit.search(input_):
        max_limit = int(get_limit.search(input_).group().strip('-l'))
    if len(input_) == 0:
        await message.edit("No Input Found!, check .help yts", del_in=5)
        return
    URL = "https://yts.mx/api/v2/list_movies.json?query_term={query}&limit={limit}"
    await message.edit("Fetching....")
    resp = requests.get(URL.format(query=_movie, limit=max_limit))
    datas = resp.json()
    if datas['status'] != "ok":
        await message.edit("WRONG STATUS")
        return
    if datas['data']['movie_count'] == 0 or len(datas['data']) == 3:
        await message.edit(f"{_movie} Not Found!", del_in=5)
        return
    _matches = datas['data']['movie_count']
    await message.edit(f"{_matches} Matches Found!, Sending {len(datas['data']['movies'])}.")
    for data in datas['data']['movies']:
        _title = data['title_long']
        _rating = data['rating']
        _language = data['language']
        _torrents = data['torrents']
        def_quality = "720p"
        _qualities = []
        for i in _torrents:
            _qualities.append(i['quality'])
        if qual in _qualities:
            def_quality = qual
        qualsize = [f"{j['quality']}: {j['size']}" for j in _torrents]
        capts = f'''
Title: {_title}
Rating: {_rating}
Language: {_language}
Size: {_torrents[_qualities.index(def_quality)]['size']}
Type: {_torrents[_qualities.index(def_quality)]['type']}
Seeds: {_torrents[_qualities.index(def_quality)]['seeds']}
Date Uploaded: {_torrents[_qualities.index(def_quality)]['date_uploaded']}
Available in: {qualsize}'''
        if def_quality in _qualities:
            files = f"{_title}{_torrents[_qualities.index(def_quality)]['quality']}.torrent"
            files = files.replace('/', '\\')
            with open(files, 'wb') as f:
                f.write(requests.get(_torrents[_qualities.index(def_quality)]['url']).content)
            await userge.send_document(chat_id=message.chat.id,
                                       document=files,
                                       caption=capts,
                                       disable_notification=True)
            os.remove(files)
        else:
            message.edit("NOT FOUND", del_in=5)
            return
    return