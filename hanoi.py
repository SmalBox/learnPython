print('汉诺塔（Hanoi）')
n = input('请输入盘子数：')
A = input('请输入第一个柱子名称：')
B = input('请输入第二个柱子名称：')
C = input('请输入第三个柱子名称：')
X = []
def move(n, a, b, c):
    if n == 1:
        step = a + str(n) + '-->' + c + str(n)
        X.append(step)
        return
    move(n-1, a, c, b)
    step = a + str(n) + '-->' + c + str(n)
    X.append(step)
    #move(1, a, b, c)   
    move(n-1, b, a, c)

move(int(n), str(A), str(B), str(C))
print('共需操作'+str(len(X))+'次\n操作过程为\n',X)
