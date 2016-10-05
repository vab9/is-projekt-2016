#! /usr/bin/env python

# import core.config
import config
import logging
import os
import sys

from flask import Flask, send_file, request, json
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


@app.route('/')
def index():
    return send_file(open('index.html'))


@app.route('/test')
def test_page():
    return send_file(open('test.html'))


@app.route('login', methods=['POST'])
def login():
    try:
        vorname = request.form['vorname']
        nachname = request.form['nachname']
        geb = parse_date(request.form['geburtstag'])
    except Exception as e:
        raise e
        return "Unable to parse login form...", 500
    requested_usrname = vorname + nachname + unicode(geb.date())
    usr = User.query.filter_by(User.username == requested_usrname).first_or_404()
    return usr.make_json_data(), 200





@app.route('/register', methods=['POST'])
def register():
    # should do more validation here!
    try:
        vorname = request.form['vorname']
        nachname = request.form['nachname']
        geb = parse_date(request.form['geburtstag'])

    except Exception as e:
        # sys.stderr.write(('===========\n', error, '===========\n'))
        raise e
        return "Unable to parse registration form...", 500

    try:
        new_user = User(vorname, nachname, geb)
        db.session.add(new_user)
        db.session.commit()
    except:
        return "Unable to save " + unicode(new_user) + " to database...", 503
    return new_user.make_json_data(), 200


# Do this with username instead, can be computed in JS
@app.route('/retrieve/<userid>')
def retrieve(userid):
    return User.get_user(userid).vorname


@app.route('/save-score/<player>')
def save_score(player):
    return "Hello My Friend!"
    # find player score, compare to database, save etc.


@app.route('/savegame', methods=['POST'])
def save_game():
    return str(request.form.values()[0])
    # ('sg', type=str)



@app.route('/add_user/<vorname>/<nachname>/<geb>', methods=['GET', 'POST'])
def add_user(vorname, nachname, geb):
    new_user = User(vorname, nachname, geb)
    return str(new_user)
