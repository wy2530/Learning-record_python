'''
服务端应该满足两个特点：
    1、一直对外服务
    2、并发地服务多个客户端
'''

import subprocess  # 这个模块可以输出命令的结果,但是有对的有错的
from socket import *

server = socket(AF_INET, SOCK_STREAM)

server.bind(('127.0.0.1', 8080))

server.listen(5)

'''
conn是建好的（某一个）连接，client_addr是客户端的IP和端口

服务端应该做两件事：
1、循环从半连接池中取出链接请求与其建立双向链接，拿到连接对象
'''
while True:
    conn, client_addr = server.accept()

    # 2、拿到链接对象，与其进行通信循环
    while True:
        try:
            # 这里的字节，是接收的命令，很少有超过1024的，够用，但是客户端返回结果极有可能不够
            cmd = conn.recv(1024)

            if len(cmd) == 0:
                break
            obj = subprocess.Popen(cmd.decode('utf-8'),
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE
                                   )
            # 这里得到的字符串有编码格式的区别了
            # #####   底层编码再看一下
            stdout_res = obj.stdout.read()
            stderr_res = obj.stderr.read()
            total_size = len(stdout_res) + len(stderr_res)
            print(total_size)
            conn.send(stdout_res + stderr_res)  # 字符串拼接发出
        except Exception:
            break
    conn.close()
