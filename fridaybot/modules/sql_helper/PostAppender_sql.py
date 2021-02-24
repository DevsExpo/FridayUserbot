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

from sqlalchemy import Boolean, Column, String, UnicodeText

from fridaybot.modules.sql_helper import BASE, SESSION


class Pa(BASE):
    __tablename__ = "pa"
    chat_id = Column(String(14), primary_key=True)
    textto_append = Column(UnicodeText)
    append_foot = Column(Boolean, default=False)

    def __init__(self, chat_id, textto_append, append_foot):
        self.chat_id = chat_id
        self.append_foot = append_foot
        self.textto_append = textto_append


Pa.__table__.create(checkfirst=True)


def add_new_datas_in_db(chat_id: int, textto_append, append_foot):
    setting_adder = Pa(str(chat_id), textto_append, append_foot)
    SESSION.add(setting_adder)
    SESSION.commit()


def get_all_setting_data(chat_id: int):
    try:
        s__ = SESSION.query(Pa).get(str(chat_id))
        return int(s__.chat_id), s__.append_foot, s__.textto_append
    finally:
        SESSION.close()


def is_data_indbs(chat_id: int):
    try:
        s__ = SESSION.query(Pa).get(str(chat_id))
        if s__:
            return s__.textto_append
    finally:
        SESSION.close()


def is_footer(chat_id: int):
    try:
        s__ = SESSION.query(Pa).get(str(chat_id))
        if s__:
            return s__.append_foot
    finally:
        SESSION.close()


def remove_dataz(chat_id):
    lul = SESSION.query(Pa).get(str(chat_id))
    if lul:
        SESSION.delete(lul)
        SESSION.commit()
