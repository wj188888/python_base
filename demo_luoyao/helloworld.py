# -*- coding: utf-8 -*-
import json

# 字符串
test = "骆瑶 你好啊!"
test1 = "niasdainia"
# temp = test+test1
int1 = 2022

def function():
    print("helloworld")
    x = 2018
    y = -9882
    z = x + y
    return z

class Building_blocks():
    def __init__(self):
        # 积木的长度
        self.length = 100
        # 单行注释
        '''
            多行注释:
            你我爱上打算打法
            发生打撒是发是否撒
            发撒是的公司法撒
        '''
        # 积木的形状
        self.rectangle = 1
        self.square = 2
        # 积木的颜色
        self.color = "黑色"
        # 积木的材质
        self.material = "wood"

    def function1(self):
        '''
        这个函数
        :return:
        '''
        self.material = "Iron and steel"
        self.color = "red"
        self.square = 10

if __name__ == '__main__':
    # build_block = Building_blocks()
    # print(build_block.color)
    # print(build_block.square)
    # print(build_block.material)

    build_block2 = Building_blocks()

    print(f'实例化对象2未加工前材质状态:{build_block2.material}')

    build_block2.function1()
    print(f'实例化对象2加工后材质状态:{build_block2.material}')