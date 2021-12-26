# 什么是迭代协议
# 迭代器是什么？   迭代器是访问集合内元素的一种方式，一般永安里遍历数据迭代器是访问集合内元素的一种方式，一般永安里遍历数据
# 迭代器和以下标的访问方式不一样， 迭代器是不能返回的， 迭代器提供了一种惰性方式数据的方式

# [] list,有魔法函数__iter__都是符合迭代协议的


from collections.abc import Iterator, Iterable

a = [1,2]
v = [x * x * x for x in a]
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))

print(isinstance(v, Iterable))
print(isinstance(v, Iterator))
print(v)
iter_rator = iter(a)
print(isinstance(iter_rator, Iterator))