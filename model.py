
from sqlalchemy import Column, Integer, String, Date, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('users_id_seq'), primary_key=True)
    vorname = Column(String(32))
    nachname = Column(String(32))
    geb = Column(Date)
    highscore = Column(Integer, default=0)
    savegame = Column(JSONB())

    def __init__(self, vorname, nachname, geb):
        self.vorname = vorname
        self.nachname = nachname
        self.geb = geb

    def __repr__(self):
        return self.vorname + self.nachname
