import socket

# 1、买手机
'''
类实例化 socket.AF_INET（地址家族），  SOCK_STREAM流式协议==》TCP协议
'''
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2、绑定手机卡 (服务端机器的IP地址，端口地址)
'''
ip+port才可以唯一确定一个机器的那个应用程序（网络层有ARP协议，mac地址可知）
关于IP地址:
    如果你使用的是私网的IP地址，那么在同一个局域网内的机器都可以使用发包
    如果你使用的是公网的IP地址，类似于多个局域网之间可以互相通信
    因此建议：
        在开发测试时，使用本地回环地址，127.0.0.1，意思是客户端和服务端都只有自己能访问
        在上线时，在放入公网
    4个局域网
关于端口地址：
    0-65535，1024之前的都被系统保留使用


'''
phone.bind(("127.0.0.1", 8080))

# 3、开机(监听)
phone.listen(5)  # 5指的是半连接池的大小

# 4、等待电话连接请求(三次握手的双向通路，客户端IP)
'''
conn是电话连接,那个三次握手的信息
'''
conn, client_addr = phone.accept()  # 接受请求
print(conn)
print("客户端的IP和端口：", client_addr)

# 5、通信
'''
建立通路之后，客服端先给服务端发消息（规则可改）
'''
# 5.1 收消息
'''
recv接收字节过大没有意义了：
    1、recv的接收字节数是一次接收的量，在TCP协议中客户端的数据可能很大，但不会一次性的发给服务端的
    2、接收的字节数受限于内存大小
'''
while True:
    try:
        data = conn.recv(1024)  # 最大接收量为1024个字节（Bytes）,如果没有收到数据就会一直等着
        # '''
        # 1、 在Unix系统中，一旦Data收到的是空，为客户端异常终止，服务端会不断循环
        # 2、在win系统中，客户端异常终止时，服务端也会出现异常
        # '''
        # if len(data)==0:
        #     break
        print("客户端发来的消息：", data.decode('utf-8'))
        # 5.2 发消息
        data = conn.send(data.upper())
    except Exception:
        break
# 6、关闭电话连接
conn.close()

# 7、关机(关闭服务端,基本可以不用)
# phone.close()

'''
服务端会有两个明显堵塞点，也可以说是等待点，accept,recv
'''

'''
如何将本地文件放入阿里云服务器
https://m.imooc.com/wenda/detail/427853
'''
