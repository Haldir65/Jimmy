# import configparser
import config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

# my_config = configparser.ConfigParser()
# my_config.read('db.conf')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + 
# config.get('DB_USER', None) + ':' 
# + config.get('DB_PASSWORD', None) 
# + '@' + config.get('DB_HOST', None) 
# + '/' + config.get('DB_DB', None)
app.config.from_object('config')

mydb = SQLAlchemy()
mydb.init_app(app)

# 一对多关系，一个分类下有多条新闻记录
class Newscate(mydb.Model):
    cate_id = mydb.Column(mydb.Integer, primary_key=True)
    cate_name = mydb.Column(mydb.String(50), nullable=False)
    cate_title = mydb.Column(mydb.String(50), nullable=False)
    newses = mydb.relationship('News', backref='newscate', lazy=True)
    def __repr__(self):
        return '<Newscate %r>' % self.cate_name

# 一对多关系，一个编辑人下有多条新闻记录
class User(mydb.Model):
    user_id = mydb.Column(mydb.Integer, primary_key=True)
    user_name = mydb.Column(mydb.String(60), nullable=False)
    user_password = mydb.Column(mydb.String(30), nullable=False)
    user_nickname = mydb.Column(mydb.String(50), nullable=False)
    user_email = mydb.Column(mydb.String(100), nullable=False)
    newses = mydb.relationship('News', backref='user', lazy=True)
    def __repr__(self):
        return '<User %r>' % self.user_nickname

class News(mydb.Model):
    news_id = mydb.Column(mydb.Integer, primary_key=True)
    news_date = mydb.Column(mydb.DateTime, nullable=False)
    news_content = mydb.Column(mydb.Text, nullable=False)
    news_title = mydb.Column(mydb.String(100), nullable=False)
    news_excerpt = mydb.Column(mydb.Text, nullable=False)
    news_status = mydb.Column(mydb.String(20), nullable=False)
    news_modified = mydb.Column(mydb.DateTime, nullable=False)
    news_category = mydb.Column(mydb.Integer, mydb.ForeignKey('newscate.cate_id'), nullable=False)
    news_author = mydb.Column(mydb.Integer, mydb.ForeignKey('user.user_id'), nullable=False)
    def __repr__(self):
        return '<News %r>' % self.news_title

@app.route('/')
def index():
    html = '<h1>Flask RESTful API</h1>'
    html += '<p>获取所有新闻数据[GET]：<br />http://127.0.0.1:5000/newslist</p>'
    html += '<p>添加一条新闻数据[POST]：<br />http://127.0.0.1:5000/news</p>'
    html += '<p>删除一条新闻数据[DELETE]：<br />http://127.0.0.1:5000/news/1</p>'
    html += '<p>修改一条新闻数据[PATCH]：<br />http://127.0.0.1:5000/news/1</p>'
    html += '<p>查询一条新闻数据[GET]：<br />http://127.0.0.1:5000/news/1</p>'
    return html

# 添加数据
@app.route('/news', methods=['POST'])
def addNews():
    news_author = request.form.get('news_author')
    news_date = request.form.get('news_date')
    news_content = request.form.get('news_content')
    news_title = request.form.get('news_title')
    news_excerpt = request.form.get('news_excerpt')
    news_category = request.form.get('news_category')
    news_status = request.form.get('news_status')
    news_modified = request.form.get('news_modified')
    news = News(news_author=news_author, news_date=news_date, news_content=news_content, news_title=news_title, news_excerpt=news_excerpt, news_category=news_category, news_status=news_status, news_modified=news_modified)
    try:
        mydb.session.add(news)
        mydb.session.commit()
    except:
        mydb.session.rollback()
        mydb.session.flush()
    newsId = news.news_id
    if (newsId is None):
        result = {'msg': '添加失败'}
        return jsonify(data=result)

    # 查询最新插入的数据
    data = mydb.session.query(News.news_id, News.news_author, News.news_date, News.news_title, News.news_content, News.news_excerpt, News.news_status, News.news_modified, Newscate.cate_name, Newscate.cate_title, User.user_name, User.user_nickname).filter_by(news_id=newsId).join(Newscate, News.news_category == Newscate.cate_id).join(User, News.news_author == User.user_id).first()
    result = {'news_id': data.news_id, 'news_author': data.news_author, 'news_author_name': data.user_name,
              'news_author_nickname': data.user_nickname, 'news_date': data.news_date, 'news_title': data.news_title,
              'news_content': data.news_content, 'news_excerpt': data.news_excerpt, 'news_status': data.news_status,
              'news_modified': data.news_modified, 'news_cate_name': data.cate_name, 'news_cate_title': data.cate_title}
    return jsonify(data=result)

