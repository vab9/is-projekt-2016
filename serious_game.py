#! /usr/bin/env python

# import core.config
import config
import logging
import os
import sys

from flask import Flask, send_file, request
from flask_sqlalchemy import SQLAlchemy
from whitenoise import WhiteNoise

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


@app.route('/register', methods=['POST'])
def register():
    # should do more validation here!
    try:
        vorname = request.form['reg_vorname']
        nachname = request.form['reg_nachname']
        geb = request.form['reg_geb']

    except Exception as e:
        error = str(e)
        sys.stderr.write(('===========\n', error, '===========\n'))
        raise e
        return "Unable to process request form...", 500

    try:
        new_user = User(vorname, nachname, geb)
        db.session.add(new_user)
        db.session.commit()
    except:
        return "Unable to save " + str(new_user) + " to database..."
    return unicode(new_user) + " erfolgreich registriert!", 204
    # return "Successfully registered " + str(new_user)


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
