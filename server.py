#! /usr/bin/env python

from flask import Flask

app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'HELP! !'

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
