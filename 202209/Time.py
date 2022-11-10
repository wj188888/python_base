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
import time

print(time.time()) # 获取时间戳，单位是秒
print(time.localtime()) # 结构化时间
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) ) # 格式化时间