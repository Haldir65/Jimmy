from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request,Blueprint
from sqlalchemy.ext.declarative import declarative_base
import datetime
from db import mydb
from config import config
from flask_script  import Manager
from flask_migrate  import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config.config')

mydb.init_app(app)


migrate = Migrate(app, mydb)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from news.views import bluprint as news
from auth.views import auth as authentication



app.register_blueprint(news)
app.register_blueprint(authentication)