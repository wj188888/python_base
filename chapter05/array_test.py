# array, deque
# 数组

a = list

import array
# array和list的一个重要区别，array只能存放指定的数据类型
my_array = array.array("i")
my_array.append(1)
my_array.append(2)
print(my_array)