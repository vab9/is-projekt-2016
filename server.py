#! /usr/bin/env python

from flask import Flask, request, send_file
from whitenoise import WhiteNoise

app = Flask(__name__)
# root should really point to a sub-directory. This is a security hole
noiseapp = WhiteNoise(app, root='./static/')

@app.route('/')
def index():
    return send_file(open('index.html'))

@app.route('/kaum')
def test():
    return "Hello My Friend!"




# import http.server
# import socketserver

# PORT = 8000

# Handler = http.server.SimpleHTTPRequestHandler

# httpd = socketserver.TCPServer(("127.0.0.1", PORT), Handler)

# print("serving at port", PORT)
# httpd.serve_forever()

# python3 -m http.server -b 127.0.0.1
