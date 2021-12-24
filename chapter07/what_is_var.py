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

x = "adc"
y = "adc"
print(x is y)
print(x==y)

# 由于python内部优化，其实对于  小整数丶和短一点的“字符串” 来说，会进行复用，而列表不会
'''
    ==: 应为调用了魔法函数__eq__，对比两个值是否相等;
    is: 两个对象相同
'''

class Person:
    pass


person = Person()
if type(person) is Person:
    print("相等")

# 或
if isinstance(person, Person):
    print("也相等")