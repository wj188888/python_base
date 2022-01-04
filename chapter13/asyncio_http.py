# -- coding:utf-8 --
# asyncio 没有提供http协议的接口（课程时候）
# 基于原生的asyncio进行

import asyncio
import socket

# urlparse是用于url解析的
from urllib.parse import urlparse

async def get_url(url): #首先设置成协程函数
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
    # 建立socket连接
    reader, writer = await asyncio.open_connection(host, port=80) # open_connnection是一个协程
    writer.write(f'GET {path} HTTP/1.1\r\nHost:{host}\r\nConnection:close\r\n\r\n'.encode("utf8"))
    all_lines = []
    async for raw_line in reader:
        data = raw_line.decode("utf8")
        all_lines.append(data)
    html = "\n".join(all_lines)
    return html

async def main():
    tasks = []
    for url in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        tasks.append(get_url(url))
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)

if __name__ == '__main__':
    import time
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # for task in tasks:
    #     print(task.result())
    print("last time: {}".format(time.time()-start_time))
