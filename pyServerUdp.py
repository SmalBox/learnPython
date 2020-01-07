# pyServerUdp

'pySerUdp'

__author__ = 'SmalBox'

import socket
import threading

# 创建ipv4，udp的socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')

# 定义要处理的过程
def udplink(sock, data, addr):
    print('Received from %s:%s.' % addr)
    sock.sendto(b'Hello, %s!' % data, addr)

# 循环等待，recvfrom()返回数据和客户端地址与端口
while True:
    # 接收数据
    data, addr = s.recvfrom(1024)
    # 创建新线程处理udp
    t = threading.Thread(target=udplink, args=(s, data, addr))
    t.start()