#! /usr/bin/env python

# import core.config
import config
import logging
import os
import sys

from flask import Flask, send_file, request
from flask_sqlalchemy import SQLAlchemy
from whitenoise import WhiteNoise
from dateutil.parser import parse as parse_date

# init flask app
app = Flask(__name__)

# Custom or Default Config
if 'APP_SETTINGS' in os.environ:
    app.config.from_object(os.environ['APP_SETTINGS'])
else:
    app.config.from_object(config.Config)

# WhiteNoise for static file delivery
noiseapp = WhiteNoise(app, root='./static/')
db = SQLAlchemy(app)

# Turn on logging
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

# EXTRA IMPORT
# need to suppress PEP8 E402 warning here
from core.model import User


####################
# BEGINNING ROUTES #
####################

@app.route('/')
def index():
    return send_file(open('index.html'))


@app.route('/anmelden', methods=['POST'])
def register():
    # should do more validation here!
    try:
        vorname = request.form['vorname']
        nachname = request.form['nachname']
        geb = parse_date(request.form['geburtstag'])

    except Exception as e:
        raise e
        return "Unable to parse form...", 500

    # look for unique username in db
    requested_usrname = vorname + nachname + unicode(geb.date())
    usr = User.query.filter_by(username=requested_usrname).first()

    if usr is None:
        # register new user
        try:
            new_user = User(vorname, nachname, geb)
            db.session.add(new_user)
            db.session.commit()
        except:
            return "Unable to save " + unicode(new_user) + " to database...", 503
        # initial score of 0
        new_user.score = 0
        return new_user.make_json_data(), 200
    else:
        # return existing user info
        return usr.make_json_data(), 200


@app.route('/savegame', methods=['POST'])
def save_game():
    username = request.form.keys()[0]
    # sg = json.loads(request.form[username])
    sg = request.form[username]
    # query for existing user, return 404 if not
    usr = User.query.filter_by(username=username).first_or_404()
    usr.savegame = sg
    usr.update_highscore()
    db.session.commit()
    return str(request.form.values()[0]), 200


@app.route('/loadgame/<userid>')
def load_game(userid):
    # should already be JSON
    sg = User.query.get_or_404(userid).savegame
    if sg is None:
        return "Dieser User hat noch kein Spielstand gespeichert. ", 404
    else:
        return sg, 200


###########################

# Do this with username instead, can be computed in JS
@app.route('/retrieve/<userid>')
def retrieve(userid):
    return User.get_user(userid).vorname


# do this by saving a game
# @app.route('/save-highscore/<player>')
# def save_score(player):
#     return "Hello My Friend!"
#     # find player score, compare to database, save etc.
