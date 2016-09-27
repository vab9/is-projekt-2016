#! /usr/bin/env python

from flask import Flask, send_file, redirect, url_for
from whitenoise import WhiteNoise

app = Flask(__name__)
noiseapp = WhiteNoise(app, root='./static/')


@app.route('/')
def index():
    return send_file(open('index.html'))


@app.route('/res/<path>')
def media_resources(path):
    return redirect(url_for('static', filename='res/' + path))


@app.route('/save-score/<player>')
def save_score(player):
    return "Hello My Friend!"
    # find player score, compare to database, save etc.




# import http.server
# import socketserver

# PORT = 8000

# Handler = http.server.SimpleHTTPRequestHandler

# httpd = socketserver.TCPServer(("127.0.0.1", PORT), Handler)

# print("serving at port", PORT)
# httpd.serve_forever()

# python3 -m http.server -b 127.0.0.1
