# -- coding:utf-8 --
# 原函数
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count

# 预激协程的装饰器
from functools import wraps
def coroutine(func):
    '''装饰器：向前执行到第一个yield表达式，预激"func"'''
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count
# @coroutine == coroutine(averager)
if __name__ == '__main__':
    coro_avg = averager()
    print(coro_avg.send(10))
    print(coro_avg.send(30))
    print(coro_avg.send(5))
    print(coro_avg.send(1023))
    print(coro_avg.send(1092))
    print(coro_avg.send(634))

