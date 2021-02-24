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

from sqlalchemy import Column, UnicodeText

from fridaybot.modules.sql_helper import BASE, SESSION


class Serverpinger(BASE):
    __tablename__ = "serverpinger"
    url = Column(UnicodeText, primary_key=True)

    def __init__(self, url):
        self.url = url


Serverpinger.__table__.create(checkfirst=True)


def add_ping(url):
    pinger = Serverpinger(url)
    SESSION.add(pinger)
    SESSION.commit()


def rmping(url):
    rmpinger = SESSION.query(Serverpinger).get(url)
    if rmpinger:
        SESSION.delete(rmpinger)
        SESSION.commit()


def get_all_url():
    stark = SESSION.query(Serverpinger).all()
    SESSION.close()
    return stark


def is_ping_indb(url):
    try:
        return SESSION.query(Serverpinger).filter(Serverpinger.url == url).one()
    except:
        return None
    finally:
        SESSION.close()
