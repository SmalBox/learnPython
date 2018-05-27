#斐波那契数列（Fibonacci）
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b #等同以下写法
        #t = (b, a + b)
        #a = t[0]
        #b = t[1]
        n = n + 1
    return 'done'
