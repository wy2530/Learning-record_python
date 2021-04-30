import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.bind(("127.0.0.1",8080))

phone.listen(5)

# 等待
conn,client_addr=phone.accept()
print("客户端的信息:",client_addr)
# 接收
data=conn.recv(1024)
print("客户端发来的消息:",data.decode('utf-8'))
data=conn.send(data.upper())


conn.close()



