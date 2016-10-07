from sqlalchemy.dialects.postgresql import JSONB
from serious_game import db
from flask import json


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
        self.username = vorname + nachname + unicode(geb.date())
        self.highscore = 0

    def __repr__(self):
        return unicode(self.vorname + " " + self.nachname)

    @classmethod
    def get_user(cls, userid):
        new_user = db.session.query(User).get(userid)
        return new_user

    def make_json_data(self):
        data = {
            'vorname': self.vorname,
            'nachname': self.nachname,
            'geburtstag': self.geb,
            'userid': self.id,
            'username': self.username,
            'highscore': self.highscore,
        }
        if hasattr(self, "score"):
            data['score'] = self.score
        return json.jsonify(data)

    def update_user(self):
        # try - except block here?!
        db.session.add(self)
        db.session.commit()

    def update_highscore(self, score):
        if score > self.highscore:
            self.highscore = score

    def save_game(self, savegame):
        self.savegame = savegame

    def load_game(self):
        if self.savegame:
            return self.savegame
