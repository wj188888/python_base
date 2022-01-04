# -- coding:utf-8 --
#

# import threading
# import asyncio
# from asyncio import Lock
#
# total = 0
# async def add():
#     # dosomething
#     # io操作
#     global total
#     for i in range(1000000):
#         total += 1
#
# async def desc():
#     global total
#     for i in range(1000000):
#         total -= 1
#
# if __name__ == '__main__':
#     tasks = [add(), desc()]
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait(tasks))
#     print(total)
#     # 凡是不涉及I/O操作或是遇到yield操作的协程都可以不使用锁机制的


# 第二部分
import asyncio
from asyncio import Lock, Queue # Queue通信,多线程可能是阻塞的，不适合asyncio的实现
cache = {}

lock = Lock()

async def get_stuff(url):
    async with lock:
        if url in cache:
            return cache[url]
        # 课程老师没有讲这个，有个红线
        stuff = await aiohttp.request('get', url)
        cache[url] = stuff
        return stuff

async def parse_stuff():
    stuff = await get_stuff()
    # do something parsing

async def use_stuff():
    stuff = await get_stuff()
    # do any others something parsing