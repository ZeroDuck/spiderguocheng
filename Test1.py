# import urllib.error
# import socket
# import urllib.request
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print("TIME OUT")


#
# import urllib.request
# request = urllib.request.Request('http://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))
#




# from urllib import request,parse
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
#     'Host' : 'httpbin.org'
# }
# dict = {
#     'name' : '周晓杰'
# }
# data = bytes(parse.urlencode(dict),encoding='utf8')
# req = request.Request(url,data,headers,method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))



#
# from urllib.request import HTTPBasicAuthHandler,HTTPPasswordMgrWithDefaultRealm,build_opener
# from urllib.error import URLError
# username = 'suername'
# password = 'password'
# url = 'http://localhost:5000/'
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None,url,username,password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)
# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)



# from urllib.error import URLError
# from urllib.request import ProxyHandler,build_opener
# proxy_handler =ProxyHandler({
#     'http':'http://127.0.0.1:9743',
#     'https':'https://127.0.0.1:9743'
# })
# opener = build_opener(proxy_handler)
# try:
#     result = opener.open('http://www.baidu.com')
#     print(result.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)



# import http.cookiejar,urllib.request
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+'='+item.value)



# import http.cookiejar,urllib.request
# filename ='cookies.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True,ignore_expires=True)



#
# import requests
# r = requests.get('http://www.baidu.com')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)
#


#
# import requests
# data = {
#     'User-Agent':'python-requests/2.10.0'
# }
# r = requests.get('http://httpbin.org/get',params=data)
# print(r.text)



'''
抓取失败，可能是缺少了登录。
'''
#
# import requests
# import re
# headers = {
#     'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'
#
# }
# r = requests.get('https://www.zhihu.com/explore',headers= headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
# titles = re.findall(pattern,r.text)
# print(titles)
# print(r.text)
#


'''
承接上一个失败案例额
'''
# from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
# from urllib.error import URLError
# import re
# username = '13824824883'
# password = '13824824883jie'
# url = 'https://www.zhihu.com/explore'
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None,url,username,password)
# handlers = HTTPBasicAuthHandler(p)
# opener = build_opener(handlers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
# try:
#     response = opener.open(url)
#     html = response.read().decode('utf-8')
#     titles = re.findall()       '这里未完成'
#     print(html)
#     print(titles)
# except URLError as e:
#     print(e.reason)


'''
z抓取GitHub网站图标并保存
'''
#
# import requests
# r = requests.get('https://github.com/favicon.ico')
# print(r.text)
# print(r.content)
#
# with open('favicon.ico','wb') as g:
#     g.write(r.content)
#
#


#
# import requests
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
# }
# r = requests.get('https://zhihu.com/explore',headers=headers)
# print(r.text)
#


#
# import requests
# r = requests.get('http://www.baidu.com')
# exit() if not r.status_code == requests.codes.ok else print('Request Successfully')
# print(type(r))
# print(r.status_code,type(r.status_code))
# print(type(r.text),r.text)
# print(type(r.headers),r.headers)
# print(type(r.cookies),r.cookies)




#
# import requests
# file = {'file':open('favicon.ico','rb')}
# r = requests.post('http://httpbin.org/post',files=file)
# print(r.text)


# import requests
# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key+'='+value)



import requests
headers = {
    'Cookie':'_zap=dc64efba-da97-4efb-b291-4d9e48aaa169; d_c0="AJASYaKFFhGPTjzmwVbAuK-T1g7O703o-Yg=|1586349202"; '
             '_ga=GA1.2.2146444949.1586349204; _xsrf=GcV9M5GnGqnXjaOpso77y6l66MAaWRyq; '
             '_gid=GA1.2.2043187076.1588137746; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1588137745,1588137760,'
             '1588138437,1588164657; JOID=UVoRC0khkh2kYi3DYCryQq9otfJ2WuVWywx6rw5jySicPWmtDBfgsvFiKslmC'
             '-8Z1n93BTqF5tUwrAnVK0F8TDw=; '
             'osd=VF8cAU0klxCuZijGbSD2R6plv_ZzX-hczwl_ogRnzC2RN22oCRrqtvRnJ8NiDuoU3HtyADeP4tA1oQPRLkRxRjg=; '
             'SESSIONID=lRq3VEs68qNvCII5miXbUxubpOoW52QG9VZEHwpVNe9; '
             'capsion_ticket="2|1:0|10:1588168399|14:capsion_ticket|44:ZWY0OWEyZmZlNmRkNDNiMDliNTBhZGE5YTc0YTliYWQ'
             '=|4769fd6b0d391457793f39ece229f6731b0e0f9d1d13f9d303d3564191736abe"; '
             'z_c0="2|1:0|10:1588168437|4:z_c0|92'
             ':Mi4xOHdPRUJRQUFBQUFBa0JKaG9vVVdFU1lBQUFCZ0FsVk45ZFNXWHdCX19UVEZRNERKMUQxMWE4bGNxWmFkc19FcXdn'
             '|89f7314af71dd71a98e13dd940485c27182f70f433257c56f46d41f1eef99628"; '
             'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1588168456; '
             'KLBRSID=37f2e85292ebb2c2ef70f1d8e39c2b34|1588168460|1588164654',
    'Host' : 'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/81.0.4044.122 Safari/537.36 '
}

# from requests.auth import HTTPBasicAuth
# import re
# r = requests.get('http://www.zhihu.com',headers=headers, auth =HTTPBasicAuth('13824824883','13824824883jie'))
# p = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
# print(r.text)
# title = re.findall(p,r.text)
# print(title)
#



import requests
import json
import re
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/81.0.4044.122 Safari/537.36',

}

pipei = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?="(.*?)".*?"star">('
                   '.*?)</p>.*?"releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
for i in range(10):
    pmks = i*10+1
    pmjs = i*10+10
    pm = str(pmks)+'——'+str(pmjs)
    print('{:*^120}'.format(pm))
    r = requests.get('https://maoyan.com/board/4?offset='+str(i*10),headers=headers)
    if r.status_code == requests.codes.ok:
        s=re.findall(pipei,r.text)
        for item in s:
            print(item)
















































