# -*- coding: utf-8 -*-
from collections.abc import Iterable, Iterator
l = [2,3,4,5]
if __name__ == '__main__':
    print(isinstance(l, Iterable))
    print(isinstance(list, Iterable))
    print(isinstance(str, Iterable))
    print(isinstance(dict, Iterable))

    # False
    print(isinstance(int, Iterable))
    print(iter(l))  # diaoyong __iter__
    it = iter(l)
    print(next(it)) # 调用 __next__
    # 直到next输入所有的list数据后,抛stopOteration为止

    # vim学习
    # https://www.cnblogs.com/heyboom/p/10522059.html
