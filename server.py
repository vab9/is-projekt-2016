#! /usr/bin/env python

import os
from flask import Flask, send_file
from whitenoise import WhiteNoise

app = Flask(__name__)
noiseapp = WhiteNoise(app, root='./static/')

# Debugging on
app.debug = True


@app.route('/')
def index():
    return send_file(open('index.html'))


@app.route('/<name>')
def hello_name(name):
    return "Hello " + name


@app.route('/save-score/<player>')
def save_score(player):
    return "Hello My Friend!"
    # find player score, compare to database, save etc.


if 'DATABASE_URL' in os.environ('DATABASE_URL'):
    db_url = os.environ('DATABASE_URL')
else:
    db_url = 'postgres://serious-db'
