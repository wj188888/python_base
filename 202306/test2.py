# -*- coding: utf-8 -*-
# @Author: jie wang
# @Date: 2023/6/2 21:55

#练习递归函数

#用递归来求阶乘
def func(num):
    if num == 1:
        return 1
    return func(num-1)*num

#上面的函数如果n的数字过大的话就会出现栈溢出的问题，这是我们需要通过尾递归来优化
def fact(num, product=1):
    if num == 1:
        return product
    return fact(num-1, num*product)

if __name__ == '__main__':
    num = 500
    n = fact(num)
    print('%d的阶乘是' % (num,), n)