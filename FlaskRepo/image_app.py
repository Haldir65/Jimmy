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
from FlaskRepo.image_utils import calculate_width_and_height
from FlaskRepo.image_utils import create_file_name_from_index
import os
from PIL import Image

# create the flask object
from FlaskRepo.web_utils import getCurrentTimeStr
from FlaskRepo.video_service import serve_video

app = Flask(__name__)


@app.route('/image/<pic_name>', methods=['GET'])
def render_image_template(pic_name):
    file_src = os.path.join(os.path.curdir, 'static/image/' + pic_name)
    file_src = os.path.abspath(file_src)
    width, height = calculate_width_and_height(file_src)
    return render_template('image_template.html', width=width, height=height, src=file_src), 200


@app.route('/image/static/image/<pic_name>', methods=['GET'])
def image_server(pic_name):
    file_src = os.path.join(os.path.curdir, 'static/image/' + pic_name)
    return send_file(file_src, mimetype='image/jpeg')


@app.route('/image/<int:index>', methods=['GET'])
def render_image_template_by_index(index):
    relative_path = 'static/image/' + create_file_name_from_index(index)
    file_src = os.path.join(os.path.curdir, relative_path)
    file_src = os.path.abspath(file_src)
    width, height = calculate_width_and_height(file_src)
    return render_template('image_template.html', width=width, height=height, src=relative_path,name='guest from Hell'), 200

@app.route('/css/common.css',methods=['GET'])
def get_common_css_resource():
    css_file_src = os.path.join(os.path.curdir,'static/css/common.css')
    return send_file(css_file_src,mimetype='text/css')

@app.route('/img/<int:index>', methods=['GET'])
def get_img_by_index_svc(index):
    relative_path = 'static/image/' + create_file_name_from_index(index)
    file_src = os.path.join(os.path.curdir, relative_path)
    file_src = os.path.abspath(file_src)
    return send_file(file_src,mimetype='image/jpeg')


@app.route('/js/<js_name>', methods=['GET'])
def get_js_file(js_name):
    file_src = os.path.join(os.path.curdir, 'static/js/' + js_name)
    print(file_src)
    return send_file(file_src, mimetype='text/javascript')

@app.route('/json/simple',methods=['GET'])
def get_simple_json():
    data = [1, 'foo']
    return json.dumps(data)

@app.errorhandler(404)
def not_found(error):
    return render_template('not_found.html', error=error, width=900, height=1050), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10089, debug=True, threaded=True)
