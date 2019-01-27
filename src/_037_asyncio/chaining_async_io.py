import random,json
import asyncio
import requests
import json
import logging
import brotli

## https://jsonplaceholder.typicode.com/posts
## https://jsonplaceholder.typicode.com/comments?postId=1

loop = asyncio.get_event_loop()

reponse_num = 0
request_num = 0
headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'referer': 'https://jsonplaceholder.typicode.com/',
    'accept-encoding':'gzip, deflate, br'}

def requet_wrapper(url,timeout=5):
    res = None
    try:
        res = requests.get(url, timeout=5, headers= headers)
    except requests.exceptions.Timeout as e1:
        print(e1)
    except requests.exceptions.ConnectionError as e2:
        print(e2) 
    return res

async def fetchCommentsByPostId(id):
    url = "https://jsonplaceholder.typicode.com/comments?postId=%d" % id
    print("dispatching request to %s " % url)
    try:
        result = await loop.run_in_executor(None, requet_wrapper, url)
    except ConnectionError as e:
        print("error for %s " % e.winerror)        
    print("response of url %s resolved" % url )
    return result


async def main(url):
    results = await loop.run_in_executor(None, requests.get, url)
    response = results.json()
    # print(response)
    smaller_tasks = await asyncio.wait([fetchCommentsByPostId(post['id']) for post in response])
    # print("waking up %s " % response)
    print("pre smaller_tasks all done")
    res , count = [] , 0
    errorc = 0;
    for e in [x for x in smaller_tasks[0] if x.result() is not None]:
        try:
            response = e.result()
            print(response.headers['content-encoding'])
            content = brotli.decompress(response.content).decode('utf-8')
            # print(gzip.decompress(response.content))
            ob = json.loads(content)
            res.append(ob)
        except Exception as e1:
            logging.error(e1)
        count+=1
    return res, count


if __name__ == "__main__":
    # futures = [asyncio.ensure_future(fetchPreApi(i), loop=loop) for i in range(10)]## 无序
    # futures = [loop.create_task(fetchPreApi(str(i))) for i in range(10)] ## 无序
    futures = [main("https://jsonplaceholder.typicode.com/posts")] ## 无序
    res = loop.run_until_complete(asyncio.gather(*futures))
    result , count = res[0][0] , res[0][1]
    loop.close()
    print("we have the results now  {0} only {1} request made it ".format(result,count))

