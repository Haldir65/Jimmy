from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request,Blueprint
from sqlalchemy.ext.declarative import declarative_base
import datetime,json
from flask_script  import Manager
from flask_migrate  import Migrate, MigrateCommand




db = SQLAlchemy()


def init_app(app):
    db.init_app(app)
    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    return manager




