# encoding:utf-8
# 实现一个能将函数调用信息记录到日志的装饰器
# 1.把每次函数的调用时间，执行时间，调用次数写入日志
# 2.可以对被装饰器函数分组，调用信息记录到不同的日志
# 3.动态修改参数，比如日志格式
# 4.动态打开关闭日志输出功能

# 比如
# @call_info(arg1, arg2, arg3)
# def func(a, b):
#     pass

import time
import logging

DEFAULT_FORMAT = '%(func_name)s -> %(call_time)s\t%(used_time)s\t%(call_n)s'

class CallInfo:
    def __init__(self, log_path, format_=DEFAULT_FORMAT, on_off=True):
        # 给getLogger不同的对象，会得到不同的log名
        self.log = logging.getLogger(log_path)
        self.log.addHandler(logging.FileHandler(log_path))
        self.log.setLevel(logging.INFO)
        self.format = format_
        self.is_on = on_off

    # 装饰器方法
    def info(self, func):
        _call_n = 0
        def wrap(*args, **kwargs):
            func_name = func.__name__
            call_time = time.strftime('%x %X',time.localtime())
            t0 = time.time()
            res = func(*args, **kwargs)
            used_time = time.time() - t0
            nonlocal _call_n
            _call_n += 1
            call_n = _call_n
            if self.is_on:
                info_dict = {'call_time': call_time}
                self.log.info(self.format % locals())
            return res
        return wrap

    def set_format(self, format_):
        self.format = format_

    def turn_on_off(self, on_off):
        self.is_on = on_off

# 测试代码


def demo_01():
    x = 1
    y = [1,2,3]
    z = 'wangjie'
    print(locals())

if __name__ == '__main__':
    '''
        为了让装饰器在使用上更加灵活，可以把类的实例方法作为装饰器，此时在包裹函数中就可以
        持有实例对象，便于修改属性和拓展功能. 
    '''
    import random

    ci1 = CallInfo('./mylog1.log')
    ci2 = CallInfo('./mylog2.log')


    @ci1.info
    def f():
        sleep_time = random.randint(0, 6) * 0.1
        time.sleep(sleep_time)
    @ci1.info
    def g():
        sleep_time = random.randint(0, 8) * 0.1
        time.sleep(sleep_time)
    @ci2.info
    def h():
        sleep_time = random.randint(0, 7) * 0.1
        time.sleep(sleep_time)

    # 从新设置打印日志的内容
    # ci1.set_format('%(func_name)s -> %(call_time)s\t%(call_n)s')
    for _ in range(30):
        # 从其中随机选一个运行
        random.choice([f, g, h])()

