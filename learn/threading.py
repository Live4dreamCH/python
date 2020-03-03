from threading import Thread
import time

class myThread (Thread):
    def __init__(self, ThreadName, CourseName, delay, public):
        Thread.__init__(self)
        self.delay = delay
        self.ThreadName = ThreadName
        self.CourseName = CourseName
        self.public = public
    def run(self):
        print ("开始线程：" + self.ThreadName)
        print_time(self.ThreadName, self.CourseName, self.delay, self.public)
        print ("退出线程：" + self.ThreadName)

def print_time(threadName, CourseName, delay, public):
    # public = True
    # global public
    while public[0]:
        time.sleep(delay)
        print (threadName, ': 尝试抢', CourseName, '课')
        if delay > 5:
            public[0] = int(input('输入0、1'))

# 函数内临时变量、值传递进入函数 => 不影响其他线程内定义的同名变量
# input阻塞 => 仅那一个线程
# 更改外部变量、引用传递 => 可以影响其他线程
public = [True]

# 创建新线程
thread1 = myThread("Thread-1", '语文', 0.5, public)
thread2 = myThread("Thread-2", '数学', 7, public)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("退出主线程")