from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
import datetime,json,logging

app = Flask(__name__)
app.config.from_object("config.config")
db = SQLAlchemy(app)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

# 一对多关系，一个分类下有多条新闻记录
class Newscate(db.Model):
    __tablename__ = 'newscate'
    cate_id = Column(db.Integer, primary_key=True)
    cate_name = Column(db.String(50), nullable=False)
    cate_title = Column(db.String(50), nullable=False)
    newses = db.relationship('News', backref='newscate', lazy=True)
    def __repr__(self):
        return '<Newscate %r>' % self.cate_name


# 一对多关系，一个编辑人下有多条新闻记录
class User(db.Model):
    __tablename__ = 'user'
    user_id = Column(db.Integer, primary_key=True,autoincrement=True)
    user_name = Column(db.String(60), nullable=False)
    user_password = Column(db.String(30), nullable=False)
    user_nickname = Column(db.String(50), nullable=False)
    user_email = Column(db.String(100), nullable=False)
    newses = db.relationship('News', backref='user', lazy=True)
    def __repr__(self):
        return '<User %r>' % self.user_nickname

class News(db.Model):
    __tablename__ = 'news'
    news_id = Column(db.Integer, primary_key=True)
    news_date = Column(db.DateTime, nullable=False,default=datetime.datetime.utcnow)
    news_content = Column(db.Text, nullable=False)
    news_title = Column(db.String(100), nullable=False)
    news_excerpt = Column(db.Text, nullable=False)
    news_status = Column(db.String(20), nullable=False)
    news_modified = Column(db.DateTime, nullable=False)
    news_author = Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    news_category = Column(db.Integer, db.ForeignKey('newscate.cate_id'), nullable=False)
    def __repr__(self):
        return '<News %r>' % self.news_title        


def main():
    pass

if __name__ == '__main__':
    main()        