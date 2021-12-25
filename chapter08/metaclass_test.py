# qian

from collections import abc

def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"
        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company

''' type, 动态创建类:
    User = type("User", (), {})
'''
# 第二个参数是继承的基类， 第三个参数放属性；

# {"name": "user"}是一个属性
# {"say": say}可以是一个方法函数

def say(self):
    print("i am user")
    # return self.name

class BaseClass:
    def answer(self):
        return "i am baseclass"

'''
    什么是元类？
    元类是创建类的类    对象<-class(对象)-<type(元类)
'''
class Metaclass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

class User(metaclass=Metaclass):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "user"

'''
    pyhton中类的实例化的过程，
    1.首先寻找metaclass，通过metaclass去创建User类
    2.然后用type去创建类对象，然后元类中会去重载__new__魔法函数，定义生成这个类的前提规则
    3.然后去类中我们的初始化，一起其他类的函数
'''

if __name__ == '__main__':
    # MyClass = create_class("user")
    # type去创建类的方式：
    # User = type("User", (BaseClass, ), {"name": "user", "say": say})



    my_obj = User(name="bobby")
    # print(my_obj.say)
    print(my_obj)