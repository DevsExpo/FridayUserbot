from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import UnicodeText

from . import BASE
from . import SESSION


class Fban(BASE):
    __tablename__ = "fban"
    fedids = Column(UnicodeText, primary_key=True)

    def __init__(self, fedids):
        self.fedids = fedids


Fban.__table__.create(checkfirst=True)


def add_fed_in_db(fedids):
    fed_id = Fban(fedids)
    SESSION.add(fed_id)
    SESSION.commit()


def get_all_fed():
    fed_ids = SESSION.query(Fban).all()
    SESSION.close()
    return fed_ids


def remove_fed(fedids):
    fednibba = SESSION.query(Fban).get(fedids)
    if fednibba:
        SESSION.delete(fednibba)
        SESSION.commit()


def already_added_fed(fedids):
    try:
        return SESSION.query(Fban).filter(Fban.fedsid is fedids).one()
    except BaseException:
        return None
    finally:
        SESSION.close()
