# -- coding:utf-8 --
# 列表生产式（列表推导式）
# 1.提取1-20之间的奇数
odd_list = []
for i in range(21):
    if i%2 == 1:
        odd_list.append(i)
print(odd_list)

odd_list2 = [i for i in range(21) if i % 2 == 0]
print(odd_list2)


# 复杂逻辑
def handle_item(item):
    return item * item
odd_list3 = [handle_item(i) for i in range(21) if i % 2 == 1]

# 列表生成式性能高于列表操作
print(type(odd_list3))
print(odd_list3)

# 生成器表达式,把中括号变成小括号就成立神生成器
odd_gen = (i for i in range(21) if i % 2 == 1)
print(type(odd_gen))
for item in odd_gen:
    print(item)

'''
    编码最重要的是可读性
'''

# 字典推导式
my_dict = {"name": "wangjie", "age": 18, "sex": "male"}
reversed_dict = {value:key for key,value in my_dict.items()}
print(reversed_dict)

# 集合推导式
my_set1 = set(my_dict.keys())
print(my_set1)
my_set = {value for key, value in my_dict.items()}
print(type(my_set))
print(my_set)

