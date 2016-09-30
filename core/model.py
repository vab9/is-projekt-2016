from sqlalchemy import Integer
from sqlalchemy.dialects.postgresql import JSONB

from serious_game import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    vorname = db.Column(db.String(32))
    nachname = db.Column(db.String(32))
    geb = db.Column(db.Date)
    highscore = db.Column(db.Integer, default=0)
    savegame = db.Column(JSONB())

    def __init__(self, vorname, nachname, geb):
        self.vorname = vorname
        self.nachname = nachname
        self.geb = geb

    def __repr__(self):
        return self.vorname + self.nachname
