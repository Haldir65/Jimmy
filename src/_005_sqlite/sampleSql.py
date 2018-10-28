#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/21 14:27
# @Author  : Aries
# @Site    : 
# @File    : sampleSql.py
# @Software: PyCharm Community Edition

import sqlite3
import time
import datetime
import random

# https://pythonprogramming.net/sqlite-part-2-dynamically-inserting-database-timestamps/?completed=/sql-database-python-part-1-inserting-database/


conn = sqlite3.connect('user_info.db')  # create if none exists
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL,datestamp TEXT,keyword TEXT,value REAL)")


def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2016-01-11 13:53:39','Python',6)")
    c.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2016-01-11 13:53:39','Python',7)")
    conn.commit()
    c.close()
    conn.close()


def dynamic_data_entry():
    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H-%M-%S'))
    keyword = 'Python_Stuff'
    value = random.randrange(0, 10)
    c.execute("INSERT INTO stuffToPlot (unix,datestamp,keyword,value) VALUES(?,?,?,?)", (unix, date, keyword, value))
    conn.commit()
    print('executing one operation')


def read_from_db():
    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    print(data)  ## list
    for row in data:
        print(row)


def read_certain_data_from_db():
    # unix = str(time.time() - 10000)
    # c.execute('SELECT * FROM stuffToPlot WHERE unix > ' + unix + '')
    # unix = str(time.time() - 10000)
    c.execute('SELECT * FROM stuffToPlot WHERE value > 4 ')
    data = c.fetchall()
    [print(row) for row in data] # for 循环还可以这么写
    # for row in data:
    #     print(row)


def update_certain_value_in_table():
    c.execute('UPDATE stuffToPlot SET value=13 WHERE value = 4 ')
    conn.commit()
    pass

if __name__ == '__main__':
    create_table()
    # for i in range(10):
    #     dynamic_data_entry()
    #     time.sleep(1)  # 休眠一秒
    print('before execution')
    read_certain_data_from_db()
    update_certain_value_in_table()
    print('after execution')
    read_certain_data_from_db()
    c.close()
    conn.close()
