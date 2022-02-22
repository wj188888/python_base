
'''
    函数式编程，map
    filter
    reduce
'''

def func(x):
    return x.isalnum()

class FuncCode:
    def __init__(self):
        pass
    def demo_map(self):
        '''
        这是一个map函数：
            使用map函数将序列的所有元素传递给函数
        :return:
        '''
        x = list(map(str, range(10)))
        print(x)

    def demo_filter(self):
        '''
        这是一个filter函数：
            根据布尔函数的返回值来对元素进行过滤
        :return:
        '''
        seq = ["foo","x41","?!", "***"]
        res = list(filter(func,seq))
        print(res)

    def demo_reduce(self):
        from functools import reduce
        '''
        这是一个reduce函数：
            使用指定的函数将序列的前两个元素合二为一，再将结果与第3个元素合二为一，依次类推，比如所有字符串的叠加
        :return:
        '''
        strs = ["wangjie","wanghao","luoyao","helloworld","pround-heart","qing"]
        types = (1,23,4,56,-2321,12)
        dicts = {"wangjie": "name", "age":18}
        res = reduce(lambda x,y: x+y , dicts) # 如果是字典就只把他们的key值进行相加
        print(res)

