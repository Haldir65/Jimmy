#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/30 13:14
# @Author  : Aries
# @Site    : 
# @File    : imagerequestplay.py
# @Software: PyCharm

import requests
import time


def get_image(url):
    headers = {'Referer': 'http://www.xiaohongchun.com.cn/classify/detail/317340946','User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'}
    r = requests.get(url, headers=headers)
    # image = Image.open(StringIO(r.content))
    with open('image2.gif','wb+') as f:
        f.write(r.content)

if __name__ == '__main__':
    get_image("http://wicdn.xiaohongchun.com/g_images/518245-da5b65a5c7498b5e12dad03b277c3360.gif")
    # get_image("http://wicdn.xiaohongchun.com/g_images/518245-4c7c0a5797b0a798a772146210c91234.gif")
