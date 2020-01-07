# pyServer

'pyServer'

__author__ = 'SmalBox'

import socket
import threading
import time

# 创建ipv4，tcp协议socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connection...')

# 定义要处理的过程
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send((('Hello, %s!' % data.decode('utf-8')).encode('utf-8')))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

# 循环等待连接，accept()会等待并返回一个Client连接
while True:
    # 接受一个连接
    sock, addr = s.accept()
    # 创建新线程处理tcp连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

