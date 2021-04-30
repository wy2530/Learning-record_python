import socket

server = socket.socket()  # TCP
server.bind(('127.0.0.1', 8081))
server.listen(5)

while True:
    conn, addr = server.accept()
    data = conn.recv(1024)
    # 需要忽略favicon.ico
    '''两个\r\n:
        响应头格式：HTTP/1.1 状态 \r\n
        空行：\r\n
    '''
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    print(data)  # 1、目前data是个二进制数据

    data = data.decode('utf-8')  # 2、转化成字符串
    # 因为是流式协议，所有这些写在哪都是一样的

    # 3、切片后端数据
    current_path = data.split(' ')[1]
    # 4、后缀是什么返回什么（有/）
    if current_path == '/index':
        conn.send(b'suffix is index')
    elif current_path == '/login':
        conn.send(b'suffix is login')
    elif current_path == '/files':
        with open(r'11  web\test_web.html', mode='rb') as f:
            conn.send(f.read())
    else:
        # 发送的数据格式应该是http格式的，才可以让浏览器访问
        conn.send(b'hello web')
    conn.close()
