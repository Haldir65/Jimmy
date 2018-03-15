#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 10:49
# @Author  : Aries
# @Site    : 
# @File    : app.py.py
# @Software: PyCharm

import os

from os import path

lastStr = ''

insertChar = 'default:\n'
insertBreak = '    break;'


def modify_file(abs_path):
    with open(abs_path, 'r', encoding="utf8") as f:
        index = 0
        switch_began = False
        forward_spacing = ''
        f.seek(index)
        file_content = f.readlines()
        switch_braces = 0
        for_braces = 0
        for_began = False
        flag = False # a hint that we may begin
        for line in file_content:
            # if line.strip().__contains__('break') or line.strip().__eq__('case'):
            striped_content = line.strip()
            if striped_content.startswith('for'):
                for_began = True
            if for_began:
                if striped_content.__contains__('{'):
                    for_braces = for_braces + 1
                elif striped_content.__contains__('}'):
                    for_braces = for_braces - 1
                    if for_braces == 0:
                        for_began = False

            # we are not inside a for loop
            if not for_began:
                if striped_content.__contains__('switch'):
                    switch_began = True
                    switch_braces = 0
                if switch_began:
                    if striped_content.__contains__('{'):
                        switch_braces = switch_braces + 1
                    elif striped_content.__contains__('}'):
                        switch_braces = switch_braces - 1
                if striped_content == 'default:':
                    switch_began = False  # we observed default now, just skip this switch block
                    # we need to know how many spaces are needed
                if striped_content.startswith('case'):
                    forward_spacing = line[0:line.index('case')]

                if flag and switch_began and striped_content.__contains__('}') and switch_braces == 0:
                    line = line.replace(line,
                                        forward_spacing + insertChar + forward_spacing + insertBreak + "\n" + line)
                    file_content[index] = line
                    switch_began = False
                    forward_spacing = ''
                    print('File modified!!! ')
                if line.strip() == 'break;':
                    flag = True
                else:
                    flag = False
            index = index + 1
        with open(abs_path, 'w+', encoding='utf-8') as f2:
            for line in file_content:
                # if line.__contains__('default'):
                f2.write(line)
    print('all done')


def listAllSrcFile(rootpath, resultlist):
    if os.path.exists(rootpath) and os.path.isdir(rootpath):
        os.chdir(rootpath)
        filenames = os.listdir(rootpath)
        for fileordir in filenames:
            fileordir = os.path.join(os.path.abspath(os.curdir), fileordir)
            if os.path.exists(fileordir):
                if os.path.isdir(fileordir):
                    listAllSrcFile(fileordir, resultlist)
                else:
                    if os.path.isfile(fileordir) and fileordir.endswith('.java'):
                        resultlist.append(fileordir)
    return resultlist


def listfiles(rootpath):
    raw = os.walk(rootpath)
    result = []
    for i in raw:
        parent_dir = i[0]
        for file in i[2]:
            if file.endswith('.java'):
                result.append(os.path.join(parent_dir, file))
    with open('result.txt', 'w+', encoding='utf-8') as f:
        for index, name in enumerate(result):
            if not os.path.exists(name):
                raise EOFError
            f.write(name + '\n')
            # if name.endswith('CourseDetailActivity.java'):
            #     modify_file(name)
                # print('index ' + str(index) + 'Filename = ' + name)
            modify_file(name)



if __name__ == '__main__':
    listfiles("D:\MyApplication\/app\src\main\java") ## find bugs say java file switch case have no default ,this script will fix it
    # print(insertChar + '}')
    # openfile()
    # for index, javaFileName in enumerate(result):
    #     print(javaFileName + '\n')
