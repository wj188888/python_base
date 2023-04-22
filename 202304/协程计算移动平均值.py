#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2023/4/22 23:02
# @Author: WangJie
# @Description:
import inspect


def avrager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average #yield放在表达式的右边就是协程的使用方式
        total += term
        count += 1
        average = total/count

def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)

def simple_coro2(a):
    print('-> started: a =',a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a+b
    print('-> Received: c =', c)


if __name__ == '__main__':
    sim = simple_coro2(12)
    print(inspect.getgeneratorstate(sim)) #查看协程当前的状态
    next(sim)#预激协程，启动协程的意思
    print(inspect.getgeneratorstate(sim))

    # print(sim.send(10))
    print(sim.send(20))
    print(inspect.getgeneratorstate(sim))


