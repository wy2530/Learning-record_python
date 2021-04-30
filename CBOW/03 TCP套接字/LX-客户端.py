import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.connect(("127.0.0.1",8080))

data=phone.send("Hello world, 你好".encode('utf-8'))

phone.close()