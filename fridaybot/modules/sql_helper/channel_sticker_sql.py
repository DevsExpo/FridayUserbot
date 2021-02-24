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


class Cst(BASE):
    __tablename__ = "cst"
    chat_id = Column(String(14), primary_key=True)
    sticker_token = Column(UnicodeText)

    def __init__(self, chat_id, sticker_token):
        self.chat_id = chat_id
        self.sticker_token = sticker_token


Cst.__table__.create(checkfirst=True)


def add_new_data_in_db(chat_id: int, sticker_token):
    sticker_adder = Cst(str(chat_id), sticker_token)
    SESSION.add(sticker_adder)
    SESSION.commit()


def get_all_st_data(chat_id: int):
    try:
        s__ = SESSION.query(Cst).get(str(chat_id))
        return int(s__.chat_id), s__.sticker_token
    finally:
        SESSION.close()


def is_data_indb(chat_id: int):
    try:
        s__ = SESSION.query(Cst).get(str(chat_id))
        if s__:
            return s__.sticker_token
    finally:
        SESSION.close()


def remove_datas(chat_id):
    sed = SESSION.query(Cst).get(str(chat_id))
    if sed:
        SESSION.delete(sed)
        SESSION.commit()
