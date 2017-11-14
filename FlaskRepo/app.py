#!/usr/bin/python3
# -*- coding:utf8 -*-

import json

from flask import Flask
from flask import request
from flask import jsonify
from flask import send_file
from flask import Response
from flask import url_for
from flask import abort
from flask import redirect
from flask import render_template
from flask import make_response
# from flask_httpauth import HTTPBasicAuth
# pip install Flask-HTTPAuth

import os

# create the flask object
# from FlaskRepo.web_utils import getCurrentTimeStr
# from FlaskRepo.video_service import serve_video

app = Flask(__name__)


# auth = HTTPBasicAuth()


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


@app.route("/posts", methods=['GET'])
def get_post_list(count=10):
    post = {'id': 1, 'title': 'Dummy title',
            'body': '昨天小米发布了小米MIX 2和小米Note 3，的确被惊艳到了，所以我决定今晚等iPhone X（据说这是下一代iPhone刚确认的名称）发布。'}
    post_lists = [post, post]
    for x in range(0, count):
        if (x % 2) == 0:
            new_post = create_post(x,'dummy even title','饿了么刚刚如愿将百度外卖收入囊中，旋即遭遇不小的整合阻力。9月11日，北京商报记者获悉百度外卖CTO（首席技术官）耿艳坤已于9月8日离职，并且业内盛传耿艳坤的新东家正是百度外卖在牵手饿了么之前的“绯闻对象”——顺丰。事实上，不少业内分析人士都曾指出，两家平台在整合的过程中难以避免出现大范围的人事变动，'
                                                        '但是对于技术见长的百度外卖而言，此次技术一把手的离开，恐在一定程度上削弱其竞争优势，这对于饿了么而言更是不小的损失。')
        else:
            new_post = create_post(x,'some odd title','近日，澳大利亚的一则羊肉电视广告遭到了该国印度教群体的强烈抗议。该广告发布于9月4日，使用了多个宗教神祗形象以表达羊肉是可以被所有宗教信仰的人所食用的观念。里边出现的象头神迦尼萨激发了印度教徒不满，原因是在该宗教文化描述中，象头神从来不吃肉。BBC报道，澳洲印度教团体已向政府提出外交抗议，要求撤下该广告，并为伤害了他们的感情和嘲笑印度文化而道歉。据悉，这则广告已遭到30多起涉及“宗教信仰”的投诉')
        post_lists.append(new_post)
    resp = Response(json.dumps(post_lists), mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    resp.headers['mimetype'] = 'application/json'
    return resp


def create_post(id= -1,title = 'unknwn',body='stuff'):
    return {'id':id,'title':title,'body':body,'extra':'some extra stuff'}


def redirect_to_url(url):
    return redirect('https://www.baidu.com')  # note ! 302 status code


@app.route('/_get_user_list', methods=['GET'])
def get_user_list():
    user_list = create_user_list()
    resp = Response(json.dumps(user_list))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['mimetype'] = 'application/json'
    return resp


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
    if os.path.exists(fullpath):
        print(' it exists')
    if os.path.exists(filename):
        print('filename exists')
    return send_file(filename, mimetype='image/jpeg')


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


@app.route('/_get_video/<_video_id>', methods=['GET'])
def get_video(_video_id):
    print(_video_id)
    filename = 'static/video/Keynote%3A An Android Retrospective (en) - Romain Guy, Chet Haase, Google.MP4'
    return send_file(filename, mimetype='video/mp4')


def file_downloads():
    return


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False,
        'time': 0

    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False,
        'time': 0
    }
]


# @app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
# def getTaskById(task_id):
#     task = filter(lambda t: t['id'] == task_id, tasks)
#     if not task.__next__:
#         abort(404)
#     return jsonify({'task', task[0]})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return jsonify({'task': task})
    abort(404)
    # task = filter(lambda t: t['id'] == task_id, tasks)
    # # if len(task) == 0:
    # #     abort(404)
    # return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
# @auth.login_required
def get_tasks():
    list = []
    for i in tasks:
        list.append(make_public_task(i))
    return jsonify({'tasks': list})


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json['task']:
        abort(404)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['task']['title'],
        'description': request.json['task'].get('description', ''),
        'done': False,
        'time': 's'
    }
    tasks.append(task)
    for i in tasks:
        print(i['time'])
    return jsonify({'task': task}), 201


def make_public_task(task):
    new_task = {}
    print('make_url')
    for field in task:
        if field == 'id':
            new_task['url'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
            print(field)
    if len(new_task) == 0:
        abort(404)
    else:
        return new_task


# @auth.get_password
def get_password(user_name):
    if user_name == 'mike':
        return 'python_guy'
    return None


# @auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Not Found'}), 404)


@app.errorhandler(404)
def not_found(error):
    return render_template('not_found.html', error=error, width=900, height=1050), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10877, debug=True, threaded=True)
