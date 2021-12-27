# requests -> urlib -> socket
import socket

# urlparse是用于url解析的
from urllib.parse import urlparse

def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))

    client.send(f'GET {path} HTTP/1.1\r\nHost:{host}\r\nConnection:close\r\n\r\n'.encode("utf8"))
    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode("utf8")
    print(data)
    # html_data = data.split("\r\n\r\n")[1]
    # print(html_data)
    client.close()

if __name__ == '__main__':
    get_url("http://www.baidu.com")