# -- coding:utf-8 --
# 实现属性可修改的函数装饰器
# 问题：在某项目中，程序运行效率差，为分析程序内哪些函数执行时间开销大，我
# 们实现一个带timeout参数的函数装饰器，装饰器功能如下：

# 解决方案：
# 为包裹函数增添一个函数，用来修改闭包中使用的自由变量，在python3中：
# 使用 nonlocal访问嵌套作用域中的变量引用

import time
import logging
import random

def warn_timeout(timeout):
    def decorator(func):
        def wrap(*args, **kwargs):
            t0 = time.time()
            res = func(*args, **kwargs)
            used = time.time() - t0
            if used > timeout:
                logging.warning(f'{func.__name__},{used},{timeout}')
            return res
        def set_timeout(new_timeout):
            nonlocal timeout
            timeout = new_timeout

        wrap.set_timeout = set_timeout
        return wrap
    return decorator

@warn_timeout(1.9)
def f(i):
    print(f'in f [{i}]')
    while random.randint(0, 1):
        time.sleep(0.6)

# for i in range(30):
#     f(i)

if __name__ == '__main__':
    f.set_timeout(12)
    for i in range(30):
        f(i)

# @warn_timeout(1.5)
# def func(a,b):
#     '''1.统计被装饰函数单词调用运行时间
#         2.时间大于参数timeout的，将此次函数调用记录到log日志中、
#         3.运行时可修改timeout的值
#         '''

# 在python2如何去做呢,利用列表的可变性去着力思考
# def decorator(func):
#     _timeout = [timeout]
#     def wrap(*args, **kwargs):
#         timeout = _timeout[0]
#     def set_timeout(new_timeout):
#         _timeout[0] = new_timeout

