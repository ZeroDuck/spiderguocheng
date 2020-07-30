import os, time
from selenium import webdriver
import requests
herosnames =[]
mingzi=''
nameurl =[]

#启动火狐浏览器
browser = webdriver.Firefox()
#英雄联盟的英雄资料地址
wangye = "https://lol.qq.com/data/info-heros.shtml"
browser.get(wangye)
#选的英雄列表
herolist = browser.find_element_by_class_name("clearfix").find_element_by_css_selector(
    "#jSearchHeroDiv").find_elements_by_css_selector("li >a")

for i in herolist:
    mingzi = i.text.strip("'")

    # print(mingzi)
    urls = i.get_attribute('href')
    # 将英雄名字与英雄详情链接组合到一个列表
    nameurl =[mingzi,urls]
    herosnames.append(nameurl)
    # print(nameurl)
    if not os.path.exists(path='./英雄联盟数据'):
        os.mkdir(path='./英雄联盟数据')
    if not os.path.exists(path='./英雄联盟数据/'+mingzi):
        os.mkdir(path='./英雄联盟数据/'+mingzi)
for index,i in enumerate(herosnames):
    browser.get(i[1])
    time.sleep(0.5)
    try:
        browser.find_element_by_css_selector("#skinNAV").find_elements_by_css_selector('li a')[1].click()
    except:
        continue
    bg = browser.find_element_by_css_selector("#skinBG").find_elements_by_css_selector('li')
    print(index)
    for b in bg:
        #因为皮肤名字存在着非法字符，所以删掉非法字符
        title = b.get_attribute('title').replace('/','')
        img = b.find_element_by_css_selector('img').get_attribute('src')
        try:
            path = './英雄联盟数据/' + i[0] + '/' + title + '.jpg'
            #检查本地是否存在相同文件，不存在则利用requests的下载
            if not os.path.exists(path='./英雄联盟数据/'+i[0]+'/'+title+'.jpg'):
                response = requests.get(img)
                with open(path,'wb') as f:
                    f.write(response.content)
                print("下载完成" + title)
            else:
                print("已经下载过了")

        except:
            print("下载失败"+title+'   '+img)
 #下载完成自动关闭浏览器
browser.close()