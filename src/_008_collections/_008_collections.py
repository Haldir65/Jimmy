#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/24 14:43
# @Author  : Aries
# @Site    : 
# @File    : _008_collections.py
# @Software: PyCharm



##Number（数字）  int、float、bool、complex（复数）。
##String（字符串）
##List（列表）
##Tuple（元组）
##Sets（集合）
##Dictionary（字典）

from collections import Iterable


def create_list():
    return ['Charley', 23, 'Bob']


def iterate_item_in_collection(c):
    for index in range(len(c)):
        item = c[index]
        # if isinstance(item, int):
        #     print('it is an int')
        # elif isinstance(item, str):
        #     print('it is an str')
        print(c[index])


def funcs_defination(a, b=10):  # we can have default params
    print(b)
    print(a)
    pass


# funcs_defination(2)


# print("can do \"anything\"", 5) ##  concatenate str and int

# print('this shall be 8', 2 ** 3)  # 计算幂
# x = 6
#
#
# def example():
#     global x
#     print(x)
#     # making stuff global
#     x += 6
#
#
# example()
# print(x)

# x = input('What is your name?: ')
# print('Hello',x)

# def list_demo():
#     students = ['bob','tina','jsoh'] # list的元素可以重复
#     iterate_item_in_collection(students)
#     students.append('tina')  ## pop 必须用index ,remove 必须要用data
#     print('\n')
#     iterate_item_in_collection(students)

def list_inside_a_list():
    l1 = ['bob', True, 'josh', u'zhi']
    l2 = ['rom', l1, 'ins']
    iterate_item_in_collection(l1)
    print('\n')
    iterate_item_in_collection(l2)
    print('\n')
    l2[1][1] = False  ## grab list item inside a list
    iterate_item_in_collection(l2)


# list_inside_a_list()


def tuple_for_demo():
    tuple = ('json', 'dsjk', True)
    iterate_item_in_collection(tuple)


# tuple_for_demo()

def dict_for_demo():
    d = {'name': 'Alice', 'Age': 49}  # dict 无须，类似HashMap,key must be immutable （not a list or container）
    print(d['name'], '\n')
    print(d['Age'])
    print('steve' in d)
    d['raven'] = True
    d.pop('name')
    print(d)


# dict_for_demo()

def set_for_demo():
    # set is just like hashSet ,
    s = {1, 2, 3, 4}  # call remove to remove stuff
    for item in s:
        print(item)


# set_for_demo()

# str . replace create a new str and return , str are immutable

def pow(num, x=2):  # 默认参数
    print(num ** x)


# pow(2,2)

def func_parms(name, age, id=10, price=100):
    print(name, age, id, price)


def make_none(L=None):
    if L is None:
        L = []
    L.append('EOF')
    return L


# func_parms('harris',12,price=20) # we can simply don't respect the order params are passed in , 默认参数创建后就是immutable的了

def isIterable(*args):
    for index, item in enumerate(args):
        if isinstance(item, Iterable):
            print(item, 'is  Iterable')
        else:
            print(item, 'is Not Iterable')


def iteratingDict(d):
    for key, value in d.items():
        print('%s key has the value %s' % (key, value))


tu = ('string', 123, [1, 2, 3], (12, 32))  # tuple装各种元素
dic = {'name': 123, 'age': 456}  # dic迭代不会取value,直接取
# isIterable(*dic)

iteratingDict(dic)
