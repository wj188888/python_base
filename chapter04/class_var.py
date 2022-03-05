class A:
    aa = 1
    def __init__(self, x, y):
        self.x = x
        self.y = y
    '''
        self是这个class， A的实例
        
    '''
a = A(2,13)
print(a.x, a.y, a.aa, A.aa)
'''
    其中a.aa的aa是类变量
    假如赋值a.aa = 1
    那么实例对象a就有两个属性，一个是类属性A.aa，另一个是a.aa
'''