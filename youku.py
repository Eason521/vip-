# coding:gbk
import requests
from lxml import etree

import urllib3
urllib3.disable_warnings()  #不显示警告信息

# movie_url = "http://v.youku.com/v_nextstage/id_3065a94071e942b7ba6e.html?scm=20140719.rcmd.1698.show_3065a94071e942b7ba6e" #优酷视频
movie_url = "https://v.youku.com/v_nextstage/id_0358c1f07d8a11e3b8b7.html?s=0358c1f07d8a11e3b8b7&scm=20140719.rcmd.7182.show_0358c1f07d8a11e3b8b7" #优酷视频
# url = 'http://69p.top/?url=%s' % movie_url
url = 'https://jx.618g.com/?url=%s' % movie_url

print(url)
response = requests.get(url=url).text
print(response)
# with open('response.html','w',encoding='utf-8') as f:
#     f.write(response)
# tree = etree.HTML(response)
# title = tree.xpath("//title/text()")[0]
# m3u8_url = tree.xpath('//div[1]/iframe/@src')[0].split("=")[1]

title = "优酷战狼2"
m3u8_url = "http://mgsp.vod.miguvideo.com:8088/depository_sjq/asset/zhengshi/5100/171/869/5100171869/media/5100171869_5005098264_55.mp4.m3u8?msisdn=BA3CC136BCD3FF3708D66E92DA8A35A4&mdspid=&spid=600058&netType=0&sid=5500357370&pid=2028600738&timestamp=20191012142227&Channel_ID=H5_&ProgramID=632552171&ParentNodeID=-99&preview=1&playseek=000000-000600&assertID=5500357370&client_ip=218.60.8.99&SecurityKey=20191012142227&promotionId=&mvid=5100171869&mcid=1000&mpid=130000023382&playurlVersion=SJ-H1-0.0.3&userid=&jmhm=&videocodec=h264&encrypt=1671d0fc03505e6f8ea0ba9365c252c3"
# print(title, m3u8_url)

# #下载m3u8文件
m3u8 = requests.get(url=m3u8_url).text
# print(m3u8)
with open('%s.m3u8' % title, 'w', encoding='utf-8') as f:
    f.write(m3u8)

# # 提取m3u8文件里的ts路径并拼接
base_url = 'https://cn3.playfeel.cc'
ts_url_list = []
# with open('%s.m3u8' % title, "r") as file:
#     lines = file.readlines()
#     for line in lines:
#         if line.endswith(".ts\n"):
#             ts_url_list.append(base_url + line.strip("\n"))
# print(ts_url_list)
# for ts_url in ts_url_list:
#     # print(ts_url)
#     a = ts_url.split(".ts")[0]
#     ts_name = a.split("/")[-1]
#     print(ts_name)
#     try:
#         response = requests.get(ts_url, stream=True, verify=False)
#         # print(response)
#         with open("%s.ts" % (title,), "ab+") as f:
#             f.write(response.content)
#     except Exception as e:
#         print("异常请求：%s" % e.args)


# # 测试 cmd命令
# test = 'ping www.baidu.com'
# os.system(test)

# # 命令行下载m3u8地址的视频
# # ffmpeg -i  "https://cn3.playfeel.cc/hls/20190824/d1cda3b4e14619b923a705e846f7c37f/1566648971/index.m3u8" -vcodec copy - acodec copy "xxx.mp4"

# # 转换格式
#  ffmpeg -f concat -i video.txt -c copy output.mkv
"""
js分析

http://mgsp.vod.miguvideo.com:8088/depository_sjq/asset/zhengshi/5100/171/869/5100171869/media/5100171869_5005098264_55.mp4.m3u8?msisdn=BA3CC136BCD3FF3708D66E92DA8A35A4&mdspid=&spid=600058&netType=0&sid=5500357370&pid=2028600738&timestamp=20191012142227&Channel_ID=H5_&ProgramID=632552171&ParentNodeID=-99&preview=1&playseek=000000-000600&assertID=5500357370&client_ip=218.60.8.99&SecurityKey=20191012142227&promotionId=&mvid=5100171869&mcid=1000&mpid=130000023382&playurlVersion=SJ-H1-0.0.3&userid=&jmhm=&videocodec=h264&encrypt=1671d0fc03505e6f8ea0ba9365c252c3
http://mgsp.vod.miguvideo.com:8088/depository_sjq/asset/zhengshi/5100/171/869/5100171869/media/5100171869_5005098264_55.mp4_0-0.ts?msisdn=BA3CC136BCD3FF3708D66E92DA8A35A4&mdspid=&spid=600058&netType=0&sid=5500357370&pid=2028600738&timestamp=20191012142227&Channel_ID=H5_&ProgramID=632552171&ParentNodeID=-99&preview=1&playseek=000000-000600&assertID=5500357370&client_ip=218.60.8.99&SecurityKey=20191012142227&promotionId=&mvid=5100171869&mcid=1000&mpid=130000023382&playurlVersion=SJ-H1-0.0.3&userid=&jmhm=&videocodec=h264&FreePlay=1&encrypt=cc79e9e3edb3d586a5341560346018ef&hls_type=2&HlsSubType=2&HlsProfileId=0&mtv_session=cc79e9e3edb3d586a5341560346018ef
http://mgsp.vod.miguvideo.com:8088/depository_sjq/asset/zhengshi/5100/171/869/5100171869/media/5100171869_5005098264_55.mp4_0-1.ts?msisdn=BA3CC136BCD3FF3708D66E92DA8A35A4&mdspid=&spid=600058&netType=0&sid=5500357370&pid=2028600738&timestamp=20191012142227&Channel_ID=H5_&ProgramID=632552171&ParentNodeID=-99&preview=1&playseek=000000-000600&assertID=5500357370&client_ip=218.60.8.99&SecurityKey=20191012142227&promotionId=&mvid=5100171869&mcid=1000&mpid=130000023382&playurlVersion=SJ-H1-0.0.3&userid=&jmhm=&videocodec=h264&FreePlay=1&encrypt=3ca25338b76481c9664080b0006d1ab8&hls_type=2&HlsSubType=2&HlsProfileId=0&mtv_session=3ca25338b76481c9664080b0006d1ab8
http://mgsp.vod.miguvideo.com:8088/depository_sjq/asset/zhengshi/5100/171/869/5100171869/media/5100171869_5005098264_55.mp4_0-2.ts?msisdn=BA3CC136BCD3FF3708D66E92DA8A35A4&mdspid=&spid=600058&netType=0&sid=5500357370&pid=2028600738&timestamp=20191012142227&Channel_ID=H5_&ProgramID=632552171&ParentNodeID=-99&preview=1&playseek=000000-000600&assertID=5500357370&client_ip=218.60.8.99&SecurityKey=20191012142227&promotionId=&mvid=5100171869&mcid=1000&mpid=130000023382&playurlVersion=SJ-H1-0.0.3&userid=&jmhm=&videocodec=h264&FreePlay=1&encrypt=c724fae59c4eddb032991c87f2c9c1d0&hls_type=2&HlsSubType=2&HlsProfileId=0&mtv_session=c724fae59c4eddb032991c87f2c9c1d0


"""
