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
