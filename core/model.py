from sqlalchemy import Integer
from sqlalchemy.dialects.postgresql import JSONB

from serious_game import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    vorname = db.Column(db.String(32), nullable=False)
    nachname = db.Column(db.String(32), nullable=False)
    geb = db.Column(db.Date, nullable=False)
    username = db.Column(db.String, nullable=False, unique=True)
    highscore = db.Column(db.Integer, default=0)
    savegame = db.Column(JSONB())

    def __init__(self, vorname, nachname, geb):
        self.vorname = vorname
        self.nachname = nachname
        self.geb = geb
        self.username = vorname + nachname + str(geb.year)
        self.highscore = 0

    def __repr__(self):
        return unicode(self.vorname + " " + self.nachname)

    def get_user(username):
        return db.session.query(User).filter(User.username == username).one_or_none()

    def update_user(self):
        # try - except block here?!
        db.session.add(self)
        db.session.commit()

    def update_highscore(self, new_score):
        if new_score > self.highscore:
            self.highscore = new_score

    def save_game(self, savegame):
        self.savegame = savegame

    def load_game(self):
        if self.savegame:
            return self.savegame
