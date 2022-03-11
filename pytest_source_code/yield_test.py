# -*- coding: utf-8 -*-
def yield_test(n):
    print("第一次返回")
    for i in range(n):
        # yield 返回call()的值,
        print(f"{i}的平方", i*i)
        # 循环体内,或者说迭代器内是每次都执行这个,而不再执行迭代外的内容;
        yield call(i)
        print("i=", i)
    # do something
    print("do something")
    print("end.")

def call(i):
    return i*2

# 使用for循环
for i in yield_test(5):
    # 将循环的内容打印出来
    print(i, ",")