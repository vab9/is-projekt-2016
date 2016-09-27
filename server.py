#! /usr/bin/env python

from flask import Flask, send_file
from whitenoise import WhiteNoise

app = Flask(__name__)
noiseapp = WhiteNoise(app, root='./static/')


@app.route('/')
def index():
    return send_file(open('index.html'))


@app.route('/save-score/<player>')
def save_score(player):
    return "Hello My Friend!"
    # find player score, compare to database, save etc.
