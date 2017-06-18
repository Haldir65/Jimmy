#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/18 18:34
# @Author  : Aries
# @Site    : 
# @File    : video_service.py
# @Software: PyCharm Community Edition

import json

import os

from flask import Flask
from flask import request
from flask import jsonify
from flask import send_file
from flask import Response
from flask import url_for

app = Flask(__name__)


@app.route('/', methods=['GET'])
def serve_video(video_id):
    print(video_id)
    filename = 'static/video/李志&quot;看见&quot;2015巡演预告片.mp4'
    fullpath = os.path.join(os.path.curdir, filename)
    return send_file(fullpath, mimetype='video/mp4')
