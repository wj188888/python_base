#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/13 20:49
# @Author  : wangjie
# @Software: PyCharm


"""
常见的时间表示：
    1.时间戳(timestamp)
    2.结构化时间（struct time）
    3.格式化的时间字符串
"""
import copy
import time

# print(time.time()) # 获取时间戳，单位是秒
# print(time.localtime()) # 结构化时间
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) ) # 格式化时间

tup1 = ('张山', '李四', '王五')
tup2 = ('张山', '李四', '王五', 123,322,192, True)
# 元祖
print(tup1.__hash__())
print(tup2.__hash__())
if tup1.__eq__(tup2):
    print("tup1和tup2是同一个对象")
else:
    print("tup1和tup2不是同一个对象")

# 列表浅拷贝的学习
lit1 = [1,2,3,4,5]
# print(lit1)
print(lit1[2:: 2])
lit2 = lit1.copy()
print(lit2)
if lit1.__eq__(lit2):
    print("lit2浅拷贝lit1相等，标签指向的同一个引用")
else:
    print("lit2浅拷贝lit1相等，标签指向的不是同一个引用")

# 深拷贝的学习
deeplit2 = copy.deepcopy(lit2)
print(deeplit2.__len__())
print(len(lit2))
if deeplit2.__eq__(lit2):
    print("deeplit2深拷贝lit2相同，便签指向的是同一个引用")
else:
    print("deeplit2深拷贝lit2不同，标签指向的不是同一个引用")
deeplit2.append(32)
print(deeplit2)
print(lit2)
if deeplit2.__eq__(lit2):
    print("deeplit2深拷贝lit2相同，便签指向的是同一个引用")
else:
    print("deeplit2深拷贝lit2不同，标签指向的不是同一个引用")
# 修改深拷贝的列表数据时，不在影响浅拷贝的内容了


try:
    # 删除元祖的操作，直接del 元祖名称
    del deeplit2
    if deeplit2 is None:
        print("成功删除deeplit2")
    else:
        print("没有被删除成功")
except NameError as e:
    print(e)
# print(deeplit2)


dict1 = {
    'name': 'wangjie',
    'age': 19
}
# print(dict1)
