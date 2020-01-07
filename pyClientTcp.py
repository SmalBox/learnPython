# pyClientTcp

'pyClient'

__author__ = 'SmalBox'

import socket

# 创建ipv4，tcp协议socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务器
s.connect(('127.0.0.1', 9999))