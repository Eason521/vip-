# coding:gbk

""" ������ʵ������Ѷvip��Ƶ��ץȡ���أ������õ���Ƶ���Ž����url,Ȼ��������Ľ���apiƴ�ӣ�
��ȡmsu8��ַ����������u3m8�ļ�����ȡ���е�ts��ַ����ƴ�ӳ�������ts url,
Ȼ������ts������Ƶ��д��ts�ļ�����MP4��"""
import requests
from lxml import etree
from fake_useragent import UserAgent

import urllib3

ua = UserAgent()
useragent = ua.random

urllib3.disable_warnings()  # ����ʾ������Ϣ
headers = {"User-Agent": useragent}

# movie_url = "https://v.qq.com/x/cover/zr5a67l333ehzu9.html"  # ��߸֮ħͯ����
movie_url = "https://v.qq.com/x/cover/wi8e2p5kirdaf3j.html"  # ս��2

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

# #����m3u8�ļ�
m3u8 = requests.get(url=m3u8_url, headers=headers).text
# print(m3u8)
with open('%s.m3u8' % title, 'w', encoding='utf-8') as f:
    f.write(m3u8)
# # ��ȡm3u8�ļ����ts·����ƴ��

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
        print("�쳣����%s" % e.args)

# # ���� cmd����
# test = 'ping www.baidu.com'
# os.system(test)

# # ����������m3u8��ַ����Ƶ
# # ffmpeg -i  "https://cn3.playfeel.cc/hls/20190824/d1cda3b4e14619b923a705e846f7c37f/1566648971/index.m3u8" -vcodec copy - acodec copy "xxx.mp4"

# # ת����ʽ
#  ffmpeg -f concat -i video.txt -c copy output.mkv
"""
ts  url����
https://cn1.ruioushang.com/hls/20190918/43caf06b8abb3d5aa93e76957184e84f/1568821235/index.m3u8   # m3u8��ַ��֪
/hls/20190918/43caf06b8abb3d5aa93e76957184e84f/1568821235/film_00000.ts             # ts����·��

ƴ��������ts·��
https://cn1.ruioushang.com/hls/20190918/43caf06b8abb3d5aa93e76957184e84f/1568821235/film_00000.ts
"""
