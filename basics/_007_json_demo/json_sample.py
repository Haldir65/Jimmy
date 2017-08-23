#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/23 15:22
# @Author  : Aries
# @Site    : 
# @File    : json_sample.py
# @Software: PyCharm Community Edition
import json, os, subprocess

from shutil import copyfile


# 给一个jsonArray ，用json解析成一个字典
def convert_string_to_json(content):
    result = json.loads(content)
    for index, part in enumerate(result):
        print(str(index) + " " + part['title'] + ' ' + part['url'])
    return result


# 读取文件，返回str
def read_string_from_file(file_src):
    abs_path = os.path.join(os.path.abspath(os.path.curdir), file_src)
    if os.path.exists(abs_path):
        with open(abs_path, 'r', encoding='utf-8')  as f:
            content = f.read()  # don't use readline , it will add line escape
            return content


def iterate_stuff(content):
    for index in range(len(content)):
        print(content[index])


def judge_line():
    abs_path = os.path.join(os.path.abspath(os.path.curdir), 'samples.json')

    if os.path.exists(abs_path):
        with open(abs_path, 'r', encoding='utf-8')  as f:
            lines = f.readlines()
        with open('sample3.json', 'w+', encoding='utf-8') as out:
            for c in lines:
                print(c)
                out.write(c)
            print('copy file succeed')


# remove designated index from file and write to original file
def remove_index_from_dict(downloaded_urls, filename):
    contents = json.loads(read_string_from_file(filename))
    for deleted_url in downloaded_urls:
        for index in range(len(contents)):
            if contents[index]['url'] == deleted_url:
                contents.pop(index) ## contens.remove(index)报错 TypeError: 'builtin_function_or_method' object is not subscriptable
                # https://stackoverflow.com/questions/8322534/typeerror-builtin-function-or-method-object-is-not-subscriptable
                break

    # for index in range(len(contents)):
    #     if contents[index]['url'] in downloaded_urls:
    #         contents.pop(index)  # remove item in dict
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(contents, file)
        print(str(len(contents))+'save file ------------------------------------------------------')


def down_load_url_and_add_to_dict(title, url):
    print('begining download ' + title)
    # subprocess.call('you-get ' + url, shell=True) ## make system call to execute download operation
    print('end download ' + title)


def main():
    content = read_string_from_file('samples.json')
    json_dict = convert_string_to_json(content)  ## a list of dict
    already_down_loaded = []
    for index in range(len(json_dict)):
        data = json_dict[index]
        try:
            down_load_url_and_add_to_dict(data['title'], data['url'])
            already_down_loaded.append(data)
        except Exception as e:
            print('error occured when downloading ' + data['title'])
        # if get_occupied_space_on_disk()>70:
        #     break
        if len(already_down_loaded) > 70:
            break
    indexs = []
    for item in already_down_loaded:
        indexs.append(item['url'])
    remove_index_from_dict(indexs, 'sample3.json')


# 获取磁盘剩余空间所占百分比
def get_occupied_space_on_disk():
    disk = os.statvfs('/')
    percent = (disk.f_blocks - disk.f_bfree) * 100 / (disk.f_blocks - disk.f_bfree + disk.f_bavail)
    print('occupied disk percentage ' + str(percent))
    return percent


#
# indexs = [x for x in range(10)]
# remove_index_from_dict(indexs, 'sample3.json')
# copyfile('samples.json','sample3.json')

main()
