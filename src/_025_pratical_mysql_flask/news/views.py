
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request,Blueprint
from sqlalchemy.ext.declarative import declarative_base
import datetime,json
import logging


bluprint = Blueprint('news', __name__)

from db import mydb
from .models import News,Newscate,User


# 添加数据
@bluprint.route('/news', methods=['POST'])
def addNews():
    if request.data:
        data = json.loads(request.data)
        news_author = data.get('news_author',None)
        news_date = data.get('news_date',datetime.datetime.utcnow())
        news_content = data.get('news_content',None)
        news_title = data.get('news_title',None)
        news_excerpt = data.get('news_excerpt',None)
        news_category = data.get('news_category',None)
        news_status = data.get('news_status',None)
        news_modified = data.get('news_modified',datetime.datetime.utcnow())
        news = News(news_author=news_author, news_date=news_date, news_content=news_content, news_title=news_title, news_excerpt=news_excerpt, news_category=news_category, news_status=news_status, news_modified=news_modified)
        try:
            print(news)
            mydb.session.add(news)
            mydb.session.commit()
        except Exception as e:
            print('大事不好了')
            mydb.session.rollback()
            mydb.session.flush()
        newsId = news.news_id    
        if (newsId is None):
            result = {'msg': '添加失败'}
            return jsonify(data=result)

        # 查询最新插入的数据
        print(newsId)
        data = mydb.session.query(News.news_id, News.news_author, News.news_date, News.news_title, News.news_content, News.news_excerpt,
         News.news_status, News.news_modified, Newscate.cate_name,
          Newscate.cate_title, User.user_name, User.user_nickname).filter_by(news_id=newsId).join(Newscate, News.news_category == Newscate.cate_id).join(User, News.news_author == User.user_id).first()
        if(data):
            result = {'news_id': data.news_id, 'news_author': data.news_author, 'news_author_name': data.user_name,
                    'news_author_nickname': data.user_nickname, 'news_date': data.news_date, 'news_title': data.news_title,
                    'news_content': data.news_content, 'news_excerpt': data.news_excerpt, 'news_status': data.news_status,
                    'news_modified': data.news_modified, 'news_cate_name': data.cate_name, 'news_cate_title': data.cate_title}
            return jsonify(data=result)
        else:
            return "no match record "            

# 删除数据
@bluprint.route('/news/<int:newsId>', methods=['DELETE'])
def deleteNews(newsId):
    News.query.filter_by(news_id=newsId).delete()
    mydb.session.commit()
    return getNewslist()

# 修改数据
@bluprint.route('/news/<int:newsId>', methods=['PATCH'])
def updateNews(newsId):
    # 获取请求的数据
    news_author = data.get('news_author')
    news_date = data.get('news_date')
    news_content = data.get('news_content')
    news_title = data.get('news_title')
    news_excerpt = data.get('news_excerpt')
    news_category = data.get('news_category')
    news_status = data.get('news_status')
    news_modified = data.get('news_modified')
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
@bluprint.route('/news/<int:newsId>', methods=['GET'])
def getNews(newsId):
    news = mydb.session.query(News.news_id, News.news_author, News.news_date, News.news_title, News.news_content, News.news_excerpt, News.news_status, News.news_modified, Newscate.cate_name, Newscate.cate_title, User.user_name, User.user_nickname).filter_by(news_id=newsId).join(Newscate, News.news_category == Newscate.cate_id).join(User, News.news_author == User.user_id).first()
    if (news is None):
        result = {'msg': '找不到数据'}
    else:
        result = {'news_id': news.news_id, 'news_author': news.news_author, 'news_author_name': news.user_name, 'news_author_nickname': news.user_nickname, 'news_date': news.news_date, 'news_title': news.news_title, 'news_content': news.news_content, 'news_excerpt': news.news_excerpt, 'news_status': news.news_status, 'news_modified': news.news_modified, 'news_cate_name': news.cate_name, 'news_cate_title': news.cate_title}
    return jsonify(data=result)

# 查询所有数据
@bluprint.route('/newslist', methods=['GET'])
def getNewslist():
    data = mydb.session.query(News.news_id, News.news_author, News.news_date, News.news_title, News.news_content, News.news_excerpt, News.news_status, News.news_modified, Newscate.cate_name, Newscate.cate_title, User.user_name, User.user_nickname).join(Newscate, News.news_category  == Newscate.cate_id).join(User, News.news_author == User.user_id)
    data_all = []
    for news in data:
        data_all.append({'news_id': news.news_id, 'news_author': news.news_author, 'news_author_name': news.user_name, 'news_author_nickname': news.user_nickname, 'news_date': news.news_date, 'news_title': news.news_title, 'news_content': news.news_content, 'news_excerpt': news.news_excerpt, 'news_status': news.news_status, 'news_modified': news.news_modified, 'news_cate_name': news.cate_name, 'news_cate_title': news.cate_title})
    return jsonify(data=data_all)