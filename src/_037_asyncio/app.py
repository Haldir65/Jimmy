import asyncio

## https://www.youtube.com/watch?v=BI0asZuqFXM Asyncio - Asynchronous programming with coroutines - Intermediate Python Programming p.26

async def find_divisible(inrange,div_by):
    print("finding nums in range {} divisible by {}".format(inrange,div_by))
    located = []
    for i in range(inrange):
        if i % div_by ==0:
            located.append(i) 
        if i % 500 == 0 :
            await asyncio.sleep(0.00001)
    print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))            
    return located


async def main():
    divs1 = loop.create_task(find_divisible(50200,34113))
    divs2 = loop.create_task(find_divisible(5200,34113))
    divs3 = loop.create_task(find_divisible(500,34113))
    await asyncio.wait([divs1,divs2,divs3])
    return divs1,divs2,divs3


if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        d1 ,d2 ,d3 = loop.run_until_complete(main())
        print(d1.result())
    except Exception as e:
        pass        
    finally:
        loop.close()


## aiohttp for async htp request    