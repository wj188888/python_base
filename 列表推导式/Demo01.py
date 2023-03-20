#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/11 9:52
# @Author  : wangjie
# @Software: PyCharm
# description: 对continue这个关键词做处理

def remove_odd_mul_100(numbers):
    """剔除奇数并乘于100"""
    results = []
    for num in numbers:
        if num % 2 == 0:
            # 退出for循环内容
            continue
        results.append(num * 100)
    return results

if __name__ == '__main__':
    list1 = [1,23,4,52,98]
    print(remove_odd_mul_100(list1))
    # 这里规则是for n in list1取到n的值，对n值筛选处理，
    results = [n * 100 for n in list1 if n % 2 == 0] # 列表推导式和上方函数一致
    print(results)