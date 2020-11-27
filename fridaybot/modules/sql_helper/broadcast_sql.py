#    Copyright (C) 2020 @HeisenbergTheDanger

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


from sqlalchemy import Column, String

from . import BASE, SESSION


class Broadcast(BASE):
    __tablename__ = "Broadcast"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


Broadcast.__table__.create(checkfirst=True)


def add_chnnl_in_db(chat_id: int):
    chnnl_id = Broadcast(str(chat_id))
    SESSION.add(chnnl_id)
    SESSION.commit()


def get_all_chnnl():
    stark = SESSION.query(Broadcast).all()
    SESSION.close()
    return stark


def already_added(chat_id):
    try:
        return SESSION.query(Broadcast).filter(Broadcast.chat_id == str(chat_id)).one()
    except:
        return None
    finally:
        SESSION.close()


def rm_channel(chat_id):
    remove = SESSION.query(Broadcast).get(str(chat_id))
    if remove:
        SESSION.delete(remove)
        SESSION.commit()
