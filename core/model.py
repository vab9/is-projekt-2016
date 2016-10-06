from sqlalchemy.dialects.postgresql import JSONB
from serious_game import db
from flask import json

import sys


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

    def update_highscore(self):
        # get new score from savegame
        # self.savegame is a dictionary
        passages = json.loads(self.savegame['savegame-value'])
        # sg is now a list of dictionaries that contain passage and variable info

        score = 0
        # look for score variable in savegame
        for passage in passages:
            if passage['passage'] == 'Hauptseite':
                score = passage['variables']['score']
                break
        # update hs in model - calling functions should commit db session
        if score > self.highscore:
            self.highscore = score


    def save_game(self, savegame):
        self.savegame = savegame

    def load_game(self):
        if self.savegame:
            return self.savegame
