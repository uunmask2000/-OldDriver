'''
Arthur       : kk
Date         : 2022-02-07 14:41:27
LastEditTime : 2022-02-07 15:08:51
LastEditors  : your name
Description  : 自動生成 [嚴格紀律 Description]
FilePath     : \-OldDriver\JKF_girls_v2.py
嚴格紀律
'''
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


###
CustomEncryption = CustomEncryption.CustomEncryption()
JkfClass = JkfClass.JkfClass(123456, 'jkf_girls_api')


def inint():

    temple_ = {
        # 搜尋瑪
        "serchcode":  '',
        # 網址
        "host": "",
        # 作者
        "auth": '',
        # 人員
        "personnel": '',
        # 標題
        "title": '',
        # 關鍵字
        "series": '',
        # 圖片
        "img":  [],
        'img_rows': 0,
        ##########################
        # 關鍵字
        "keywords": "",
        # 簡介
        "description": "",
        # 部分
        "section": []


    }

    return temple_


def singe_page(url, _text):

    ###
    # title
    # <meta property="article:section" content="正妹">
    # <meta property="article:section2" content="台灣正妹">
    # <meta name="keywords" itemprop="keywords" content="阿粗嚴選,阿粗學長,jieeeshin,潔 心,正妹,奶好大" />
    # <meta name="description" content="這次受到阿粗學長的感召！要推薦大家「阿粗」分享ㄉ正妹～以前都覺得全糖妹才是真妹子，現在閱妹無數之後才發現臭臉妹才是王道啊！！有兇兇的脾氣，才有兇兇的身材 ... ♥阿粗嚴選♥臭臉妹身材好暴力！海島曬乳「絕美水滴胸型」好Q好飽滿...老司機嗨到起秋~  (阿粗嚴選,阿粗學長,jieeeshin,潔 心,正妹,奶好大)"/>

    ##
    temple_ = inint()
    _text = "Tgmv{}".format(_text)

    # _text = url.replace('https://www.jkforum.net/thread-',
    #                     '').replace('.html', '')
    print(_text)
    if(JkfClass.check_json(_text)):
        print('url ' + url)
        return True
    file_s = []
    ###
    soup = JkfClass.get_soup(url)
    try:
        div_ = soup.find('div', {'class': 't_fsz'}).find_all('img')
    except expression as identifier:
        return False

    # print(div_)
    for target_list in div_:
        file_ = target_list.get('file')
        # print(file_)
        if file_ == None:
            pass
        else:
            file_s.append(file_)
    # 圖片
    # print(file_s)
    temple_['img'] = file_s
    temple_['img_rows'] = len(file_s)
    ##
    temple_['host'] = url
    temple_['h1'] = _text
    temple_['title_main'] = CustomEncryption.removePunctuation(
        soup.find("meta",  property="og:title")['content'])
    temple_['title'] = ','.join(str(i) for i in re.findall(
        u"[\u4e00-\u9fa5]+", soup.title.text))
    ####
    try:
        temple_['section'].append(
            soup.find("meta",  property="article:section")['content'])
        temple_['section'].append(
            soup.find("meta",  property="article:section2")['content'])
    except:
        pass

    # print(temple_)
    # <meta property="dable:item_id" content="4952696">
    # temple_['serchcode'] = soup.find("meta", property="dable:item_id")['content']
    # 使用網址 進行 b16encode
    # print(temple_)
    # return True
    # temple_['serchcode'] = CustomEncryption.b16_encode(url)
    temple_['serchcode'] = _text

    temple_['keywords'] = soup.find(attrs={"name": "keywords"})['content']
    temple_['description'] = soup.find(
        attrs={"name": "description"})['content']
    # print(temple_)

    # IMG path
    temple_['img'] = JkfClass.get_to_image(
        _text,  temple_['img'],  temple_['img_rows'])
    # JSON path
    JkfClass.get_to_json(temple_,   _text)
    # if len(temple_['img']) > 10:
    #     # IMG path
    #     temple_['img'] = JkfClass.get_to_image(
    #         _text,  temple_['img'],  temple_['img_rows'])
    #     # JSON path
    #     JkfClass.get_to_json(temple_,   _text)
    # else:
    #     print('少於十張')

    return True


def list_page(url):
    soup = JkfClass.get_soup(url)
    # print(soup)
    aa = soup.find_all('a', {'class': "z"})
    number = 0
    for _a in aa:
        url = _a.get('href')
        title = CustomEncryption.removePunctuation(_a.get('title'))
        if url.find("typeid") == -1:
            print(url, ' : ', title)
            number += 1
            _url = 'https://www.jkforum.net/' + url
            singe_page(_url, number)
    return True


# 抓取頁數
___url = "https://www.jkforum.net/forum-1112-{}.html"
for i in range(1, 20):
    url = ___url.format(i)
    print(url)
    list_page(___url.format(i))
