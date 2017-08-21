#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/11 17:44
# @Author  : Aries
# @Site    : 
# @File    : decode_scripts.py
# @Software: PyCharm Community Edition

s = b'HMS-2.4.0.300/HWHMS-SDK-v2.4.0.300/docs/Getting Started-HMS\xe2\x94\x90\xc2\xac\xe2\x95\x96\xc3\xb3\xe2\x95\x93\xe2\x95\x95\xe2\x95\xa1\xe2\x95\x9d\xe2\x95\xa9\xce\x98.pdf'


fs = ''

for b in s:
    if isinstance(s,bytes):
       print(fs.join(fs,b))
    elif isinstance(s,str):
        print('is Str')
    else:
        print('is not either')

print(fs)