#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import time


#  Decoration is more like adding interceptors for functions
# you may use any words , but for convention ,wrapper or _decorator is better
def log(func):
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        func(*args, **kwargs)
        print('existing %s():' % func.__name__)
        # return func(*args, **kwargs)

    return wrapper


def debug(func):
    def wrapper(*args, **kwargs):
        for item in args:
            print('get item %s' % item)
        print('end displaying args')
        # print("start func %s(): " % func.__name__ + ' args= ' + args[0] + str(kwargs.__sizeof__()))
        func(*args, **kwargs)
        print("end func %s(): " % func.__name__)

    return wrapper


# a log with level
def log_level(level):
    def log(func):
        def _decorator(*args, **kagrs):
            print('func name is %s' % func.__name__ + 'arguments input is %s' % args[0])
            print('current log level is %d' % level)
            func(*args)  # the function can even be omitted
            print('end function')

        return _decorator

    return log


@debug
def current_time():
    print(time.ctime())


@log_level(level=5)
def func_with_args(name, price):
    print('name %s' % name + ' and price is %d' % price)


def plain_msg(status_code):
    msg = 'success' if status_code == 200  else 'fail'
    return msg


# cache user

dictcache = {}


def cache(func):
    def __decorator(user):  # user is ifered as str
        now = time.time()
        if (user in dictcache):
            result, cache_time = dictcache[user]
            if (now - cache_time) > 30:  # cache expired
                result = func(user)
                dictcache[user] = (result, now)  # cache the result by user
            else:
                print('cache hits')
        else:
            result = func(user)
            dictcache[user] = (result, now)
        return result

    return __decorator


def login(user):
    print('in login:' + user)
    msg = validate(user)
    return msg


@cache  # apply the cache for this slow validation
def validate(user):
    time.sleep(5)  # simulate 10 second block
    msg = "success" if user == "jatsz" else "fail"
    return msg


def lengthy_task():
    result1 = login('jatsz')
    print(result1)

    result2 = login('jatsz')
    print(result2)  # this login will return immediately by hit the cache
    result3 = login('candy')
    print(result3)


# current_time()
# func_with_args('dollar', 100)


if __name__ == '__main__':
    lengthy_task()
