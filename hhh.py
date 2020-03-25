from threading import Thread


class myThread (Thread):
    """多线程，调用threading库，需要新建一个类，继承Thread，并且重载run函数"""
    def __init__(self, n):
        """传抢课需要的参"""
        Thread.__init__(self)
        self.n = n

    def run(self):
        """每一个线程做的事"""
        print("\n开始线程：" + self.getName())
        print(self.n, ':', fib(self.n))
        print("\n结束线程：" + self.getName())



def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)
    
for i in range(20, 30):
    thread = myThread(i)
    thread.start()
print("mainThread fin.")

# answers = [-1 for i in range(10005)]
# answers[1] = 1
# answers[2] = 1

# def fib(n):
#     if answers[n] == -1:
#         answers[n] = fib(n - 1) + fib(n - 2)
#     return answers[n]
    
# for i in range(1, 10001):
#     print(i, ':', fib(i))
