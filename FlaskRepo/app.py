#!/usr/bin/python3
# -*- coding:utf8 -*-

import json

from flask import Flask
from flask import request
from flask import jsonify
from flask import send_file
from flask import Response
from flask import url_for
from flask import redirect
from flask import render_template


from video_service import serve_video

import os

# create the flask object
app = Flask(__name__)


#
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return '<h1>Home</h1>'
#
#
# # simple html form , don't bother
# @app.route('/signin', methods=['GET'])
# def signin_form():
#     return '''<form action="/signin" method="post">
#               <p><input name="username"></p>
#               <p><input name="password" type="password"></p>
#               <p><button type="submit">Sign In</button></p>
#               </form>'''
#
#
# @app.route('/signin', methods=['POST'])
# def sign_in():
#     if request.form['username'] == 'admin' and request.form['password'] == 'password':
#         return '<h3>Hello,admin</h3>'
#     return '<h3>Invalid user account</h3>'


@app.route('/', methods=['POST'])
def handle_post():
    uid = request.form['uid']
    name = request.form['name']
    print('uid is %s ,name is %s ' % (uid, name))
    return '200 OK'


@app.route('/', methods=['GET'])
def handle_get():
    return 'haha ,this is http status code 200'


@app.route('/res', methods=['GET'])
def handle_get_res():
    return 'you find a new resourse'


@app.route('/_get_current_user', methods=['GET'])
def get_current_user():
    return jsonify(
        username='Admin',
        email='Harris@gmail.com',
        age=18
    )


@app.route('/_get_user_list', methods=['GET'])
def get_user_list():
    user_list = create_user_list()
    return Response(json.dumps(user_list), mimetype='application/json')


def create_user_list():
    alice = {'name': 'alice', 'age': 16, 'sex': 'female'}
    tom = {'name': 'tom', 'age': 23, 'sex': 'male'}
    josh = {'name': 'josh', 'age': 20, 'sex': 'male'}
    bill = {'name': 'bill', 'age': 19, 'sex': 'male'}
    li = [alice, tom, josh, bill]
    return li


@app.route('/_single_product', methods=['GET'])
def get_single_product():
    return jsonify(
        name='Coffee',
        id=17990,
        price=20,
        image_url="/image_xxxxx"
    )


@app.route('/_get_image', methods=['GET'])
def get_image():
    filename = 'static/image/b1.jpg'
    fullpath = os.path.join(os.path.curdir, filename)
    print(filename, fullpath)
    return send_file(fullpath, mimetype='image/jpeg')


@app.route('/_get_user/<user_id>', methods=['GET'])
def get_user_detail(user_id):
    print(url_for('static', filename='user_id'))
    return jsonify(
        name='John',
        id=user_id,
        avatar="/_image/xx",
        age=10,
        extra=[1, 2, 'f', 20]
    )


@app.route('/_get_user_list', methods=['POST'])
def post_user():
    error = None
    if request.form['username'] == 12345:
        print('Validation OK')
    else:
        pass
    return jsonify(
        name='Duck',
        id=12,
        avatar="/_image/xx",
        age=10,
        extra=[1, 2, 'f', 20]
    )


@app.route('/_search_user', methods=['GET'])
def query_user_profile():
    user = request.args.get('user')
    date = request.args.get('date')
    print(user)
    print(date)
    return 'every Thing Ok'


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',error=error),404


@app.route('/_get_video/<_video_id>', methods=['GET'])
def get_video(_video_id):
    print(_video_id)
    filename = 'static/video/porn.MP4'
    return send_file(filename, mimetype='video/mp4')


def file_downloads():
    return




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10899, debug=True)
