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
        self.username = vorname + nachname + unicode(geb.date())
        self.highscore = 0

    def __repr__(self):
        return unicode(self.vorname + " " + self.nachname)

    # @classmethod
    # def get_user(cls, username):
    #     # Try to create new instance from database and return it ?!?!?!
    #     return db.session.query(User).filter(User.username == username).one_or_none()

    @classmethod
    def get_user(cls, userid):
        new_user = db.session.query(User).get(userid)
        return new_user

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
