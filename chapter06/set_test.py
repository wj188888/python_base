# -- coding:utf-8 --
# set集合 fronzenset(不可变集合),无序，不重复

enter = '\n'
s = set('abcdef')
# s = set(['a', 'b', 'c', 'd', 'e'])
s = set({'a', 'b', 'c', 'd', 'e', 'f'})
print(f's:{enter}{s}')
s.add('ssx')


# frozenset 可以作为dict的key
k = frozenset({'a', 'b', 'c', 'd', 'e', 'f'})
print(f'k:{enter}{k}')

# 向set添加数据
# xx = set.add('xx')

# difference
another_set = set('def')
res_set = s.difference(another_set)
print(res_set)

print(s-another_set)

others = set({"wangji", "fadasd", "name"})
res_setaz = others.difference(s)
print(res_setaz)


# set集合运算，/ & * + -等操作;时间复杂度是1，是哈希查询

re_set = s & another_set
print(re_set)

# 判断是否在集合中
if "c" in re_set:
    print("i am in set")
else:
    print("不在")