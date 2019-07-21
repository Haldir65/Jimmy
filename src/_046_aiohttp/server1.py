from aiohttp import web
import json,os



class Handler:

    def __init__(self):
        pass

    async def handle_intro(self, request):
        return web.Response(text="Hello, John")

    async def handle_greeting(self, request):
        name = request.match_info.get('name', "Anonymous")
        txt = "Hello, {}".format(name)
        return web.Response(text=txt)

    async def handler_json(self,request):
        data = {'some': 'dict'}
        return web.json_response(data)    

     

# header("Content-type: application/x-ns-proxy-autoconfig");
# header("Cache-Control: no-cache, must-revalidate");
# header("Expires: Sat, 26 Jul 1997 05:00:00 GMT")

## customize headers
async def on_prepare(request, response):
    print(request.rel_url)
    theurl = request.path
    ## reference for request object
    ## https://docs.aiohttp.org/en/stable/web_reference.html
    if ".py" in theurl :
        response.headers['My-Header'] = 'Hey pac'
    else:   
        response.headers['My-Header'] = 'Hey others'

app = web.Application()
handler = Handler()
app.add_routes([web.get('/intro', handler.handle_intro),
                web.get('/greet/{name}', handler.handle_greeting),
                web.get('/api', handler.handler_json)
                ])
app.router.add_static('/static/', path='./src/', name='static',show_index=True)
app.on_response_prepare.append(on_prepare)
print("open your browser at http://127.0.0.1:8089/static/ ")
web.run_app(app,port=8089)
