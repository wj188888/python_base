# -- coding:utf-8 --
my_list = []
my_list.append(1)
my_list.append("a")

# 容器相关的数据结构的抽象基类都放在collections中的

from collections import abc

# 列表相加
a = [1,2]
c = a + [3,5]
print(c)

# 就地加,+=后可以为任意对象的,调用了__iadd__，还是extend,只要是可迭代的都是可以加上去
a += (3,5)
print(a)

a.extend(range(3))

# append是吧[1,2]这个数组当成一个值，不是作为可迭代对象
a.append([1,2])