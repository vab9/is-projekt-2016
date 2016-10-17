#! /usr/bin/env python

# import core.config
import config
import logging
import os
import sys

from flask import Flask, send_file, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from whitenoise import WhiteNoise
from datetime import date
from dateutil.parser import parse as parse_date
from dateutil.relativedelta import *

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

    # check date in range
    if geb.year not in range(1890, 2020):
        return "Unrealistisches Geburtsjahr", 400

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
        return new_user.make_json_data(), 201
    else:
        # return existing user info
        return usr.make_json_data(), 200


@app.route('/savegame', methods=['POST'])
def save_game():
    """Save a game state to the database and return the user it belongs to or 404"""
    data = request.get_json(force=True)

    username = data['username']
    usr = User.query.filter_by(username=username).first_or_404()

    # do i need to call json.dumps(data) ???
    usr.savegame = data

    if 'score' in data:
        score = data['score']
        usr.update_highscore(score)

    db.session.commit()
    return usr.make_json_data(), 200


@app.route('/loadgame/<int:userid>')
def load_game(userid):
    """Tries to load a savegame from the database and returns it or 404"""
    # this should be a dict of unicode strings...
    sg = User.query.get_or_404(userid).savegame
    if sg is None:
        return "Dieser User hat noch keinen Spielstand gespeichert. ", 404
    else:
        return jsonify(sg), 200


@app.route('/bestenliste')
def bestenliste():
    """Sends Top 10 List to client"""
    best_users = User.query.add_columns(User.vorname, User.nachname, User.geb, User.highscore).order_by(User.highscore.desc()).limit(10).all()
    res = []
    # get today once
    today = date.today()

    for usr in best_users:
        # get age
        age = relativedelta(today, usr.geb).years
        age = age if age > 0 else 0
        res.append({
            'vorname': usr.vorname,
            'nachname': usr.nachname,
            'alter': age,
            'highscore': usr.highscore
        })
    return jsonify(res), 200

###########################

# Do this with username instead, can be computed in JS
# @app.route('/retrieve/<userid>')
# def retrieve(userid):
#     return User.get_user(userid).vorname
