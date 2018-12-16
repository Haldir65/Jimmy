#!/usr/bin/env python3

import socket
import time
import logging
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
logging.getLogger().setLevel(logging.INFO)

selector = DefaultSelector()

n_tasks = 0
PORT = 15000


class Future:
    def __init__(self):
        self.callbacks = []

    def resolve(self):
        for c in self.callbacks:
            c()


class Task:
    def __init__(self, gen):
        self.gen = gen
        self.step()

    def step(self):
        try:
            f = next(self.gen)
        except StopIteration as identifier:
            return
        f.callbacks.append(self.step)


def get(path):
    global n_tasks
    n_tasks += 1
    s = socket.socket()
    s.setblocking(False)
    try:
        s.connect(('localhost', PORT))
    except BlockingIOError:
        pass
    request = 'GET %s HTTP/1.1\r\n\r\n' % path

    f = Future()
    selector.register(s.fileno(), EVENT_WRITE, data=f)

    # pause until writable
    yield f
    selector.unregister(s.fileno())
    ## s is writable
    s.send(request.encode())
    chunks = []

    while True:
        f = Future()
        selector.register(s.fileno(), EVENT_READ, data=f)
        yield f
        # s is readable!
        selector.unregister(s.fileno())
        chunk = s.recv(1000)
        if chunk:
            chunks.append(chunk)
            if(len(chunk) < 1000):
                body = (b''.join(chunks)).decode()
                print(body.split('\n')[0])
                n_tasks -= 1
                # in reality , you might want to check the content-length field from the response header
                return
            else:
                f = Future()
                selector.register(s.fileno(), EVENT_READ, data=f)
                yield f

        else:
            body = (b''.join(chunks)).decode()
            print(body.split('\n')[0])
            n_tasks -= 1
            return


def main():
    start = time.time()
    # return a generator
    # action = lambda : get('/')
    [Task(get('/')) for x in range(10)] ## plain list comprehension
    # for i in range(0, 10):
    #     Task(get('/'))
    while n_tasks:
        events = selector.select()
        for event, mask in events:
            fut = event.data
            fut.resolve()

    print('took %.1f second ' % (time.time() - start))


if __name__ == "__main__":
    main()
