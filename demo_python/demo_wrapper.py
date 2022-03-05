# -*- coding: utf-8 -*-

'''
 装饰器基础知识:
    装饰器是可调用的对象,其参数是另一个函数(被装饰的安徽那书,)装饰其可能会处理被装饰u的函数
    ,然后把他返回,或者将其替换成另一个函数或不可调用对象
 装时期只是与发烫.如前所示,装饰器可以像常规的可调用对喜爱那个那样调用,其参数是另一个函数.
    元变成,可以在程序运行的时候改变程序的行为
    能把被装饰的函数替换成其他的函数.第二个特性是,装时器在加载模块是,立即执行;
'''

# registration.py

registry = []
def register(func):
    print('running register(%s)%func')
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')

def f2():
    print('running f2()')

def f3():
    print('running f3()')

def main():
    print('running main()')
    print('registry->', registry)
    f1()
    f2()
    f3()

b = 6
def func2(a):
    global b
    print(a)
    print(b)
    b=9
from dis import dis

if __name__ == '__main__':
    func2(3)
    print(dis(f1))