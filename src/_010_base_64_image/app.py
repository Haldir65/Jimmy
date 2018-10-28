#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 16:32
# @Author  : Aries
# @Site    : 
# @File    : app.py.py
# @Software: PyCharm
import base64
import PIL.Image
import io
import PIL.Image

def image_to_string():
    with open('./Image_21.jpeg','rb') as file:
        encoded_string = base64.b64decode(file.read())
        with open('result.txt','wb+') as output:
            output.write(encoded_string)
            print('we are done here')
            return encoded_string

def string_to_image(data):

    file_like = io.StringIO(data)
    img = PIL.Image.open(file_like)
    img.show()




if __name__ == '__main__':
    s = image_to_string()
    s = str(s,'utf-8')
    string_to_image(s)
