#    Copyright (C) Midhun KM 2020
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
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from . import BASE
from . import SESSION


class Blockedid(BASE):
    __tablename__ = "blockedid"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


Blockedid.__table__.create(checkfirst=True)


def add_nibba_in_db(chat_id: int):
    id_user = Blockedid(str(chat_id))
    SESSION.add(id_user)
    SESSION.commit()


def get_all_nibba():
    nibbaid = SESSION.query(Blockedid).all()
    SESSION.close()
    return nibbaid


def is_he_added(chat_id):
    try:
        return SESSION.query(Blockedid).filter(
            Blockedid.chat_id == str(chat_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()


def removenibba(chat_id):
    nibbanoob = SESSION.query(Blockedid).get(str(chat_id))
    if nibbanoob:
        SESSION.delete(nibbanoob)
        SESSION.commit()
