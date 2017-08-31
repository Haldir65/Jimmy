#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/31 14:56
# @Author  : Aries
# @Site    : 
# @File    : initiate_request.py
# @Software: PyCharm

import requests
import time
from PIL import Image
from io import StringIO

from multiprocessing import Process, Lock


def get_index_response():
    r = requests.get('http://httpbin.org/ip')
    print(r.content)


def print_blocked(i):
    time.sleep(1)
    print('get index %d' % i)


def get_image(url):
    r = requests.get(url)
    # image = Image.open(StringIO(r.content))
    with open('image.jpg','wb+') as f:
        f.write(r.content)
    # print(image.size)
    # image.show()


class MyProcess(Process):
    def __init__(self, loop, lock):
        Process.__init__(self)
        self.loop = loop
        self.lock = lock

    def run(self):
        amount = 1000
        for count in range(self.loop):
            time.sleep(0.1)
            self.lock.acquire()
            print('Pid =' + str(self.pid) + ' LoopCount: ' + str(count))
            amount = amount + 1
            print('global varible is %d' % amount)
            self.lock.release()


def start_multiple_process():
    # count = multiprocessing.cpu_count()
    # for i in range(0, count):
    #     p = multiprocessing.Process(target=print_blocked, args=(i,))
    #     # args是需要给方法传入的参数，是一个tuple
    #     p.start()
    # print('ending--------------')
    amount = 1000
    lock = Lock()
    for i in range(2, 6):
        p = MyProcess(i, lock)
        p.daemon = True
        p.start()
        p.join()

    print("exiting==============")


if __name__ == '__main__':
    get_image('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1504176633747&di=5782b9af086516142abc2cbba925c69b&imgtype=0&src=http%3A%2F%2Fdl.bizhi.sogou.com%2Fimages%2F2012%2F02%2F11%2F185741.jpg')

