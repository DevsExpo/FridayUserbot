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


from sqlalchemy import Column, String, UnicodeText
from fridaybot.modules.sql_helper import BASE, SESSION


class Gban(BASE):
    __tablename__ = "gban"
    user_id = Column(String(14), primary_key=True)
    reason = Column(UnicodeText)

    def __init__(self, user_id, reason):
        self.user_id = user_id
        self.reason = reason


Gban.__table__.create(checkfirst=True)


def gban_user(user_id: int, reason):
    gbanner = Gban(str(user_id), str(reason))
    SESSION.add(gbanner)
    SESSION.commit()


def gban_data(user_id: int):
    try:
        s__ = SESSION.query(Gban).get(str(user_id))
        return int(s__.user_id), str(s__.reason)
    finally:
        SESSION.close()
        
def is_gbanned(user_id: int):
    try:
        s__ = SESSION.query(Gban).get(str(user_id))
        if s__:
            return str(s__.reason)
    finally:
        SESSION.close()

def ungban_user(user_id):
    ungbanner = SESSION.query(Gban).get(str(user_id))
    if ungbanner:
        SESSION.delete(ungbanner)
        SESSION.commit()
        
