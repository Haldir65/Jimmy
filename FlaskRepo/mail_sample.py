#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/22 17:41
# @Author  : Aries
# @Site    : 
# @File    : mail_sample.py
# @Software: PyCharm Community Edition

from flask import Flask
from flask_mail import Mail, Message
import os
import threading

## 需要在python2.7 virtual env下运行

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.163.com'  # 电子邮件服务器的主机名或IP地址
app.config['MAIL_PORT'] = '465'  # 电子邮件服务器的端口
app.config['MAIL_USE_TLS'] = True  # 启用传输层安全
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  # 邮件账户用户名 当然不要在这里写真实密码
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')  # 邮件账户的密码

# # 163使用的是TLS协议，所以要这么写：
# app.config['MAIL_PORT'] = '994'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True


## 163邮箱的端口介绍
## http://help.163.com/10/0731/11/6CTUBPT300753VB8.html

mail = Mail(app)


@app.route('/')
def index():
    msg = Message('主题', sender=os.environ.get('MAIL_USERNAME'), recipients=['test@test.com'])
    msg.body = '文本 body'
    msg.html = '<b>HTML</b> body'
    mail.send(msg)

    return '<h1>邮件发送成功</h1>'


def send_mail_async(apps, msg):
    with apps.app_context():
        mail.send(msg)


@app.route('/')
def index():
    msg = Message('主题', sender=os.environ.get('MAIL_USERNAME'), recipients=['test@test.com'])
    msg.body = '文本 body'
    msg.html = '<b>HTML</b> body'
    mail.send(msg)

    thread = threading.Thread(target=send_mail_async, args=[app, msg]) # 异步发送邮件
    thread.start()

    pass


if __name__ == '__main__':
    app.run(debug=True)


    ## Flask-Mail连接到简单邮件传输协议（SMTP）服务器，并把邮件交给这个服务器发送。如果不进行配置，Flask-Mail会连接localhost上的端口25，无需验证即可发送邮件。
    #   http://www.jianshu.com/p/3d717415121b
