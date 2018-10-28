#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 14:02
# @Author  : Aries
# @Site    : 
# @File    : app.py.py
# @Software: PyCharm
import os

import shutil
import zipfile

apkFile = "app-release.apk"
apk = "app-release"

# print apkFile
emptyFile = 'xxx.txt'
f = open(emptyFile, 'w')
f.close()
with open('./channel_list.txt', 'r') as f:
    contens = f.read()
lines = contens.split('\n')
os.mkdir('./release')
#print lines[0]
for line in lines:
    channel = 'channel_' + line
    destfile = './release/%s_%s.apk' % (apk, channel)
    shutil.copy(apkFile, destfile)
    zipped = zipfile.ZipFile(destfile, 'a')
    channelFile = "META-INF/{channelname}".format(channelname=channel)
    zipped.write(emptyFile, channelFile)
    zipped.close()
os.remove('./xxx.txt')

