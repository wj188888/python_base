# -*- coding:utf-8 -*-

list1 = [1,3,2,4,5,6,7,8,9,10]
print(list1[0:5]) # 0,1,2,3,4
print(list1[0:5:2])
print("=================")
# list2 =
values = list1
z = list(map(lambda x,y: x+y,[1,2], [3,4])) # 匿名表达式
print(z)
zz = (value for value in list1 if value%2==0) # 生成式
for z in zz:
    print(z)



