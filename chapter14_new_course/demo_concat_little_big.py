# -- coding:utf-8 --
# 如何将多个字符串拼接成一个大的字符串
# 目的将多个字符串，连接起来然后，拼接成一个包，长得字符串
# 方法一：迭代列表，连续使用‘+’
# 方法二：使用str.join()方法，更加快速的拼接列表
from timeit import timeit

s1 = 'abcdef'
s2 = '12345'
s3 = s1 + s2
print(s3)
print(type(s1))
print(type(s2))
s4=s1.__add__(s2)
print(s4)
l = ["<1002>", "<2322>", "<2x013>","60", "<1>", "<100.0>", "<500.0>"]
s = ''
for x in l:
    # 这样的加法，存在严重的浪费
    s += x
print(s.__repr__())

from functools import reduce

l2 = ['abv', 'fs', 'fasdas']
print(''.join(l2))
print(''.join(l))

# 如何测试一条语句执行的时间
timeit(''.join(l))
