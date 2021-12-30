# -- coding:utf-8 --
# 1.epoll并不代表一定比select好
# 并发性不高， 同时连接很活跃，select比epol好

#  通过非阻塞I/O实现http请求

# requests -> urlib -> socket
import socket
# urlparse是用于url解析的
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE   # 这种通常使用的更多

# 使用select完成http请求
# select.select()
'''select + 回调 + 事件循环'''
# 并发性高
# 使用单线程

urls = ["http://www.baidu.com"]
selector = DefaultSelector()
stop = False

class Fetcher:
    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send(f'GET {self.path} HTTP/1.1\r\nHost:{self.host}\r\nConnection:close\r\n\r\n'.encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
        if not urls:
            global stop
            stop = True

    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/"
        # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置为非阻塞的I/O
        self.client.setblocking(False)
        try:
            self.client.connect((self.host, 80))
        except BlockingIOError as e:
            pass
        # 注册
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)
# 回调自己的事
def loop():
    # 事件循环，不停的请求socket的状态并调用对应的回调函数
    '''select本身是不支持register模式'''
    # 2.socket状态变化后的回调是由程序员自己完成
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)
        # 回调+事件循环+select（poll\epoll）

if __name__ == '__main__':
    fetcher = Fetcher()
    fetcher.get_url("http://www.baidu.com")
    loop()

