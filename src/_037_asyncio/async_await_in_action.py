import time
import requests
import asyncio



async def getUrlBlocking(url):
    print("starting request to %s " % url)
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, requests.get, url)
    print(response.status_code)
    return response


async def gotResponse(url):
    res = await getUrlBlocking(url)
    print(res.text)
    return res




if __name__ == "__main__":
    s = time.perf_counter()
    loop = asyncio.get_event_loop()
    tasks = [gotResponse("https://jsonplaceholder.typicode.com/posts/%s" % i) for i in range(100)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")    