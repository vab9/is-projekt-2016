# Flask config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEVELOPMENT = True
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgres://localhost/serious-db'
    SECRET_KEY = 'xmu\xb1\xbe#\x9e\xceecrX\x91\x7f\xdb\xbf\x11\xf9\x18rv\xe4\x1cQ'


class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
