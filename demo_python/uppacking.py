# -- coding:utf-8 --
color = ['red', 'yellow', 'blue', 'black', 'green']
num = [21, 232, -232,92,11, -21,-100,999]
'''reverse=False默认，是降序，resverse=True,是升序'''
num_s = sorted(num, reverse=True)
# oldest, *others, youngest = num_s
# print(oldest, youngest)
# print(*others)

# 列表值是数字
first, second, *others = num_s
print(first, second, *others)

# 字符串
color_s = sorted(color)
little, *others, big = color_s
print(little, big)
print(*others)

#
