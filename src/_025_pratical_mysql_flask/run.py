# import configparser
import config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
from sqlalchemy.ext.declarative import declarative_base
import datetime

from app import app

@app.route('/')
def index():
    html = '<h1>Flask RESTful API</h1>'
    html += '<p>获取所有新闻数据[GET]：<br />http://127.0.0.1:5000/newslist</p>'
    html += '<p>添加一条新闻数据[POST]：<br />http://127.0.0.1:5000/news</p>'
    html += '<p>删除一条新闻数据[DELETE]：<br />http://127.0.0.1:5000/news/1</p>'
    html += '<p>修改一条新闻数据[PATCH]：<br />http://127.0.0.1:5000/news/1</p>'
    html += '<p>查询一条新闻数据[GET]：<br />http://127.0.0.1:5000/news/1</p>'
    return html

if __name__ == '__main__':
    # for key, value in app.config.items():
    #     print(str(key)+" "+str(value))
    app.run(debug=True)
    