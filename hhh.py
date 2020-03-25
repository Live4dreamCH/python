# def fib(n):
#     if n <= 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
    
# for i in range(1, 1001):
#     print(i, ':', fib(i))

answers = [-1 for i in range(10005)]
answers[1] = 1
answers[2] = 1

def fib(n):
    if answers[n] == -1:
        answers[n] = fib(n - 1) + fib(n - 2)
    return answers[n]
    
for i in range(1, 10001):
    print(i, ':', fib(i))