# 删除数据
@app.route('/news/<int:newsId>', methods=['DELETE'])
def deleteNews(newsId):
    News.query.filter_by(news_id=newsId).delete()
    mydb.session.commit()
    return getNewslist()

# 修改数据
@app.route('/news/<int:newsId>', methods=['PATCH'])
def updateNews(newsId):
    # 获取请求的数据
    news_author = request.form.get('news_author')
    news_date = request.form.get('news_date')
    news_content = request.form.get('news_content')
    news_title = request.form.get('news_title')
    news_excerpt = request.form.get('news_excerpt')
    news_category = request.form.get('news_category')
    news_status = request.form.get('news_status')
    news_modified = request.form.get('news_modified')
    try:
        news = News.query.filter_by(news_id=newsId).first()
        if (news is None):
            result = {'msg': '找不到要修改的记录'}
            return jsonify(data=result)
        else:
            news.news_author = news_author
            news.news_date = news_date
            news.news_content = news_content
            news.news_title = news_title
            news.news_excerpt = news_excerpt
            news.news_category = news_category
            news.news_status = news_status
            news.news_modified = news_modified
            mydb.session.commit()
    except:
        mydb.session.rollback()
        mydb.session.flush()
    # 获取修改的数据ID
    newsId = news.news_id
    # 查询修改的数据
    data = mydb.session.query(News.news_id, News.news_author, News.news_date, News.news_title, News.news_content, News.news_excerpt, News.news_status, News.news_modified, Newscate.cate_name, Newscate.cate_title, User.user_name, User.user_nickname).filter_by(news_id=newsId).join(Newscate, News.news_category == Newscate.cate_id).join(User, News.news_author == User.user_id).first()
    result = {'news_id': data.news_id, 'news_author': data.news_author, 'news_author_name': data.user_name,
              'news_author_nickname': data.user_nickname, 'news_date': data.news_date, 'news_title': data.news_title,
              'news_content': data.news_content, 'news_excerpt': data.news_excerpt, 'news_status': data.news_status,
              'news_modified': data.news_modified, 'news_cate_name': data.cate_name, 'news_cate_title': data.cate_title}
    return jsonify(data=result)

# 查询单条数据
@app.route('/news/<int:newsId>', methods=['GET'])
def getNews(newsId):
    news = mydb.session.query(News.news_id, News.news_author, News.news_date, News.news_title, News.news_content, News.news_excerpt, News.news_status, News.news_modified, Newscate.cate_name, Newscate.cate_title, User.user_name, User.user_nickname).filter_by(news_id=newsId).join(Newscate, News.news_category == Newscate.cate_id).join(User, News.news_author == User.user_id).first()
    if (news is None):
        result = {'msg': '找不到数据'}
    else:
        result = {'news_id': news.news_id, 'news_author': news.news_author, 'news_author_name': news.user_name, 'news_author_nickname': news.user_nickname, 'news_date': news.news_date, 'news_title': news.news_title, 'news_content': news.news_content, 'news_excerpt': news.news_excerpt, 'news_status': news.news_status, 'news_modified': news.news_modified, 'news_cate_name': news.cate_name, 'news_cate_title': news.cate_title}
    return jsonify(data=result)

# 查询所有数据
@app.route('/newslist', methods=['GET'])
def getNewslist():
    data = mydb.session.query(News.news_id, News.news_author, News.news_date, News.news_title, News.news_content, News.news_excerpt, News.news_status, News.news_modified, Newscate.cate_name, Newscate.cate_title, User.user_name, User.user_nickname).join(Newscate, News.news_category  == Newscate.cate_id).join(User, News.news_author == User.user_id)
    data_all = []
    for news in data:
        data_all.append({'news_id': news.news_id, 'news_author': news.news_author, 'news_author_name': news.user_name, 'news_author_nickname': news.user_nickname, 'news_date': news.news_date, 'news_title': news.news_title, 'news_content': news.news_content, 'news_excerpt': news.news_excerpt, 'news_status': news.news_status, 'news_modified': news.news_modified, 'news_cate_name': news.cate_name, 'news_cate_title': news.cate_title})
    return jsonify(data=data_all)

if __name__ == '__main__':
    for key, value in app.config.items():
        print(str(key)+" "+str(value))
    app.run(debug=True)
    