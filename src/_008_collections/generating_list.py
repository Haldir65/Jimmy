#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/30 11:05
# @Author  : Aries
# @Site    : 
# @File    : generating_list.py
# @Software: PyCharm

import os
import time
import logging, coloredlogs

logger = logging.getLogger('Jimmy')

coloredlogs.install(level='INFO')


logger.debug('this is some debug log output')
logger.info('this is some info log output')
logger.warning('this is some warning log output')
logger.error('this is some error log output')
logger.exception('this is some exception log output')

def creating_list(ranges=10):
    L = list(range(0, ranges))
    for index, item in enumerate(L):
        print('%s index is %s value' % (index, item))


# creating_list(20)
# creating_list()


def creating_complex_list(ranges):
    L = [x * x for x in range(0, ranges) if x % 2 == 0]
    for index, data in enumerate(L):
        print('%s index is value is %s' % (index, data))


# creating_complex_list(20)
def create_list_form_os_dir():
    L = [x for x in os.listdir('.')]  ## 当前目录下所有文件
    return L


def iterate_dic():
    d = {'A': 1, 'B': 2, 'C': 3}
    for x, y in d.items():
        print('x is %s y is %s' % (x, y))


# iterate_dic()

def create_generator():
    # generators are simple ,just like list
    G = (x * x for x in range(0, 20))
    for data in G:
        print(data)

    return G


# g = create_generator()
#
#
# while True:
#     try:
#         x = next(g)
#         print('g: ',x)
#     except StopIteration as e:
#         print('end of iteration ',e.value)
#         break


def another_way_of_using_generator(max):
    i = 0
    while i < max:
        i = i + 1
        yield i * i


#
# g = another_way_of_using_generator(20)
# while True:
#     try:
#         print(next(g))
#     except StopIteration as e:
#         print('end now ')
#         break


def manupulating_iter():
    it = iter(range(0, 5))
    while True:
        try:
            time.sleep(1)
            print(next(it))
        except StopIteration as e:
            print('end')
            break


manupulating_iter()
