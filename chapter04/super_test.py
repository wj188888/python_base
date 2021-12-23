# -- coding:utf-8 --
# 4.9super真的是调用父类吗

class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B,C):
    def __init__(self):
        print("D")
        super(D, self).__init__()



from threading import Thread
class MyThread(Thread):
    def __init__(self, user, name):
        self.user = user
        # 重用父类的方法
        super().__init__(name = name)


#
'''答：应为super父类可能有很多逻辑，我们继承了父类，可以去复用一些逻辑，不用再造轮子了'''
# super到底执行顺序是什么样的？
'''答：执行顺序就是按照MRO算法去执行，深度广度优先算法'''
if __name__ == '__main__':
    d = D()

'''
    mixin模式特点：
    1.Minxi类模式单一，一般就放一个方法
    2. 不和基类关联，可以和任意基类组合，基类可以不和mixin关联就可以初始化成功
    3.在mixin中不要使用super用法，因为super符合MRO算法
    4. 最好以Mixin结尾
'''