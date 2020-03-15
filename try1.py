# socket 仅接受ip
# gethostbyname将域名转换为ip
# gethostbyname_ex则返回更全面的信息(一个三元组)，第三项是一个包括所有ip地址的列表

def fun123(x):
    return x**2


if __name__ == "__main__":
    import socket
    print(socket.gethostbyname_ex('live.bilibili.com'))

    import os
    os.system('pause')

    # 1970-1-1 => now,seconds
    import time
    print(time.time())

    # plot
    from matplotlib import pyplot as plt
    import numpy as np
    x1 = np.arange(-0.1,-0.01,0.01)
    x2=np.arange(0.01,0.1,0.01)
    x = np.concatenate((x1,x2))
    y=600/x*(1-np.exp(-15*x))
    # z=600*(1-np.exp(-15*x))
    plt.plot(x,y)
    # plt.plot(x,z)
    plt.show()
