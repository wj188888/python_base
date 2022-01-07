# -- coding:utf-8 --
# 如何拆分含有多种分隔符的字符串
from functools import reduce

# 方法1：连续使用str.split()方法
str1 = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
# print(str1.split(';'))
#
# # 列表解析
# print([ss.split('|') for ss in str1.split(';')])

print(sum([str1.split('|') for str1 in str1.split(';')], []))

def my_split(s, seps):
    res = [s]
    for sep in seps:
        t = []
        list(map(lambda ss: t.extend(ss.split(sep)), res))
        res = t
    return res

if __name__ == '__main__':
    '''
        使用之前的结果，然后创建一个函数
        # [x] sep1 => [x, yz,z] sep2 => [1,3,4,56]
    '''
    # my_split(str1, ',;|\t')
    # 首先，lambda后边的参数，冒号前的参数是输入参数，冒号后的参数是输出参数，然后后边是对集合等可迭代的对象，列表和元祖，str
    print(reduce(lambda l, sep: sum(map(lambda ss: ss.split(sep), l), []), ',:;|\t', [str1]))
    # 和上边实现的一样
    my_split2 = lambda s, seps: reduce(lambda l, sep: sum(map(lambda ss: ss.split(sep), l), []), seps, [str1])
    print(my_split2(str1, ';,|\t'))

    # 方法二：
    # 使用正则表达式,re.split()方法
    import re

    print(re.split('[;|,:\t]', str1))