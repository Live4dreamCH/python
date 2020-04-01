# -*- coding: utf-8 -*-

from threading import Thread
from requests import session
from time import sleep

# import json
from random import sample, randint  # 16 digits
from string import ascii_letters, digits, punctuation


class myThread (Thread):
    """多线程，调用threading库，需要新建一个类，继承Thread，并且重载run函数"""
    def __init__(self):
        """传抢课需要的参"""
        Thread.__init__(self)
    def run(self):
        """每一个线程做的事"""
        print("\n开始线程：" + self.getName())
        SubmitWrong()
        print ("\n结束线程：" + self.getName())



def SubmitWrong():
    my_session = session()


    my_url1 = "http://45.199.55.87/sop/youxiang.php"
    my_headers1 = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Host": "45.199.55.87",
        "Proxy-Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    }
    my_session.headers=my_headers1
    response1 = my_session.get(my_url1)
    print(response1.status_code)
    if response1.status_code != 200:
        print("加载cookies失败!")
    print("cookie加载成功:")


    num = str(randint(100000000, 9999999999))
    psw = "".join(sample(ascii_letters + digits + punctuation, randint(9, 15)))

    url = "http://45.199.55.87/sop/2019.php"
    my_data = {"user": num, "pass": psw, "submit": ""}
    my_header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Length": "44",
        "Content-Type": "application/x-www-form-urlencoded",
        # "Cookie": "PHPSESSID=skhgrov9d6ndsudb1a27o8ahc2",
        "Host": "45.199.55.87",
        "Origin": "http://45.199.55.87",
        "Referer": "http://45.199.55.87/sop/youxiang.php",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    }
    my_session.headers = my_header
    respond = my_session.post(url, data=my_data)
    xxx=my_session.resolve_redirects(respond)
    print(respond.status_code)
    if respond.status_code != 200:
        print("发送账号密码失败!")
    else:
        print("发送成功:", num, psw)
    my_session.close()
    del my_session


threadlist=[]
while True:
    l = len(threadlist)
    i = 0
    while i < l:
        if not threadlist[i].is_alive():
            threadlist.pop(i)
            l -= 1
        else:
            i += 1
    if l < 20:
        for i in range(20 - l):
            thread = myThread()
            threadlist.append(thread)
            thread.start()
    sleep(0.3)
print('main thread fin')