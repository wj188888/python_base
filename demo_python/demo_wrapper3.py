# -*- coding: utf-8 -*-

import time
import functools

'''
    优化demo_wrapper2.py后,@functools.wraps(func)
'''

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_str = ','.join(repr(arg) for arg in args)
        if kwargs:
            pairs = ['%s=%r'%(k, w) for k,w in sorted(kwargs.items())]
            arg_lst.append(','.join(pairs))
        arg_str = ','.join(arg_lst)
        print('[%0.8fs]%s(%s)->%r'%(elapsed, name, arg_str,result))
        return result
    return clocked

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)
'''
    python内置了三个用于装饰方法的函数:property丶classmethod丶staticmethod
    
    functools.wraps是为了协助构建行为良好的装饰器
    
    functools.lru_cache是非常使用的装饰器,它实现了备忘的功能,这是一项优化技术,避免传入相同的参数时候重复计算
    
    
    
    
'''

# functools.lru_cache运用,减少了重复的运算
@functools.lru_cache
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)



if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6!=',factorial(6))

    # functools.lru_cache运用
    print(fibonacci(6))
