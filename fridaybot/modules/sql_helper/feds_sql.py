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


class Fed(BASE):
    __tablename__ = "fed"
    feds = Column(UnicodeText, primary_key=True)

    def __init__(self, feds):
        self.feds = feds


Fed.__table__.create(checkfirst=True)


def add_fed(feds):
    feddy = Fed(feds)
    SESSION.add(feddy)
    SESSION.commit()


def rmfed(feds):
    rmfeddy = SESSION.query(Fed).get(feds)
    if rmfeddy:
        SESSION.delete(rmfeddy)
        SESSION.commit()


def get_all_feds():
    stark = SESSION.query(Fed).all()
    SESSION.close()
    return stark


def is_fed_indb(feds):
    try:
        return SESSION.query(Fed).filter(Fed.feds == feds).one()
    except:
        return None
    finally:
        SESSION.close()
