# encoding:utf-8
# 事件循环+回调(驱动生成器)+epoll（I/O多路复用）
# asyncio是python用于解决异步io编程的一整套解决方案
# 用于tornado丶gevent丶twisted丶
# tornado,实现了web服务器;django+flask(uwsgi, gunicorn+nginx)
# tornado可以直接部署，nginx+tornado

# 使用asyncio
# import asyncio
# import time
#
#
# async def get_html(url):
#     print("start get url")
#     # 不能使用我们的io，，time。sleep
#     await asyncio.sleep(2)
#     print("end get url")
#
# if __name__ == '__main__':
#     # s事件循环
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     tasks = [get_html("http://www.baidu.com") for i in range(100)]
#     loop.run_until_complete(asyncio.wait(tasks))
#     print(time.time() - start_time)

# 获取协程的换回执
# import asyncio
# import time
# from functools import partial   # 把函数包装成另一个函数
#
# async def get_html(url):
#     print("start get url")
#     # 不能使用我们的io，，time。sleep
#     await asyncio.sleep(2)
#     print("end get url")
#
# def callback(url, future):
#     print(url)
#     print("send email booby")
#
#
# if __name__ == '__main__':
#     # s事件循环
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     # get_future = asyncio.ensure_future(get_html("http://www.baidu.com") for i in range(100))
#     # loop.create_task()与asyncio.ensure_future()等效
#     task = loop.create_task(get_html("http://www.baidu.com"))
#     task = task.add_done_callback(partial(callback, "http://www.baidu.com")) # partial返回一个函数不是掉用
#     loop.run_until_complete(task) # run_until_complete能接受喝多方式,task
#     print(task.result())  # task.result()


# await和gather的区别
import asyncio
import time


async def get_html(url):
    print("start get url")
    # 不能使用我们的io，，time。sleep
    await asyncio.sleep(2)
    print("end get url")

if __name__ == '__main__':
    # s事件循环
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html("http://www.baidu.com") for i in range(100)]
    loop.run_until_complete(asyncio.gather(*tasks))
    print(time.time() - start_time)

    # gather和await的区别
    # gather更加高层hight-level,比如对task进行分组
    group1 = [get_html("http://www.baidu.com") for i in range(100)]
    group2 = [get_html("http://www.baidu.com") for i in range(100)]
    # loop.run_until_complete(asyncio.gather(*group1, *group2)) # 和下边三句是一样的我
    group1 = asyncio.gather(*group1)
    group1 = asyncio.gather(*group2)
    loop.run_until_complete(asyncio.gather(group1, group2))

    print(time.time() - start_time)