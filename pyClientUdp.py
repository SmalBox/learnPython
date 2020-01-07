# pyClientUdp

'pyClientUdp'

__author__ = 'SmalBox'

import socket

# 创建ipv4，udp的socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 用s.sendto(data, ('127.0.0.1', 9999))发送数据