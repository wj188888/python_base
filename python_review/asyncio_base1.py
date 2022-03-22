# -*- coding:utf-8 -*-

# asyncio是单线程单进程的程序，然后本质上是event loop
# 同时执行的任务只能有一个，他不存在在系统级的上下文切换
# 不存在竞争冒险这样的问题
# 先理解coroutine 和 task

import asyncio

async def main():
    """ 返回的是一个coroutine（object）对象"""
    print("hello")
    await asyncio.sleep(1)
    print("world")

coro = main()

# 将synchronize切换到asynchronize模式
asyncio.run(coro)

# 将coroutine 变成task进入队列,然后执行