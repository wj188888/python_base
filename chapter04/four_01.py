# -- coding:utf-8 --
class Cat(object):
    def say(self):
        print("i'm a cat")


class Dog(object):
    def say(self):
        print("i'm a dog")


class Duck(object):
    def say(self):
        print("i'm a duck")


# anminal = Cat
# anminal().say()

# 在java中这样
# class Anminal(object):
#     def say(self):
#         print("i'm a anminal")

'''
在 java中去调用父类的方法，首先父类要进行声明;
Anminal an = Cat()
an.say()    这样去调用
'''

# 在python中

anminal_list = [Cat, Dog, Duck]
for anminal in anminal_list:
    # 这一步实现了多态,不知道为啥会有anminal(),不加括号就是错的;
    anminal().say()


# ======================
a = ["body1", "body2"]
b = ["body2", "body"]
name_tuple = ["body3", "body4"]
name_set = set()
name_set.add("body5")
name_set.add("body6")

# extend()内的是一个可迭代对象
a.extend(name_set)
print(a)

'''主要实现了__getitem__方法，那么这个类就是可迭代的'''
