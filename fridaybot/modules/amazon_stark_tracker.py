#    Copyright (C) Midhun KM 2020-2021
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


from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fridaybot.modules.sql_helper.amazon_tracker_sql import add_new_tracker, is_tracker_in_db, rm_tracker, get_tracker_info, rm_tracker, get_all_tracker, get_all_urls
import requests
from bs4 import BeautifulSoup

@friday.on(friday_on_cmd(pattern="amt"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("`Processing..`")
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    url = event.text.split(" ", maxsplit=1)[1]
    try:
        page = requests.get(url, headers = headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find(id = "productTitle").get_text()
        price = soup.find(id = "priceblock_ourprice").get_text()
        title = title.strip()
        price = price[2:].split(',')
        price = round(float("".join(price)))
    except:
        await event.edit("**Invalid Url !**")
        return
    if is_tracker_in_db(str(url)):
        await event.edit("**Tracker Already Found In Db**")
        return
    add_new_tracker(url, price)
    await event.edit(f"Product Name : {title} \nCurrent Price : {price} \n**Added To TrackerList**")
    
@friday.on(friday_on_cmd(pattern="rmt"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("`Processing..`")
    url = event.text.split(" ", maxsplit=1)[1]
    if url == "all":
        ws = get_all_urls()
        for i in ws:
            try:
                rm_tracker(str(i))
            except:
                pass
        await event.edit("Sucessfully Removed All Trackers")
    if not is_tracker_in_db(str(url)):
        await event.edit("**Tracker Not Found In Db**")
        return
    rm_tracker(str(url))
    await event.edit(f"**Sucessfully Removed From TrackerList**")
    
async def track_amazon():
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    ws = get_all_urls() 
    if len(ws) == 0:
        return
    kk = get_all_tracker()
    for ujwal in kk:
        page = requests.get(ujwal.amazon_url, headers = headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find(id = "productTitle").get_text()
        price = soup.find(id = "priceblock_ourprice").get_text()
        title = title.strip()
        price = price[2:].split(',')
        price = round(float("".join(price)))
        if (int(price) > int(ujwal.budget)):
            await borg.send_message(Config.PRIVATE_GROUP_ID, f"#Tracker - Price Reduced \nProduct Name : {title} \nCurrent price : {price}")
            rm_tracker(str(ujwal.amazon_url))
        else:
            pass

scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(track_amazon, trigger="cron", hour=9)
scheduler.start()
