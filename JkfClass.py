'''
Arthur       : kk
Date         : 2022-02-07 14:41:55
LastEditTime : 2022-02-07 16:15:11
LastEditors  : your name
Description  : 自動生成 [嚴格紀律 Description]
FilePath     : \-OldDriver\jkfClass.py
嚴格紀律
'''
import base64
import re
import string
import requests
import re
import json
import os
import requests
import urllib.request
import time
import base64
import datetime
import sys

import string
import shutil

import CustomEncryption
import JkfClass

# 引入 Beautiful Soup 模組
from bs4 import BeautifulSoup


class JkfClass:
    '''
    預設值
    '''

    def __init__(self, key=None, path=None):
        if key == None:
            self.key = '1234567'
        self.key = key
        if path == None:
            self.path = 'JKF_common'
        self.path = path

    def cr_dir(self, FILE_PATH):
        if os.path.isdir(FILE_PATH):  # 不用加引号，如果是多级目录，只判断最后一级目录是否存在
            pass
        else:
            # 只能创建单级目录，用这个命令创建级联的会报OSError错误         print 'mkdir ok
            os.mkdir(FILE_PATH)
        return True

    def check_json(self, _name):
        print(self.path)
        path = './json/'
        self.cr_dir(path)
        path = './json/'+self.path+'/'
        self.cr_dir(path)
        filename = path + str(_name) + '.json'
        realpath = os.path.normpath(filename)
        print(realpath)
        type = os.path.exists(realpath)
        print(filename)
        print(type)
        return type

    def get_soup(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        headers['Referer'] = url
        r = requests.get(url, headers=headers)

        html_doc = r.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        return soup

    def get_to_json(self, content, _prex):
        ###
        path = './json/'
        self.cr_dir(path)
        path = './json/'+self.path+'/'
        self.cr_dir(path)
        ###
        filename = path + str(_prex) + '.json'
        # print(filename)
        # print(_prex)
        # print(content)
        # Writing JSON data
        try:
            with open(filename, 'w') as f:
                json.dump(content, f)
        except:
            pass
        # with open(filename, 'w') as f:
        #     json.dump(content, f)

        return True

    def get_to_image(self, _prex,  img,  max=20):

        try:
            path = './images/'+self.path+'/'
            self.cr_dir(path)
            # 過濾
            path = path + str(_prex) + '/'
            self.cr_dir(path)
            true_local_path = []

            # ------------------------------------------------------
            _s1 = len(os.listdir(path))
            _S1 = len(img)
            # print(img)
            # print(_s1)
            # print(_S1)

            # 刪除資料夾。
            if _S1 == 0:
                try:
                    shutil.rmtree(path)
                except OSError as e:
                    print(e)
                return []

            # 下載圖片
            if _s1 == _S1:
                # 空資料夾刪除
                if _s1 == 0:
                    try:
                        shutil.rmtree(path)
                    except OSError as e:
                        print(e)
                return []
            else:
                print('下載圖片')
            # ------------------------------------------------------

            row = 0
            for url_img in img:
                ##
                row += 1
                html = requests.get(url_img)
                img_name = path + str(row) + '.png'
                type = os.path.exists(img_name)
                print(type)
                if type == False:
                    ####
                    true_local_path.append(img_name)
                    # pass
                    with open(img_name, 'wb') as file:  # 以byte的形式將圖片數據寫入
                        file.write(html.content)
                        file.flush()
                    file.close()  # close file
                else:
                    print('第 %d 張 已經下載' % (row))
                print('第 %d 張' % (row))
                # time.sleep(1)
        except:
            true_local_path = ""
        ###

        return true_local_path
