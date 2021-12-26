import socket
import threading

# 这个定义的socket 是用来监听的
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))  # 绑定ip和端口
server.listen()


def handle_sock(sock, addr):
    data = sock.recv(1024)  # 单位是字节
    data = data.decode("utf8")
    re_data = input()
    sock.send(re_data.encode("utf8"))



# 从客户端发送的数据，一次获取1k的数据
while True:

    # 全局的设定，而这个sock是用户用来发送数据的,因为要进行多个连接socket，所以要加入线程
    sock, addr = server.accept()

    # 用线程去处理新接受的连接（用户）
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))  # 这里只传函数名称，不调用
    client_thread.start()


    # data = sock.recv(1024)   # 单位是字节
    # data = data.decode("utf8")
    # print(data)
    # re_data = input()
    # sock.send(re_data.encode("utf8"))
    # sock.send(f"hello {data}".encode("utf8"))
    # server.close()
    # sock.close()