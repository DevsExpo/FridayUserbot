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


from sqlalchemy import Column, String

from . import BASE, SESSION


class Botchecker(BASE):
    __tablename__ = "botchecker"
    bot_username = Column(String(14), primary_key=True)
    def __init__(self, bot_username):
        self.bot_username = bot_username


Botchecker.__table__.create(checkfirst=True)


def add_bot_in_db(bot_username: int):
    bot_id = Botchecker(str(bot_username))
    SESSION.add(bot_id)
    SESSION.commit()


def get_all_bot():
    warner = SESSION.query(Botchecker).all()
    SESSION.close()
    return warner


def is_bot_already_added(bot_username):
    try:
        return SESSION.query(Botchecker).filter(Botchecker.bot_username == str(bot_username)).one()
    except:
        return None
    finally:
        SESSION.close()


def rm_bot(bot_username):
    remove = SESSION.query(Botchecker).get(str(bot_username))
    if remove:
        SESSION.delete(remove)
        SESSION.commit()
