from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request,Blueprint
from sqlalchemy.ext.declarative import declarative_base
import datetime,json
import logging
from _module1.views import blueprint as mod1
from _module2.views import blueprint as mod2


import config
from database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_database(app)
    register_bluprints(app)
    return app

def register_database(app):
    db.init_app(app)


def register_bluprints(app):
    app.register_blueprint(mod1)
    app.register_blueprint(mod2)
    

def main():
    app = create_app()
    app.run(debug=True,port=10000)

if __name__ == '__main__':
    main()
