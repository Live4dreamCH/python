# -*- coding: utf-8 -*-

# 服务器端
import socketserver
from time import sleep
import string
import random


def my_encode(mac):
    """加密，把原字符的ASCII值加上其下标的立方，再对128取模，得到新字符串  
    
    再在其后加上10位随机字符串，混淆"""
    maclist = list(mac)
    for i in range(len(maclist)):
        maclist[i] = chr((ord(maclist[i]) + i ** 3) % 128)
    newmac = "".join(maclist) + "".join(
        random.sample(string.ascii_letters + string.digits, 10)
    )
    return newmac.encode("utf-8")


def my_decode(newmac):
    """解密，上面过程是可逆的"""
    newmac = newmac.decode("utf-8")
    l = len(newmac) - 10
    mac = newmac[:l]
    maclist = list(mac)
    for i in range(len(maclist)):
        maclist[i] = chr((ord(maclist[i]) - i ** 3) % 128)
    newmac = "".join(maclist)
    return newmac


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        link = self.request
        address = self.client_address
        print("连接成功:", address)
        num = my_decode(link.recv(1024))
        for i in range(int(num)):
            link.send(my_encode(str(i + 1)))
            sleep(0.1)
        print("send over!")


if __name__ == "__main__":
    IP = "172.17.0.13"
    port = 17264
    add = (IP, port)
    server = socketserver.ThreadingTCPServer(add, MyServer)
    print("server started")
    server.serve_forever()
