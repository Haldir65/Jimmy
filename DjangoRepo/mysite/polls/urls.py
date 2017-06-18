#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/18 19:46
# @Author  : Aries
# @Site    : 
# @File    : urls.py
# @Software: PyCharm Community Edition

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]