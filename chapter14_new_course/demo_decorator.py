# -- coding:utf-8 --
# 某些时候我们想为多个函数，同一添加某种功能，比如即时统计
# 记录日志，缓存运算结果等等。
# cache = {}
# def fibonacci(n):
#     res = cache.get(n)
#     if res:
#         return res
#     if n <= 1:
#         return 1
#     res = cache[n] = fibonacci(n-1) + fibonacci(n-2)
#     return res
#
# if __name__ == '__main__':
#     print(fibonacci(100))

# 第二部分===============

def memo(func):
    '''首先定义的一个函数，然后这函数传入的是func方法，定义一个缓存，
        我们吧输入的参数定义成一个可变序列元祖，
    '''
    cache = {}
    def wrap(*args, **kwargs):
        res = cache.get(args)
        if not res:
            res = cache[args] = func(*args)
        return res
    return wrap

# 给这个函数加上memo装饰器
@memo
def fibonacci(n):
    if n <= 1:
        return 1
    res = fibonacci(n-1) + fibonacci(n-2)
    return res

# 给这个函数加上memo装饰器
@memo
def climb(n, steps):
    count = 0
    if n==0:
        count = 1
    elif n > 0:
        for step in steps:
            count += climb(n-step, steps)
    return count


# fibonacci = memo(fibonacci) # 等价于在fibonacci函数上添加一个@memo
# climb = memo(climb)

# a: int是参数注释，func() -> int:是函数的注释
def func(a: int, b: int) -> int:
    return a + b
from random import randint

def func2(a, b=1, c =[]):
    pass

def f(a):
    return lambda n: a**n
g =f(3)
print(g(10))
print(g.__call__)
print(g.__closure__)    # 判断闭包，是：返回cell，否，返回None

if __name__ == '__main__':
    # 解决方案：
    # 定义装饰函数用它来生成一个在原函数基础添加了新功能的函数，替代原函数
    print(fibonacci(10))
    print(climb(10, (1, 2, 3)))
    ''':cvar
        函数元数据，如果一个函数被装饰器装饰后，无法访问该函数的元数据，如果解决
    '''
    print(func.__name__)
    print(func.__module__)
    print(randint.__module__)
    print(func(1, 2))
