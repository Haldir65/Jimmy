#!/usr/bin/python3
# -*- coding:utf8 -*-
# http://blog.csdn.net/jnu_simba/article/details/27229693

import socket
import re
import os
import codecs,logging


HOST = ''
PORT = 18004

# Read index.html, put into HTTP response data
index_content = '''
HTTP/1.x 200 ok
Content-Type: text/html

'''

file = open('index.html', 'r')
index_content += file.read()
file.close()

# Read reg.html, put into HTTP response data
reg_content = '''
HTTP/1.x 200 ok
Content-Type: text/html

'''

# file = open('reg.html', 'r')
# reg_content += file.read()
# file.close()


pic_content = '''
HTTP/1.x 200 ok
Content-Type: image/jpg

'''
# i guess the binary data are stored behind these Strings
# Read picture, put into HTTP response data
with open(os.path.join(os.getcwd(), 'image\\sunrise_dim_grass.jpg'),"rb") as binary_file:
    pic_content += str(binary_file.read())


# Configure socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(100)

# infinite loop
while True:
    # maximum number of requests waiting
    conn, addr = sock.accept()
    request = conn.recv(1024)
    if isinstance(request,bytes):
        request = str(request)
        logging.error(request)

    splited = request.split(' ')    
    if(len(splited)<2):
        continue
    method = request.split(' ')[0]
    src = request.split(' ')[1]

    print('Connect by: ', addr)
    print('Request is:\n', request)

    # deal wiht GET method
    if method == 'GET' or method.__contains__('GET'):
        if src == '/index.html':
            content = index_content
        elif src == '/image/image_12.jpg':
            content = pic_content
        elif src == '/reg.html':
            content = reg_content
        elif re.match('^/\?.*$', src):
            entry = src.split('?')[1]  # main content of the request
            content = 'HTTP/1.x 200 ok\r\nContent-Type: text/html\r\n\r\n'
            content += entry
            content += '<br /><font color="green" size="7">register successs!</p>'
        else:
            continue


    # deal with POST method
    elif method == 'POST':
        form = request.split('\r\n')
        entry = form[-1]  # main content of the request
        content = 'HTTP/1.x 200 ok\r\nContent-Type: text/html\r\n\r\n'
        content += entry
        content += '<br /><font color="green" size="7">register successs!</p>'

    ######
    # More operations, such as put the form into database
    # ...
    ######

    else:
        continue
    if(type(content) is str):
        content = content.encode('utf-8')
    conn.sendall(content)
    # close connection
    conn.close()
