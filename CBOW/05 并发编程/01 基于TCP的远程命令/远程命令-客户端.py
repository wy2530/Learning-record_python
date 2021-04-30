"""
会有粘包问题：也就是客户端接收的字节不够，一次 取 1024 个字节，剩下的命令仍然在缓存区
            你下一次输入命令时，它会将第一次命令剩下结果的取出来
粘包问题出现的原因：
    1、tcp是流式协议，数据流像水流一样，没有任何边界区分
    2、收数据没收干净，有残留，就会和下一次混淆在一起
解决办法：(收干净)recv不能无限增大，因为有缓冲区的内存大小限制
    1、先拿到数据的总大小total_size
    2、recv_size=0,循环接收，recv_size+=接收的长度（...最后一次长度不一样怎么办）
    3、直到recv_size=total_size，结束循环

TCP才会有粘包问题，UDP不会，因为UDP是不可靠传输，收不完直接扔掉
UDP每一个都是一一对应的
"""

from socket import *

client = socket(AF_INET, SOCK_STREAM)

client.connect(('127.0.0.1', 8080))

while True:
    msg = input('请输入命令：').strip()
    if len(msg) == 0:
        continue
    client.send(msg.encode('utf-8'))
    # 这里的字节数很有可能导致字节接收不全的问题，在第二个命令时，他会接着输出
    cmd_res = client.recv(1024)
    print(cmd_res.decode('gbk'))  # 这里是命令行的解码方式，linux系统是utf-8，win是gbk
