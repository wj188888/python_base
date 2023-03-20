#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/11 10:21
# @Author  : wangjie
# @Software: PyCharm

from collections import namedtuple, OrderedDict
# 导入具名元祖包

Rectangle = namedtuple('Rectangle', 'width,height')

rect = Rectangle(100,20)
print("width: " + str(rect.width))
print("height: " + str(rect.height))


movie = {'name': 'Buring', 'type': 'movie', 'year': 2018}
print(movie['year'])

d = OrderedDict()
d['First_key'] = 1
d['two_key'] = 2
for key in d.keys():
    print(key)

for value in d.values():
    print(value)