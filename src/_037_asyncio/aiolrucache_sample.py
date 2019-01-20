import asyncio

import aiohttp
from async_lru import alru_cache


@alru_cache(maxsize=32)
async def get_pep(num):
    resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(resource) as s:
                return await s.read()
        except aiohttp.ClientError:
            return 'Not Found'

@alru_cache(maxsize=50)
async def get_json_line(num):
    resource = 'https://jsonplaceholder.typicode.com/todos/%s' % num
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(resource) as s:
                return await s.read();
        except aiohttp.ClientError:
            return 'Erro'



async def main():
    #for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
     #   pep = await get_pep(n)
      #  print(n, len(pep))

    for n in range(100):
        jsons = await get_json_line(n)
        print(n, jsons.decode("utf-8"))
    #print(get_pep.cache_info())
    # CacheInfo(hits=3, misses=8, maxsize=32, currsize=8)

    # closing is optional, but highly recommended
#    await get_pep.close()


loop = asyncio.get_event_loop()

loop.run_until_complete(main())

loop.close()
