#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/12 18:50
# @Author  : wangjie
# @Software: PyCharm

def for_else_test():
    '''测试for...else...意思是，for运行完成后运行else'''
    list = [1,2,3,4,5]
    for i in list:
        if i%2==0:
            print(i)
        # else:
        #     break
    else:
        # 如果上边的for正常执行完成，else就会执行，否则else是不执行的
        print("执行for了else")


def while_else_test():
    '''测试while...else...意思是，while条件为假退出时执行else'''
    active_flag = True
    list = {
        'name': 'zhangsan',
        'age': 20,
        'score': 90
    }
    while active_flag:
        if list.get('name')=='zhangsan':
            # active_flag = False
            print('张三来了，大家快跑！！！')
    else:
        print("我晓得张三来了，并且执行了else语句~")

def try_else_test():
    '''测试try...else...意思是，try没有报错就执行else'''
    try:
        div = 1/1
        print(div)
    except Exception as _:
        print("抛出错误，并且不去执行else")
    else:
        print("true正常运行，没有遇到什么问题")


class LookingClass:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JKJKDSDASADQQDA'

    def reverse_write(self):
        return self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True


if __name__ == '__main__':
    # for_else_test()
    # while_else_test()
    try_else_test()
    with LookingClass() as fp:
        # TypeError: reverse_write() takes 1 positional argument but 2 were given?????
        print('Alice kitty and Snowdrop')
        print(fp)