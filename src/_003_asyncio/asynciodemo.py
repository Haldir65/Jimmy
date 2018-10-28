#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/22 10:23
# @Author  : Aries
# @Site    : 
# @File    : asynciodemo.py
# @Software: PyCharm Community Edition

import asyncio


@asyncio.coroutine
def hello():
    print('hey there!')

    r = yield from asyncio.sleep(1)

    print(" hello again!")


loop = asyncio.get_event_loop()

loop.run_until_complete(hello())
loop.close()
