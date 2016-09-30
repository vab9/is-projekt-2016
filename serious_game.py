#! /usr/bin/env python

# import core.config
import config
import os
import sys

from flask import Flask, send_file, request
from flask_sqlalchemy import SQLAlchemy
from whitenoise import WhiteNoise

app = Flask(__name__)
noiseapp = WhiteNoise(app, root='./static/')
db = SQLAlchemy(app)

# Custom or Default Config
if 'APP_SETTINGS' in os.environ:
    app.config.from_object(os.environ['APP_SETTINGS'])
else:
    app.config.from_object(config.Config)

# need to suppress PEP8 E402 warning here
# from core import User

from core.model import User


@app.route('/')
def index():
    return send_file(open('index.html'))


@app.route('/register', methods=['POST'])
def register():
    # should do more validation here!
    try:
        vorname = request.form['reg_vorname']
        nachname = request.form['reg_nachname']
        geb = request.form['reg_geb']
    except:
        return "Unable to process request form..."

    try:
        new_user = User(vorname, nachname, geb)
        db.session.add(new_user)
        db.session.commit()
    except:
        return "Unable to save " + new_user + " to database..."



@app.route('/<name>')
def hello_name(name):
    error = str(request)
    sys.stderr.writelines(('===========\n', error, '===========\n'))
    return "Hello " + name


@app.route('/save-score/<player>')
def save_score(player):
    return "Hello My Friend!"
    # find player score, compare to database, save etc.


@app.route('/add_user/<vorname>/<nachname>/<geb>', methods=['GET', 'POST'])
def add_user(vorname, nachname, geb):
    new_user = User(vorname, nachname, geb)
    return str(new_user)
