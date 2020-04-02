# -*- coding: utf-8 -*-

from requests import session
from MyGrab.NewLogin.myAES import aescrypt

my_session = session()
origin_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
my_session.headers=origin_headers
response1 = my_session.get(url='http://xkfw.xjtu.edu.cn/')
# with open('login.html', 'wb') as f:
#     f.write(response1.content)
# print(response1.headers)
# print(response1.cookies.get_dict())
print(my_session.cookies)
print(my_session.headers)

getJcaptchaCode_headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'org.xjtu.edu.cn',
    'Origin': 'http://org.xjtu.edu.cn',
    'Referer': 'http://org.xjtu.edu.cn/openplatform/login.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
}
my_session.headers = getJcaptchaCode_headers
response2 = my_session.post(url='http://org.xjtu.edu.cn/openplatform/g/admin/getJcaptchaCode')
# print(response2.text)
print(response2.headers)
print(response2.cookies)
print(my_session.cookies)
print(my_session.headers)

login_headers = {
    'Content-Length': '90',
    'Content-Type': 'application/json;charset=UTF-8'
}
my_session.headers.update(login_headers)
