
import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))

import config
from _025_pratical_mysql_flask.db import mydb

from sqlalchemy.orm import mapper
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey



from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
from sqlalchemy.ext.declarative import declarative_base
import datetime

# 一对多关系，一个分类下有多条新闻记录
class Newscate(mydb.Model):
    __tablename__ = 'newscate'
    cate_id = Column(mydb.Integer, primary_key=True)
    cate_name = Column(mydb.String(50), nullable=False)
    cate_title = Column(mydb.String(50), nullable=False)
    newses = mydb.relationship('News', backref='newscate', lazy=True)
    def __repr__(self):
        return '<Newscate %r>' % self.cate_name


# 一对多关系，一个编辑人下有多条新闻记录
class User(mydb.Model):
    __tablename__ = 'user'
    user_id = Column(mydb.Integer, primary_key=True,autoincrement=True)
    user_name = Column(mydb.String(60), nullable=False)
    user_password = Column(mydb.String(30), nullable=False)
    user_nickname = Column(mydb.String(50), nullable=False)
    user_email = Column(mydb.String(100), nullable=False)
    newses = mydb.relationship('News', backref='user', lazy=True)
    def __repr__(self):
        return '<User %r>' % self.user_nickname

class News(mydb.Model):
    __tablename__ = 'news'
    news_id = Column(mydb.Integer, primary_key=True)
    news_date = Column(mydb.DateTime, nullable=False,default=datetime.datetime.utcnow)
    news_content = Column(mydb.Text, nullable=False)
    news_title = Column(mydb.String(100), nullable=False)
    news_excerpt = Column(mydb.Text, nullable=False)
    news_status = Column(mydb.String(20), nullable=False)
    news_modified = Column(mydb.DateTime, nullable=False)
    news_author = Column(mydb.Integer, mydb.ForeignKey('user.user_id'), nullable=False)
    news_category = Column(mydb.Integer, mydb.ForeignKey('newscate.cate_id'), nullable=False)
    def __repr__(self):
        return '<News %r>' % self.news_title
