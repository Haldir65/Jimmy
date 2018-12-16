import asyncio
import time

async def speak_async(): 
    print('starting====') 
    r = await asyncio.sleep(1)
    print('OMG asynchronicity!')

loop = asyncio.get_event_loop()  
loop.run_until_complete(speak_async())  
loop.close()  