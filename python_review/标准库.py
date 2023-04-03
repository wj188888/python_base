#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2023/3/22 20:07
# @Author: WangJie
# @Description: 字典排序操作


from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['name']='zhangshan'
favorite_languages['age']="21"
favorite_languages['type']="True"
favorite_languages['point']="A-B-C"

# 查看迭代出来的内容是否是按顺序的
for key, values in favorite_languages.items():
    print(key.title() + "对应的values是: " + values.title() + '.')

file_name = r'data/data.txt'
with open(file_name) as fp:
    for line in fp:
        if line is '\n': # 如果是换行符就直接跳到下一个
            continue
        else:
            print(line.rstrip())

#打印出来看下这个读取的行是什么呀
with open(file_name) as f:
    lines = f.readlines()
    print(lines)
