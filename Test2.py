import requests
import re
headers = {

   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/81.0.4044.129 Safari/537.36 '
}
pattern = re.compile('<dd>.*?"board-index board-index-.*?">(.*?)</i>.*?<img data-src="(.*?)".*?<p class="name">.*?">('
                     '.*?)</a></p>.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>.*?<p '
                     'class="score"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i>.*?</dd>',re.S)
def one_page_get():
    r = requests.get('https://maoyan.com/board/4', headers=headers)
    print(r.text)
    content = re.findall(pattern,r.text)
    for item in content:
        yield {
            'rank': item[0],
            'image': item[1],
            'name': item[2].strip(),
            'star' : item[3].strip(),
            'time' : item[4].strip(),
            'score' : item[5].strip()+item[6].strip()
        }

one_page_get()