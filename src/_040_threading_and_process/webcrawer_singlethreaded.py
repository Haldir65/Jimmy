import logging ,time , queue, requests

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s - %(asctime)s  - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def main():
    start = time.time()
    for s in source():
        r = requests.get(s)
        print(r.json())
    print('total time cost %.2f ' % (time.time() - start))


def source():
    return ['http://localhost:15000/api/%d' % x for x in range(100)]

    # return ['https://jsonplaceholder.typicode.com/posts/%d' % x for x in range(10)]


if __name__ == "__main__":
    main()