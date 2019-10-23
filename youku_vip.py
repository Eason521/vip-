import requests
import re
import json

class VIP(object):
    def __init__(self):
        self.api = 'http://yun.mt2t.com/lines?url='
        self.post_url = 'http://yun.mt2t.com/lines/getdata'
        self.url = 'https://v.youku.com/v_show/id_XNDA0MDg2NzU0OA==.html?spm=a2h03.8164468.2069780.5'
    def run(self):
        res = requests.get(self.api + self.url)
        html = res.content.decode()
        print('html', html)
        key = re.findall(r'key:.*?"(.*?)"', html)
        print('key', key)
        episode = re.findall(r'episode:(.*?),', html)
        print('episode', episode)
        name = re.findall(r'name:"(.*?)"', html)  # 这个字段为空，就不返回
        print('name', name)
        type = re.findall(r'type:"(.*?)".*?name', html)  # 这个字段为空，就不返回
        print('type', type)
        return key[0], episode[0]
    def get_playlist(self):
        key, episode = self.run()
        data = {
            "url": self.url,
            "key": key,
            "episode": episode
        }
        html = requests.post(self.post_url, data=data).content.decode()
        dic = json.loads(html)
        for d in dic:
            print(d)  # 先查看下输出的内容
            url = d['Url']  # 提取里面的Url再解析
            # url = 'http://y2.mt2t.com:91/ifr?url=rG7mvsvalVBQtYTfBb2j8l1vjFs%2fOmudRmSAcZXwT9w74YebSPlorQpY%2fbqhKB25gIOAhqqJtOBzhPvR%2bJnERQ%3d%3d&type=m3u8'得到的url为这种形式
            url = self.url2(url)
            print(url)
            # 'http://youku.kuyun-leshi.com/ppvod/17BE244D58718E511AFAEAF77ACC34F7.m3u8 '这是将url转义后的形式
    def url2(self, url):
        # url = 'http://y2.mt2t.com:91/ifrurl=rG7mvsvalVBQtYTfBb2j8l1vjFs%2fOmudRmSAcZXwT9w74YebSPlorQpY%2fbqhKB25gIOAhqqJtOBzhPvR%2bJnERQ%3d%3d&type=m3u8'
        url_param = url.replace("%2b", "+").replace("%3d", "=").replace("%2f", "/")
        # url为编码过后的字符串，如上形式，可以通过字符转义将Url转换过来
        return url_param
if __name__ == '__main__':
    vip = VIP()
    vip.get_playlist()
