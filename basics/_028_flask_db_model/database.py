from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request,Blueprint
from sqlalchemy.ext.declarative import declarative_base
import datetime,json




db = SQLAlchemy()


def init_app(app):
    db.init_app(app)




