from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request,Blueprint
from sqlalchemy.ext.declarative import declarative_base
import datetime,json,logging
from flask_script  import Manager
from flask_migrate  import Migrate, MigrateCommand
from news.views import bluprint as news
from auth.views import auth as authentication
from config import config
from db import mydb




def create_app():
    app = Flask(__name__)
    app.config.from_object('config.config')
    mydb.init_app(app)
    return app


def create_table():
    app = Flask(__name__)
    app.config.from_object('config.config')
    app.app_context().push()
    mydb.init_app(app)
    from news.models import News,Newscate,User
    mydb.create_all()
    mydb.session.commit()



def register_blueprints(app):
    app.register_blueprint(news)
    app.register_blueprint(authentication)

    