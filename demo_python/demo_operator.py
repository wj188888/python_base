# -*- coding: utf-8 -*-

from functools import reduce

def fact(n):
    '''
    匿名函数
    :param n:
    :return:
    '''
    return reduce(lambda a,b: a*b, range(1, n+1))

from operator import mul
def fact2(n):
    '''
    匿名函数
    :param n:
    :return:
    '''
    return reduce(mul, range(1, n+1))

if __name__ == '__main__':
    print(fact(10))
    print(fact2(10))