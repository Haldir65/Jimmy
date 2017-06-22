#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/22 17:06
# @Author  : Aries
# @Site    : 
# @File    : example_unicode_error.py
# @Software: PyCharm Community Edition

# bytes >> unicode >> utf-8


# str are represented as unicode

b = "this is english within ascii".encode('ascii')
# s = "你好".encode('ascii') # this will raise an error ,UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

# binary = (b"你好啊").decode('utf-8')
string = "你好啊"
bstring = b'\xe4\xbd\xa0\xe5\xa5\xbd\xe5\x95\x8a'
bstring2string = bstring.decode('utf-8')
i = 3


def which_instance_is_this(o):
    if isinstance(o, bytes):
        return ('is byte ')
    elif isinstance(o, str):
        return ('is str')
    elif isinstance(o, int):
        return ('is integer')
    elif isinstance(o, float):
        return ('is float')


if __name__ == '__main__':
    # print(which_instance_is_this(b))
    # print((b"totally cool binary representation of english words within ascii range").decode('ascii'))
    # print((b"totally cool binary cause utf-8 include ascii").decode('utf-8'))
    print(chr(20320))
    print(ord('你'))
