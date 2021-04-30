from socket import *
import struct

client = socket(AF_INET, SOCK_STREAM)

client.connect(('127.0.0.1', 8080))

while True:
    msg = input('请输入命令：').strip()
    if len(msg) == 0:
        continue
    client.send(msg.encode('utf-8'))

    header = client.recv(4)
    total_size = struct.unpack('i', header)[0]  # 从header中拿到需要的信息,因为是元组
    # print(total_size[0])
    # total_size=1202
    recv_res = 0

    while recv_res < total_size:
        # 这里的字节数很有可能导致字节接收不全的问题，在第二个命令时，他会接着输出
        res = client.recv(1024)
        recv_res += len(res)
        print(res.decode('gbk'),end='')  # 这里是命令行的解码方式，linux系统是utf-8，win是gbk
