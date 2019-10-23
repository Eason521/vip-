# coding:gbk

""" 本代码实现了腾讯vip视频的抓取下载，首先拿到视频播放界面的url,然后与给定的解析api拼接，
获取msu8地址，请求下载u3m8文件，提取其中的ts地址，并拼接成完整的ts url,
然后请求ts下载视频并写入ts文件或者MP4等"""
import requests
from lxml import etree
from fake_useragent import UserAgent

import urllib3

ua = UserAgent()
useragent = ua.random

urllib3.disable_warnings()  # 不显示警告信息
headers = {"User-Agent": useragent}

# movie_url = "https://v.qq.com/x/cover/zr5a67l333ehzu9.html"  # 哪吒之魔童降世
movie_url = "https://v.qq.com/x/cover/wi8e2p5kirdaf3j.html"  # 战狼2

url = 'https://jx.618g.com/?url=%s' % movie_url
response = requests.get(url=url, headers=headers).text
# print(response)
# with open('response.html','w',encoding='utf-8') as f:
#     f.write(response)
tree = etree.HTML(response)
title = tree.xpath("//title/text()")[0]
m3u8_url = tree.xpath('//div[1]/iframe/@src')[0].split("=")[1]
"""/m3u8-dp.php?url=https://cn1.ruioushang.com/hls/20190918/43caf06b8abb3d5aa93e76957184e84f/1568821235/index.m3u8"""
print(title, m3u8_url)

# #下载m3u8文件
m3u8 = requests.get(url=m3u8_url, headers=headers).text
# print(m3u8)
with open('%s.m3u8' % title, 'w', encoding='utf-8') as f:
    f.write(m3u8)
# # 提取m3u8文件里的ts路径并拼接

m3u8_str = m3u8_url.split('/')
base_url = m3u8_str[0] + "//" + m3u8_str[2]
# base_url = 'https://cn1.ruioushang.com'
ts_url_list = []
with open('%s.m3u8' % title, "r") as file:
    lines = file.readlines()
    for line in lines:
        if line.endswith(".ts\n"):
            ts_url_list.append(base_url + line.strip("\n"))
print(ts_url_list)
for ts_url in ts_url_list:
    # print(ts_url)
    a = ts_url.split(".ts")[0]
    ts_name = a.split("/")[-1]
    print(ts_name)
    try:
        response = requests.get(ts_url, stream=True, verify=False)
        # print(response)
        with open("%s.mp4" % (title,), "ab+") as f:
            f.write(response.content)
    except Exception as e:
        print("异常请求：%s" % e.args)

# # 测试 cmd命令
# test = 'ping www.baidu.com'
# os.system(test)

# # 命令行下载m3u8地址的视频
# # ffmpeg -i  "https://cn3.playfeel.cc/hls/20190824/d1cda3b4e14619b923a705e846f7c37f/1566648971/index.m3u8" -vcodec copy - acodec copy "xxx.mp4"

# # 转换格式
#  ffmpeg -f concat -i video.txt -c copy output.mkv
"""
ts  url分析
https://cn1.ruioushang.com/hls/20190918/43caf06b8abb3d5aa93e76957184e84f/1568821235/index.m3u8   # m3u8地址已知
/hls/20190918/43caf06b8abb3d5aa93e76957184e84f/1568821235/film_00000.ts             # ts部分路径

拼接完整的ts路径
https://cn1.ruioushang.com/hls/20190918/43caf06b8abb3d5aa93e76957184e84f/1568821235/film_00000.ts
"""
