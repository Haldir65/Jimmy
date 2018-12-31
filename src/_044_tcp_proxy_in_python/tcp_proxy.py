#!/usr/bin/env python
# coding: utf-8
# yc@2011/11/08
# usage: python tcp_proxy.py -l 0.0.0.0:1021 -r 911.im:80 -v

from __future__ import with_statement
import socket
import re
import sys
import threading
from optparse import OptionParser
import signal
import os  
import time 


def readConfiguration(signalNumber, frame):  
    print ('(SIGHUP) reading configuration')
    return

def terminateProcess(signalNumber, frame):  
    print ('(SIGTERM) terminating the process')
    sys.exit()

def receiveSignal(signalNumber, frame):  
    print('Received:', signalNumber)
    return


def parse_cmd():
    re_ip_port = r'^(?P<addr>.+:)?(?P<port>[0-9]{1,5})$'

    parser = OptionParser(
        usage='%prog -l [host:]port -r host:port [-v]', version='%prog 1.0')
    parser.add_option('-l', dest='local',
                      help='local addr(optional) & port: 0.0.0.0:123 or 123')
    parser.add_option('-r', dest='remote',
                      help='remote addr & port: 911.im:123')
    parser.add_option('-v', dest='verbose', default=False,
                      action='store_true', help='print stat to screen')

    options, args = parser.parse_args()
    if not options.local or not options.remote:
        parser.print_usage()
        sys.exit(-1)

    x = re.match(re_ip_port, options.local)
    if not x:
        parser.error('local format error!')
    local_addr = x.group('addr') or '0.0.0.0'
    local_addr = local_addr.rstrip(':')
    local_port = x.group('port')
    if not local_port:
        parser.error('specify local port plz!')
    local_port = int(local_port)

    x = re.match(re_ip_port, options.remote)
    if not x:
        parser.error('remote format error!')
    remote_addr = x.group('addr')
    if not remote_addr:
        parser.error('specify remote addr plz!')
    remote_addr = remote_addr.rstrip(':')
    remote_port = x.group('port')
    if not remote_port:
        parser.error('specify remote port plz!')
    remote_port = int(remote_port)
    verbose = options.verbose

    return local_addr, local_port, remote_addr, remote_port, verbose


log_lock = threading.Lock()


def log(msg):
    if verbose:
        with log_lock:
            print(msg)


def sock_proxy(sock_in, sock_out, forward):
    addr_in = '%s:%d' % sock_in.getpeername()
    addr_out = '%s:%d' % sock_out.getpeername()

    while True:
        try:
            data = sock_in.recv(4096) 
            # print('try reading')
        except Exception as e:
            log('Socket read error of %s: %s' % (addr_in, str(e)))
            break

        if not data:
            # log('Socket closed by ' + addr_in)
            continue
        else:
            if forward:
                log('reading data %s from local client ' % data)
            else:
                log('reading data %s from remote server ' % data)    
        try:
            if forward:
                request = 'GET / HTTP/1.1\r\nHost: www.zhihu.com\r\nContent-Type: text/html; charset=utf-8\r\n\r\n\r\n'
                sock_out.sendall(request.encode())
            else:
                ## reeving data
                sock_out.sendall(data)
        except Exception as e:
            log('Socket write error of %s: %s' % (addr_out, str(e)))
            break
        if forward:
            log('sending out %s => %s (%d bytes)' % (addr_in, addr_out, len(data)))
        else:
            log('receving data from remote server %s => %s (%d bytes)' % (addr_in, addr_out, len(data)))

    sock_in.close()
    if forward:
        log('client to server closing')
    else:
        log('server to client closing')
    sock_out.close()


def new_clients(sock_in):
    sock_out = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock_out.connect((remote_addr, remote_port))
    except socket.error as e:
        sock_in.close()
        log('Remote error: %s' % str(e))
        return

    threading.Thread(target=sock_proxy, args=(sock_in, sock_out, True)).start()
    threading.Thread(target=sock_proxy, args=(sock_out, sock_in, False)).start()


def register_signal():
    # register the signals to be caught
    signal.signal(signal.SIGHUP, readConfiguration)
    signal.signal(signal.SIGINT, terminateProcess) ## ctrl + c 
    signal.signal(signal.SIGQUIT, receiveSignal)
    signal.signal(signal.SIGILL, receiveSignal)
    signal.signal(signal.SIGTRAP, receiveSignal)
    signal.signal(signal.SIGABRT, receiveSignal)
    signal.signal(signal.SIGBUS, receiveSignal)
    signal.signal(signal.SIGFPE, receiveSignal)
    #signal.signal(signal.SIGKILL, receiveSignal)
    signal.signal(signal.SIGUSR1, receiveSignal)
    signal.signal(signal.SIGSEGV, receiveSignal)
    signal.signal(signal.SIGUSR2, receiveSignal)
    signal.signal(signal.SIGPIPE, receiveSignal)
    signal.signal(signal.SIGALRM, receiveSignal)
    signal.signal(signal.SIGTERM, terminateProcess)

local_addr, local_port, remote_addr, remote_port, verbose = parse_cmd()
sock_main = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_main.bind((local_addr, local_port))
sock_main.listen(5)
log('Listening at %s:%d ...' % (local_addr, local_port))
register_signal()

while True:
    try:
        sock, addr = sock_main.accept()
    except (KeyboardInterrupt, SystemExit):
        log('Closing...')
        sock_main.close()
        break

    threading.Thread(target=new_clients, args=(sock,)).start()
    log('New clients from %s:%d' % addr)
