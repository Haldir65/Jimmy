#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/18 23:00
# @Author  : Aries
# @Site    : 
# @File    : web_utils.py
# @Software: PyCharm Community Edition


import socket
import uuid
import socket
import struct
import datetime


def get_ethernet_address():
    return socket.gethostbyname(socket.gethostname())



# def get_ip_address(ifname):
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     return socket.inet_ntoa(fcntl.ioctl(
#         s.fileno(),
#         0x8915,  # SIOCGIFADDR
#         struct.pack('256s', ifname[:15])
#     )[20:24])


if __name__ == '__main__':
    ip = get_ethernet_address()
    print(ip)


def getCurrentTimeStr():
    now = datetime.datetime.now()
    otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    return otherStyleTime
