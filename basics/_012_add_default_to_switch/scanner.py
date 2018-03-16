#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 18:10
# @Author  : Aries
# @Site    : 
# @File    : scanner.py
# @Software: PyCharm
import os


def listAllSrcFile(rootpath, resultlist):
    if os.path.exists(rootpath) and os.path.isdir(rootpath):
        for fileordir in os.listdir(rootpath):
            fileordir = os.path.join(os.path.abspath(os.curdir), fileordir)
            if os.path.exists(fileordir):
                if os.path.isdir(fileordir):
                    listAllSrcFile(fileordir, resultlist)
                else:
                    if os.path.isfile(fileordir) and fileordir.endswith('.java'):
                        resultlist.append(fileordir)
    return resultlist


def scandir(dir):
    for f in os.listdir(dir):
        _f = os.path.join(dir, f)
        if os.path.isdir(_f):
            print(_f)
            scandir(_f)
        else:
            if os.path.isfile(_f):
                print(_f)
    pass


os.chdir(os.pardir)
os.chdir(os.pardir)
print(scandir(os.path.abspath(os.path.curdir)))
