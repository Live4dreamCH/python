import socket


def my_encode(mac):
    """与服务器端一致的加密解密"""
    maclist = list(mac)
    for i in range(len(maclist)):
        maclist[i] = chr((ord(maclist[i])+i**3) % 128)
    newmac = "".join(maclist)
    return newmac.encode('utf-8')

def my_decode(newmac):
    """与服务器端一致的加密解密"""
    newmac = newmac.decode('utf-8')
    maclist = list(newmac)
    l = len(maclist)
    for i in range(l):
        maclist[i] = chr((ord(maclist[i])-i**3) % 128)
    mac = "".join(maclist)
    return mac

if __name__ == "__main__":
    link = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    domain = 'www.live4dreamch.xyz'
    IP = socket.gethostbyname(domain)
    port = 17264
    link.connect((IP, port))
    print('连接注册服务器端成功！')
    num = input('input a number\n')
    link.send(my_encode(num))
    for i in range(int(num)):
        print(my_decode(link.recv(1024)))
    link.close()
    print("fin")