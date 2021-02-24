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
from apscheduler.executors.asyncio import AsyncIOExecutor
import requests
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from fridaybot.modules.sql_helper import server_pinger_sql as warnerstark

if Config.PING_SERVERS:
    @friday.on(friday_on_cmd(pattern="aping"))
    async def _(event):
        if event.fwd_from:
            return
        await event.edit("`Processing..`")
        url = event.text.split(" ", maxsplit=1)[1]
        if warnerstark.is_ping_indb(str(url)):
            await event.edit("**Server Already Found In Db !**")
            return
        warnerstark.add_ping(url)
        await event.edit(f"**URL :** `{url}` **Sucessfully Added To Db**")
    @friday.on(friday_on_cmd(pattern="rping"))
    async def _(event):
        if event.fwd_from:
            return
        await event.edit("`Processing..`")
        url = event.text.split(" ", maxsplit=1)[1]
        if not warnerstark.is_ping_indb(str(url)):
            await event.edit("**Server Not Found In Db !**")
            return
        warnerstark.rmping(url)
        await event.edit(f"**URL :** `{url}` **Sucessfully Removed From Db**")
    
    async def ping_servers():
        hmm_p = 0
        url_s = warnerstark.get_all_url()
        header_s = {"User-Agent": 'Server Pinged By @FridayOT'}
        if len(url_s) == 0:
            return
        for i in url_s:
            try:
              ws = requests.get(url=i.url, headers=header_s).status_code
              logger.info(f"Pinged {i.url} // Status Code Recived : {ws}")
            except:
              hmm_p += 1
        success_l = len(url_s) - hmm_p
        logger.info(f"Sucessfully Pinged {success_l} Urls Out Of {len(url_s)}")
    
    
    scheduler = AsyncIOScheduler(
        executors={
    'default': AsyncIOExecutor(),
        }
    )
    scheduler.add_job(ping_servers, 'interval', minutes=Config.PING_SERVER_EVERY_MINUTE_VALUE)
    scheduler.start()
