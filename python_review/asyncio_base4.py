# -*- coding:utf-8 -*-

import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    return f"{what} - {delay}"

async def main():
    # task1 = asyncio.create_task(
    #     say_after(1, "hello")
    # )
    # task2 = asyncio.create_task(
    #     say_after(2, "world")
    # )
    # 这段代码的灵魂
    # ret = await asyncio.gather(task1, task2) # 这段代码等于25-29代码



    print(f"started at {time.strftime('%X')}")

    # 也可以这样写：
    rert = await asyncio.gather(
        # gather自动把coroutine变成task
        say_after(1, "hello"),
        say_after(2, "world")
        )

    print(rert)

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())