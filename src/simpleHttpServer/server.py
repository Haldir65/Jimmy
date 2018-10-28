#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
from http.server import SimpleHTTPRequestHandler
from http.server import BaseHTTPRequestHandler, HTTPServer
from wsgiref.simple_server import make_server


# Web Server GateWay Interface
def test(HandlerClass=SimpleHTTPRequestHandler,
         ServerClass=HTTPServer):
    protocol = "HTTP/1.0"
    host = ''
    port = 8000
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if ':' in arg:
            host, port = arg.split(':')
            port = int(port)
        else:
            try:
                port = int(sys.argv[1])
            except:
                host = sys.argv[1]

    server_address = (host, port)

    HandlerClass.protocol_version = protocol
    HandlerClass.extensions_map.update({
        '.webapp': 'application/x-web-app-manifest+json',
    })
    httpd = ServerClass(server_address, HandlerClass)

    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    httpd.serve_forever()


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'Text/html')])
    return [b'<h1>Hello ,there </h1>']


def serve():
    httpd = make_server('', 8000, application)
    print('Serving Http on Port 8000....')
    httpd.serve_forever()


if __name__ == "__main__":
    test()
