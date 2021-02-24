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


class Anp(BASE):
    __tablename__ = "anp"
    amazon_url = Column(UnicodeText, primary_key=True)
    budget = Column(String(14))

    def __init__(self, amazon_url, budget):
        self.amazon_url = amazon_url
        self.budget = budget


Anp.__table__.create(checkfirst=True)

def add_new_tracker(amazon_url, budget: int):
    tracker_adder = Anp(str(amazon_url), str(budget))
    SESSION.add(tracker_adder)
    SESSION.commit()

def get_tracker_info(amazon_url: str):
    try:
        s__ = SESSION.query(Anp).get(str(amazon_url))
        return str(s__.budget), str(s__.amazon_url)
    finally:
        SESSION.close()
        
def is_tracker_in_db(amazon_url: str):
    try:
        s__ = SESSION.query(Anp).get(str(amazon_url))
        if s__:
            return str(s__.budget)
    finally:
        SESSION.close()
        
        
def get_all_urls():
    stark = [r.amazon_url for r in SESSION.query(Anp).all()]
    SESSION.close()
    return stark

def get_all_tracker():
    s = SESSION.query(Anp).all()
    SESSION.close()
    return s


def rm_tracker(amazon_url: str):
    warner = SESSION.query(Anp).get(str(amazon_url))
    if warner:
        SESSION.delete(warner)
        SESSION.commit()
