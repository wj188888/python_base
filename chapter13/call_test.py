# -- coding:utf-8 --
import asyncio

def callback(sleep_times):
    print("success time {}".format(loop.time))

def stoploop(loop):
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    now = loop.time()
    loop.call_at(now+2, callback, 2, loop)
    loop.call_at(now+1, callback, 1, loop)
    loop.call_at(now+3, callback, 3, loop)

    # loop.call_later(2,callback,2)   # 根据延迟调用使用去按顺序执行
    # loop.call_later(1,callback,1)
    # loop.call_later(3,callback,3)
    # loop.call_later(2,stoploop, loop)
    loop.call_soon(callback, 4) # 立马执行，
    loop.run_forever()