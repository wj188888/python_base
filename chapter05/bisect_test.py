import bisect
# 用来处理已排序的序列，用来维持已排序的序列，升序方式
from collections import deque
# 二分法查找

inter_list = deque()
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 10)
bisect.insort(inter_list, 33)
bisect.insort(inter_list, 6)
bisect.insort(inter_list, -100)


print(inter_list)

# 查找在一个序列中，第几个位置是什么元素，方便插入
print(bisect.bisect_left(inter_list, 11))
print(inter_list)
