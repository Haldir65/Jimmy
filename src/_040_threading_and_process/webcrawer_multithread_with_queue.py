
## use a message queue for pringting the result 
## spwan 10 threads for io operation, each will then deliver response from remote server to the queue upon completion
## bear in mind , we still have the gil.  
## attention, race condition among different threads for resources
## the logging module have lock inside

import logging ,time , queue, requests
from threading import Thread

# create logger

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s - %(asctime)s  - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
 
q = queue.Queue()


def do_work(task,  result, index):
    logger.info("doing tasks %s" % task)
    try:
        r = requests.get(task)
        j = r.text
        result[index] = j
    except Exception as e:
        logger.error(e)
        result[index] = {}


def worker():
    if q.empty():
        logger.info('is empty')
    else:
        logger.info('not empty')
    while not q.empty():
        item = q.get()
        logger.debug("before puting tasks %s into queue" % item[0] )
        url  = item[0]
        resultlist = item[1]
        index = item[2]
        do_work(url, resultlist, index)
        q.task_done()

def source():
    return ['http://localhost:15000/api/%d' % x for x in range(50)]
    # return ['https://jsonplaceholder.typicode.com/posts/%d' % x for x in range(10)]

def main():
    logger.info('This is a log info')
    logger.debug('Debugging')
    logger.warning('Warning exists')
    logger.info('Finish')
    start = time.time()

    s = source()
    results = [{} for x in s]
    tasks = [(x, results,ind) for ind, x in enumerate(s)]
    num_worker_threads = min(50,len(tasks))

    for item in tasks:
        q.put(item)

    threads = []
    for i in range(num_worker_threads):
        t = Thread(target=worker)
        # t.daemon = True
         #setting threads as "daemon" allows main program to 
          #exit eventually even if these dont finish 
       #correctly.
        t.start()    

    q.join()       # block until all tasks are done

    for res in results:
        print(res)
    print('total time cost %.2f ' % (time.time() - start))

if __name__ == "__main__":
    main()