#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2023/3/23 20:05
# @Author: WangJie
# @Description:

import socket

host_name = socket.gethostname()
print("IP address:" + host_name)
#查看fqdn
print(socket.getfqdn())
#获取名字详情
print(socket.getnameinfo)
# 获取服务器名称
print(socket.getservbyname)
# 获取服务器的端口号
print(socket.getservbyport)

#hexlify函数的作用是将十六进制切换成二进制的对象
from binascii import hexlify

def convert_ip4_address():
    #定义两个ip地址
    for ip_addr in ['127.0.0.1', '192.168.0.1']:
        packed_ip_addr = socket.inet_aton(ip_addr) #转成32bit的数据
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr) #转成ip地址字符串
        print(f"IP Address: {ip_addr} => Packed: {hexlify(packed_ip_addr)}, Unpacked_ip_addr: {unpacked_ip_addr}")

def find_service_name():
    prototocolname = 'tcp'
    for port in [80, 25]:
        print(f"Port: {port} ==> service name: {socket.getservbyport(port, prototocolname)}")
    print(f"Port: {53} => service name: {socket.getservbyport(53, 'udp')}")

def convert_integer():
    #定义一个字符串
    data = 1234
    # 32-bit
    print(f"Original: {data} => Long host byte order {socket.ntohl(data)}, Network byte order: {socket.htonl(data)}")
    # 16-bit
    print(f"Original: {data} => Short host byte order {socket.ntohs(data)}, Network byte order: {socket.htons(data)}")

def socket_timeout():
    #测试超时时间，用于开发服务器时有用
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Default socket timeout: {s.gettimeout()}") #没有默认超时时间
    s.settimeout(100)
    print(f"Current socket timeout: {s.gettimeout()}") #默认超时时间

if __name__ == '__main__':
    socket_timeout()

