#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/23 13:26
# @Author  : Aries
# @Site    : 
# @File    : get_you.py
# @Software: PyCharm Community Edition

import os
import sys
import subprocess


# sys.argv=['you-get','-h']
# you_get.main()


def read_file():
    src = 'result.txt'
    with open(src, "r") as f:
        contents = f.readlines()
    contents = [x.strip() for x in contents]
    for line in contents:
        # print(line)
        if get_available_space_on_disk() > 50:
            break
        try:
            print('start down_load ' + line)
            subprocess.call('you-get ' + line, shell=True)
            # 使用subprocess模块可以创建新的进程，可以与新建进程的输入/输出/错误管道连通，并可以获得新建进程执行的返回状态。
            # 使用subprocess模块的目的是替代os.system()、os.popen*()、commands.*等旧的函数或模块
            # os.system() 太慢了
            print('finish download ' + line)
        except Exception as e:
            print('error on url ' + line)
            pass


# 获取磁盘剩余空间所占百分比
def get_available_space_on_disk():
    disk = os.statvfs('/')
    percent = (disk.f_blocks - disk.f_bfree) * 100 / (disk.f_blocks - disk.f_bfree + disk.f_bavail)
    print('available disk percentage ' + str(percent))
    return percent


# read_file()

# get_available_space_on_disk()
read_file()
