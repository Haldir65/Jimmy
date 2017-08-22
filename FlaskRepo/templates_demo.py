#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/22 18:27
# @Author  : Aries
# @Site    : 
# @File    : templates_demo.py
# @Software: PyCharm Community Edition

### Sample app for render various templates


from flask import Flask, render_template
from flask import request
from flask import jsonify
from flask import send_file
from flask import Response
from flask import url_for
from flask import abort
from flask import redirect
from flask import make_response

app = Flask(__name__)
bootstrap = Bootstrap(app)


## http://roseou.github.io/2016/05/17/bootstrap/


@app.route('/user/<name>')
def user(name):
    return render_template('user_page.html', user=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10847, debug=True, threaded=True)
