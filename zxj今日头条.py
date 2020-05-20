import requests
from urllib.parse import urlencode

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
        'cookie':'tt_webid=6828177575999915527; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6828177575999915527; '
                 'csrftoken=f8fc163b3e428ba0ad658f16262c7ed7; SLARDAR_WEB_ID=f62ad535-d11b-4ede-be6b-3fa92571a2a1; '
                 'ttcid=d904656f6a194f89b0fdcde4b8fa083583; '
                 's_v_web_id=verify_kadhj2jh_kMWcFsxO_FDFE_4PB3_8riQ_GohqPEmiwITj; '
                 '__tasessionId=wqkfnkguc1589874958712; '
                 'tt_scid=WaeKw371i97NssCmysAPcz8TuIzTSYGqHxwEq3uqeCUZbVI0DpJ5dlC0fhuiY7pXc33d',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent':'http://toutiao.com/group/6828341075556434435/'
    }
    url = base_url +urlencode(params)
    try :
        responese = requests.get(url,headers = headers)
        # print(responese.text)
        if responese.status_code ==200:
            return responese.json()
    except requests.ConnectionError as e :
        print('Error!',e.args)

def get_mages(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            if title is None or title == '街拍-百科':
                continue
            # print(title)

            article_url = item.get('article_url')
            image_list = item.get('image_list')
            # print(article_url)
            yield {
                'title': title,
                'article_url': article_url,
                'image_list': image_list
            }


import re
import os
from hashlib import md5
# def filefolder(title):
#     if not os.path.exists(r'./爬取今日头条街拍图'):
#         os.mkdir(r'./爬取今日头条街拍图')
#     if not os.path.exists(r'./爬取今日头条街拍图/{}'.format(title)):
#         os.mkdir(r'爬取今日头条街拍图/{}'.format(title))

# get_mages(one_page(10))
pattern = re.compile(r'[|\.]')
def save_images():
    for item in get_mages(one_page(0)):
        titles = item['title']
        titles = re.sub(r'[|\.]', '', titles)
        images_list = item['image_list']
        articles_url = item['article_url']
        for image in images_list:
            image_url = image['url']
            response = requests.get(image_url, headers = headers)
            if not os.path.exists(r'./爬取今日头条街拍图'):
                os.mkdir(r'./爬取今日头条街拍图')
            if not os.path.exists(r'./爬取今日头条街拍图/{}'.format(titles)):
                os.mkdir(r'爬取今日头条街拍图/{}'.format(titles))
            else :
                with open(r'爬取今日头条街拍图/{}/{}.{}'.format(titles, md5(response.content).hexdigest(), 'jpg'),'wb') as f:
                    f.write(response.content)
            print('Download successfully!')

        print(titles)
        # print(image_list)


save_images()


