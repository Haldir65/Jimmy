import threading,time, random

FUZZ = True

def fuzz():
    if FUZZ:
        time.sleep(random.random())

counter = 0

def worker():
    global counter
    fuzz()
    oldcnt = counter
    fuzz()
    counter = oldcnt +1
    fuzz()
    print('The count is %d' % counter)
    fuzz()
    print('------------')
    fuzz()


print('Starting up --------\n')
fuzz()

for i in range(10):
    t = threading.Thread(target=worker)
    t.start()
    fuzz()

print('Finishing up')  
fuzz()  