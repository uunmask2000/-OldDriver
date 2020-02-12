
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
###

import CustomEncryption

# 引入 Beautiful Soup 模組
from bs4 import BeautifulSoup


###
CustomEncryption = CustomEncryption.CustomEncryption()


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


def cr_dir(FILE_PATH):

    if os.path.isdir(FILE_PATH):  # 不用加引号，如果是多级目录，只判断最后一级目录是否存在
        pass
    else:
        # 只能创建单级目录，用这个命令创建级联的会报OSError错误         print 'mkdir ok
        os.mkdir(FILE_PATH)
    return True


def get_soup(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    headers['Referer'] = url
    r = requests.get(url, headers=headers)

    html_doc = r.text
    # print(html_doc)
    # .decode('utf-8', 'ignore')
    # 以 Beautiful Soup 解析 HTML 程式碼
    soup = BeautifulSoup(html_doc, 'html.parser')
    return soup


def singe_page(url, _text):

    ###
    # title
    # <meta property="article:section" content="正妹">
    # <meta property="article:section2" content="台灣正妹">
    # <meta name="keywords" itemprop="keywords" content="阿粗嚴選,阿粗學長,jieeeshin,潔 心,正妹,奶好大" />
    # <meta name="description" content="這次受到阿粗學長的感召！要推薦大家「阿粗」分享ㄉ正妹～以前都覺得全糖妹才是真妹子，現在閱妹無數之後才發現臭臉妹才是王道啊！！有兇兇的脾氣，才有兇兇的身材 ... ♥阿粗嚴選♥臭臉妹身材好暴力！海島曬乳「絕美水滴胸型」好Q好飽滿...老司機嗨到起秋~  (阿粗嚴選,阿粗學長,jieeeshin,潔 心,正妹,奶好大)"/>

    ##
    temple_ = inint()
    path_name = 'JKF'

    file_s = []
    ###
    soup = get_soup(url)
    div_ = soup.find('div', {'class': 't_fsz'}).find_all('img')
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
    temple_['serchcode'] = CustomEncryption.removePunctuation(_text)

    temple_['keywords'] = soup.find(attrs={"name": "keywords"})['content']
    temple_['description'] = soup.find(
        attrs={"name": "description"})['content']
    # print(temple_)

    # IMG path
    temple_['img'] = get_to_image(temple_['serchcode'],  temple_['img'],  temple_['img_rows'])

    # JSON path
    get_to_json(temple_,  temple_['serchcode'])

    return True


def get_to_json(content, _prex):

    ###
    path = './json/JKF'
    cr_dir(path)

    ###
    filename = path + str(_prex) + '.json'
    # print(filename)
    # print(_prex)
    # print(content)
    # Writing JSON data
    with open(filename, 'w') as f:
        json.dump(content, f)

    return True


def get_to_image(_prex,  img,  count):
     ###
    path = './images/JKF'
    cr_dir(path)
    path = path + _prex + '/'
    cr_dir(path)
    #################################
    true_local_path = []
    #################################

    row = 0
    for url_img in img:
        ##
        row += 1
        html = requests.get(url_img)
        img_name = path + str(row) + '.png'
        ####
        true_local_path.append(img_name)
        # pass
        with open(img_name, 'wb') as file:  # 以byte的形式將圖片數據寫入
            file.write(html.content)
            file.flush()
        file.close()  # close file
        print('第 %d 張' % (row))
        time.sleep(1)
    return true_local_path


def list_page(url):
    soup = get_soup(url)
    # print(soup)
    aa = soup.find_all('a', {'class': "z"})
    for _a in aa:
        url = _a.get('href')
        title = _a.get('title').replace(
            '/', '_').replace(':', '_').replace('，', '_')
        if url.find("typeid") == -1:
            print(url, ' : ', title)
            _url = 'https://www.jkforum.net/' + url
            singe_page(_url, title)
    return True


# 抓取頁數
___url = 'https://www.jkforum.net/forum-520-1.html'
list_page(___url)
