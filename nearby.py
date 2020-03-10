# coding = utf-8

import urllib.request
import urllib.parse
import http.cookiejar


def get_nearby_addr():
    headers = {
        'Host': 'zabm.fjadd.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    url = 'http://zabm.fjadd.com/weixin/zhfw/yaoyiyao_list.jsp?longitude=118.70638&latitude=25.365812&radius=10'

    request = urllib.request.Request(url, headers=headers)
    filename = 'cookie.txt'
    # 使用http.cookiejar.CookieJar()创建CookieJar对象
    cjar = http.cookiejar.CookieJar()
    # 使用HTTPCookieProcessor创建cookie处理器，并以其为参数构建opener对象
    cookie = urllib.request.HTTPCookieProcessor(cjar)
    opener = urllib.request.build_opener(cookie)
    # 将opener安装为全局
    urllib.request.install_opener(opener)

    try:
        response = urllib.request.urlopen(request)
        print(response.read().decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.reason)


if __name__ == '__main__':
    get_nearby_addr()
    pass
