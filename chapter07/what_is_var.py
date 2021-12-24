# -- coding:utf-8 --
# python和java中的变量本质不一样,python的变量实质是一个指针, int, str
# 也可以理解为一个便利贴，指针的大小是固定的
a = 1
a = 'abc'
pass

# 2.先生对象，然后贴在便利贴
a = [1,2,3]
b = a
b.append(4)

print(a)

print(a is b)
# 内存的id
print(id(a), id(b))