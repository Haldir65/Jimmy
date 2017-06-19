#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/19 17:43
# @Author  : Aries
# @Site    : 
# @File    : gunicorndemo.py
# @Software: PyCharm Community Edition

from flask import Flask
from flask import render_template_string
import os
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)


@app.route('/')
def index():
    return "worked!"


app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    app.run()
