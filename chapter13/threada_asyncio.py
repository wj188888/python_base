# -- coding:utf-8 --
# 使用多线程:在协程中集成阻塞i/o
import asyncio
import socket
from concurrent.futures import ThreadPoolExecutor
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
    # 协程新增,设置为非阻塞或是非阻塞的一个操作
    # client.setblocking(False)

    client.connect((host, 80))  # 阻塞不消耗cpu

    # 不停的询问连接是否建立好，需要while循环不停的去检查状态
    # 做计算任务或再次发起其他的连接请求
    # 非阻塞式I/O，把时间消耗在系统调用状态维护上,比较耗cpu
    # I/O复用，select(应用程序)也是阻塞的，但是他是批量处理的,同时监听多个

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
    import time
    start_time = time.time()
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor() #可以给线程池给
    tasks = []
    for url in range(20):
        task = loop.run_in_executor(executor, get_url, "http://imooc.com")
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    print("last time :{}".format(time.time() - start_time))