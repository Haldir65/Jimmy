from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request,Blueprint
from sqlalchemy.ext.declarative import declarative_base
import datetime,json,logging
from news.models import User
from db import mydb


auth = Blueprint('auth', __name__)

# @auth.route('/<page>')
# def show(page):
#     try:
#         return render_template('pages/%s.html' % page)
#     except TemplateNotFound:
#         abort(404)

@auth.route('/user/register',methods=['POST'])
def user_register():
    if request.data:
        data = json.loads(request.data)
        user_name = data.get('user_name',None)
        user_password = data.get('user_password',None)
        user_nickname = data.get('user_nickname',None)
        user_email = data.get('user_email',None)
        logging.warn(data)
        if not all(v is not None for v in [user_name, user_password, user_nickname, user_email]):
            return jsonify({"msg":"non valid input","errorcode":403})
        user = User(user_name=user_name,user_password=user_password
        ,user_email=user_email,user_nickname=user_nickname,newses=[])
        try:
            mydb.session.add(user)
            mydb.session.commit()
        except:
            mydb.session.rollback()
            mydb.session.flush()
        user_id = user.user_id
        if user_id is None:
           return jsonify({"msg":"create user error"}) 
        return jsonify({'msg':"user created",'errorCode':0,"data":user.user_id})        
    return "Dummy"


@auth.route('/user/login',methods=['GET','POST'])
def user_login():
    return "Dumb ass"

