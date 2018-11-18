#!/usr/bin/env python3

import threading
import time

origin = "this is awesome"

def testThread(num):
    global origin
    time.sleep(1)
    print("thread {0} saw the origin as {1}  ".format(num,origin))
    print("hey there")
if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=testThread, args=(i,))
        t.start()
        t.join()

