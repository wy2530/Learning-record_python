import socket


# 1、买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 2、拨通服务端电话（建立请求）
'''
客户端要连接的是服务端，所以写的是服务端的IP和端口
'''
phone.connect(("127.0.0.1",8080))
# 3、通信
'''
服务端在监听，客户端需要发送消息
字符串什么的需要转成bytes类型
'''
while True:
    msg=input("请输入信息：").strip()  # 去空格
    if len(msg)==0:continue
    phone.send(msg.encode('utf-8'))

    # 3.1 客户端也可以接受来自服务端返回的消息
    data=phone.recv(1024)
    print(data.decode('utf-8'))

# 4、关闭连接(一定要写的)
phone.close()
