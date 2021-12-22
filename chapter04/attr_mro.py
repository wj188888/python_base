class A:
    name = "A"

    def __init__(self):
        self.name = "obj"
a = A()
print(a.name)

'''
    实例对象有一个类属性和方法属性，查找顺序是由下而上的，所以会打印obj
'''

'''
    MRO算法：
    多继承会很复杂
    DFS，深度优先搜索；
'''
# 不写object叫做：新式类
class D:
    pass

class E:
    pass

class C(E):
    pass

class B(D):
    pass

class A(B,C):
    pass


print(A.__mro__)
# 菱形查询顺序是(<class '__main__.A'>,
# <class '__main__.B'>,
# <class '__main__.C'>,
# <class '__main__.D'>, <class 'object'>)

# B丶C各自继承自D丶E，因为都是沿用了C3算法，所以都是不会报错的