#!/usr/bin/python3
# -*- coding:utf8 -*-
from PIL import Image
import os


def calculate_width_and_height(abs_path):
    im = Image.open(abs_path)
    return im.size
    # im.size  # (width,height) tuple

# 返回带.jpg的文件名称
def create_file_name_from_index(index):
    path = os.path.abspath(os.path.join(os.path.curdir, 'static/image'))
    ll = os.listdir(path)
    if index>=len(ll):
        index = 1
    elif index<=0:
        index = 1
    return ll[index]
