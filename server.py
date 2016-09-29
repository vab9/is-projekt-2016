#! /usr/bin/env python

import config
import os
from flask import Flask, send_file
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


@app.route('/')
def index():
    # sys.stderr.write(str(app.config))
    return send_file(open('index.html'))


@app.route('/<name>')
def hello_name(name):
    return "Hello " + name


@app.route('/save-score/<player>')
def save_score(player):
    return "Hello My Friend!"
    # find player score, compare to database, save etc.


@app.route('/add_user/<vorname>/<nachname>/<geb>', methods=['GET', 'POST'])
def add_user(vorname, nachname, geb):
    return "Hello " + vorname + nachname + geb
