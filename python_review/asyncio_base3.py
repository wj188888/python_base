# -*- coding:utf-8 -*-
import asyncio
import time

async def say_after(delay, what):
    """返回一个coroutine对象"""
    await asyncio.sleep(delay)
    return f"{what} - {delay}"

async def main():
    print(f"started at {time.strftime('%X')}")
    task1 = asyncio.create_task(
        say_after(1, "hello")
    )
    task2 = asyncio.create_task(
        say_after(2, "world")
    )
    print(f"finished at {time.strftime('%X')}")
    # 去拿coroutine返回的值
    res1 = await task1
    res2 = await task2

    print(res1)
    print(res2)

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())