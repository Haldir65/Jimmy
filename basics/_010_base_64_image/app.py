#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 16:32
# @Author  : Aries
# @Site    : 
# @File    : app.py.py
# @Software: PyCharm
import base64
import PIL.Image

def image_to_string():
    with open('./Image_21.jpeg','rb') as file:
        encoded_string = base64.b64decode(file.read())
        with open('result.txt','wb+') as output:
            output.write(encoded_string)
            print('we are done here')




if __name__ == '__main__':
    image_to_string()
