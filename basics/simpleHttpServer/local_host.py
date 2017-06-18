#!/usr/bin/python
# -*- coding: UTF-8 -*-

import http.server
from socketserver import BaseRequestHandler, TCPServer
from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import socketserver
import os


def create_local_host():
    PORT = 10800

    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print('server at port ', PORT)
    httpd.serve_forever()

create_local_host()

