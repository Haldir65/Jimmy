from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey

from database import db


class User(db.Model):
    __tablename__="t_user"
    __table_args__ = {"useexisting": True}
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(60), nullable=False)
    user_password = db.Column(db.String(30), nullable=False)
    user_nickname = db.Column(db.String(50), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    newses = db.relationship('News', backref='user', lazy=True)
    def __repr__(self):
        return '<User %r>' % self.user_nickname


class Newscate(db.Model):
    __tablename__="t_newscat"
    __table_args__ = {"useexisting": True}
    cate_id = db.Column(db.Integer, primary_key=True)
    cate_name = db.Column(db.String(50), nullable=False)
    cate_title = db.Column(db.String(50), nullable=False)
    newses = db.relationship('models.News', backref='newscate', lazy=True)
    def __repr__(self):
        return '<Newscate %r>' % self.cate_name



class News(db.Model):
    __tablename__="t_news"
    __table_args__ = {"useexisting": True}
    news_id = db.Column(db.Integer, primary_key=True)
    news_date = db.Column(db.DateTime, nullable=False)
    news_content = db.Column(db.Text, nullable=False)
    news_title = db.Column(db.String(100), nullable=False)
    news_excerpt = db.Column(db.Text, nullable=False)
    news_status = db.Column(db.String(20), nullable=False)
    news_modified = db.Column(db.DateTime, nullable=False)
    news_category = db.Column(db.Integer, db.ForeignKey('t_newscat.cate_id'), nullable=False)
    news_author = db.Column(db.Integer, db.ForeignKey('t_user.user_id'), nullable=False)
    def __repr__(self):
        return '<News %r>' % self.news_title   


# tags = db.Table('tags',
#     db.Column('tag_id', db.Integer, db.ForeignKey('t_tag.id'), primary_key=True),
#     db.Column('page_id', db.Integer, db.ForeignKey('t_page.id'), primary_key=True)
# )

# class Page(db.Model):
#     __tablename__="t_page"
#     __table_args__ = {"useexisting": True}
#     id = db.Column(db.Integer, primary_key=True)
#     tags = db.relationship('Tag', secondary=tags, lazy='subquery',
#         backref=db.backref('pages', lazy=True))

# class Tag(db.Model):
#     __tablename__="t_tag"
#     __table_args__ = {"useexisting": True}
#     id = db.Column(db.Integer, primary_key=True)    