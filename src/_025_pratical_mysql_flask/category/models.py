
import config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
from sqlalchemy.ext.declarative import declarative_base
import datetime
from db import mydb
from news.models import News


