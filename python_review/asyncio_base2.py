# -*- coding:utf-8 -*-
import asyncio
import time

async def say_after(delay, what):
    """返回一个coroutine对象"""
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")
    # 第一步：将这个coroutine包装成一个task
    await say_after(1, "hello")
    await say_after(2, "world")

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())