# 获取到所有电影url 利用下载代码进行下载
"""
url = "https://v.qq.com/x/list/movie?&offset=0" 第一页
url = "https://v.qq.com/x/list/movie?&offset=30" 第二页
url = "https://v.qq.com/x/list/movie?&offset=60" 第三页

共167页"""

import requests
from lxml import etree
from fake_useragent import UserAgent

ua=UserAgent().random
headers = {'User-Agent':ua}
for i in range(167):
    url = "https://v.qq.com/x/list/movie?&offset=%d"%(i*30)
    response = requests.get(url=url,headers=headers).text
    # print(response)
    tree = etree.HTML(response)
    video_list = tree.xpath("//li[@class='list_item']")
    print(video_list)  #
    for node in video_list:
        name = node.xpath(".//strong[@class='figure_title']/a/text()")
        print(name)
        play_url = node.xpath(".//a/@href")[0]
        print(play_url)

