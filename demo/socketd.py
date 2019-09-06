#coding=utf-8

import socket
# 参数 AF_INET网络模式，AF_UNIX文件模式
# 参数 SOCK_STREAM tcp/ip SOCK_DGRAM udp
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9001)) #设置地址和端口
s.listen(9) #设置最大请求处理数
while 1:
    connection,address = s.accept()
    buf = connection.recv(1024)
    connection.send(buf)
s.close()