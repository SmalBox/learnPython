#쳲��������У�Fibonacci��
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b #��ͬ����д��
        #t = (b, a + b)
        #a = t[0]
        #b = t[1]
        n = n + 1
    return 'done'
