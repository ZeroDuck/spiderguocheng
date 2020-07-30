"""
仅供测试
学习爬虫

uft-8
author:ZXJ(zero)
version：1.0
该版本不能抓取json的图片，只能从image_list中的网页提取图片
该版本还存在着image的TypeError现象，并没有修正只是利用try让其跳过

"""

import requests
from urllib.parse import urlencode

# 基础网页，基础网页加尾部做到多页抓取
base_url = 'https://www.toutiao.com/api/search/content/?'

headers = {
    'cookie': 'tt_webid=6828177575999915527; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6828177575999915527; '
              'csrftoken=f8fc163b3e428ba0ad658f16262c7ed7; SLARDAR_WEB_ID=f62ad535-d11b-4ede-be6b-3fa92571a2a1; '
              'ttcid=d904656f6a194f89b0fdcde4b8fa083583; '
              's_v_web_id=verify_kadhj2jh_kMWcFsxO_FDFE_4PB3_8riQ_GohqPEmiwITj; '
              '__tasessionId=wqkfnkguc1589874958712; '
              'tt_scid=WaeKw371i97NssCmysAPcz8TuIzTSYGqHxwEq3uqeCUZbVI0DpJ5dlC0fhuiY7pXc33d',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'http://toutiao.com/group/6828341075556434435/'
}


# 抓取一页的网页数据

def one_page(offset):
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'pd': 'synthesis',
        'from': 'search_tab'
    }
    headers = {
        'cookie': 'tt_webid=6828177575999915527; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6828177575999915527; '
                  'csrftoken=f8fc163b3e428ba0ad658f16262c7ed7; SLARDAR_WEB_ID=f62ad535-d11b-4ede-be6b-3fa92571a2a1; '
                  'ttcid=d904656f6a194f89b0fdcde4b8fa083583; '
                  's_v_web_id=verify_kadhj2jh_kMWcFsxO_FDFE_4PB3_8riQ_GohqPEmiwITj; '
                  '__tasessionId=wqkfnkguc1589874958712; '
                  'tt_scid=WaeKw371i97NssCmysAPcz8TuIzTSYGqHxwEq3uqeCUZbVI0DpJ5dlC0fhuiY7pXc33d',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'http://toutiao.com/group/6828341075556434435/'
    }
    url = base_url + urlencode(params)
    try:
        responese = requests.get(url, headers=headers)
        # print(responese.text)
        if responese.status_code == 200:
            return responese.json()
    except requests.ConnectionError as e:
        print('Error!', e.args)


# 分析数据，提取有用信息

def get_mages(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            if title is None or title == '街拍-百科':  # 去掉空白title
                continue
            # print(title)

            # 这里的文章链接可能有提取网页当中的图片，以后版本可以用到。
            article_url = item.get('article_url')  # 获取文章的链接，图片的链接。
            image_list = item.get('image_list')
            # print(article_url)
            yield {
                'title': title,
                'article_url': article_url,
                'image_list': image_list
            }

# os是用于创建文件夹，hashlib 用于名字命名，这里不太懂

import re
import os
from hashlib import md5


# def filefolder(title):
#     if not os.path.exists(r'./爬取今日头条街拍图'):
#         os.mkdir(r'./爬取今日头条街拍图')
#     if not os.path.exists(r'./爬取今日头条街拍图/{}'.format(title)):
#         os.mkdir(r'爬取今日头条街拍图/{}'.format(title))

# get_mages(one_page(10))

def save_images():
    for item in get_mages(one_page(0)):
        titles = item['title']
        titles = re.sub(r'[|\.]', '', titles)      # 去掉非法字符。以免文件夹不能用
        images_list = item['image_list']
        articles_url = item['article_url']
        try:
            for image in images_list:
                image_url = image['url']
                print(image_url)
                response = requests.get(image_url, headers=headers)
                if not os.path.exists(r'./爬取今日头条街拍图'):
                    os.mkdir(r'./爬取今日头条街拍图')
                if not os.path.exists(r'./爬取今日头条街拍图/{}'.format(titles)):
                    os.mkdir(r'爬取今日头条街拍图/{}'.format(titles))
                else:
                    try :
                        with open(r'爬取今日头条街拍图/{}/{}.{}'.format(titles, md5(response.content).hexdigest(), 'jpg'), 'wb') as f:
                            f.write(response.content)           # 储存图片到每个title为名的文件夹当中
                        print('Download successfully!')
                    except ConnectionError as e:               # 这里的错误原因没写明白，需要更改！
                        print(' unsuccessfully! ', e.args)
                print(titles)
                print(image_url)

        except TypeError as t:
            pass



save_images()
