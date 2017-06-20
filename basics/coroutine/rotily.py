#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/20 11:44
# @Author  : Aries
# @Site    : 
# @File    : rotily.py
# @Software: PyCharm Community Edition


import os


# http://aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html



def create_a_generator():
    g = (x for x in range(1, 10))
    return g


def print_each_element_in_a_list(l):
    for i in l:
        print(i)


g = create_a_generator()
print_each_element_in_a_list(g)


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)
