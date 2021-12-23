# -- coding:utf-8 --
alist = [1,2,3,4,5,6,7,8,9]
'''
alist[start:end:step]# 开始，结束，步长

'''

print(alist[::])
print(alist[::-1])
print(alist[3:6])
print(alist[0:100])
print(alist[100:])

alist[len(alist):] = 9 # 这是一个赋值操作，在列表尾部加一个元素
alist[:0] = [1, 2] # 在列表头部插入元素
alist[3:3] = [4]    # 在列表中间位置插入元素
alist[:3] = [1, 2]

