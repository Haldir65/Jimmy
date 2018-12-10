#!/usr/bin/env python3

import socket,time,logging
from selectors import DefaultSelector,EVENT_READ,EVENT_WRITE
logging.getLogger().setLevel(logging.INFO)

selector = DefaultSelector()

n_tasks = 0
PORT = 15000

def get(path):
    global n_tasks
    n_tasks+=1
    s = socket.socket()
    s.setblocking(False)
    try:
        s.connect(('localhost', PORT))
    except BlockingIOError:
        pass
    request = 'GET %s HTTP/1.1\r\n\r\n' % path

    callback = lambda: connected(s,request)
    selector.register(s.fileno(),EVENT_WRITE, data= callback)

def connected(s,request):
    selector.unregister(s.fileno())
    try:
        s.send(request.encode())
    except BrokenPipeError:
        pass
    chunks = []
    callback = lambda: readable(s, chunks)
    selector.register(s.fileno(),EVENT_READ,data=callback)


def readable(s, chunks):
    # s is readable!
    global n_tasks
    selector.unregister(s.fileno())
    chunk = s.recv(1000)
    if chunk:
        chunks.append(chunk)
        if(len(chunk) < 1000):
            body = (b''.join(chunks)).decode()
            print(body.split('\n')[0])
            n_tasks -= 1
            ## in reality , you might want to check the content-length field from the response header
            return
        else:
            callback = lambda: readable(s,chunks)
            selector.register(s.fileno(),EVENT_READ, data= callback)

    else:
        body = (b''.join(chunks)).decode()
        print(body.split('\n')[0])
        n_tasks -= 1
        return
            


def main():
    start = time.time()
    action = lambda : get('/')
    for i in range(0,10):
        action()
    while n_tasks:
        events = selector.select()
        for event, mask in events:
            cb = event.data
            cb()

    print('took %.1f second ' % (time.time() - start))

if __name__ == "__main__":
    main()