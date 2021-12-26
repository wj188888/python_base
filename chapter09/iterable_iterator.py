#
from collections.abc import Iterator, Iterable


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list
    # 调用iter必须返回一个Iterator
    # 自定义一个迭代器

    def __iter__(self):
        return MyIterator(self.employee)


    '''
        如果有__getitem__函数，就会自己去调用__iter__;
        如果有__iter__函数，那么首先是调用这个魔法函数
        如果都没有，就会报错，对象是不可迭代的
    '''


    # 魔法函数
    def __getitem__(self, item):
        return self.employee[item]

    # 迭代器不支持切片
class MyIterator(Iterator):
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __next__(self):
        # 真正返回迭代值在这里
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word




if __name__ == '__main__':
    company = Company(["tom", "bob", "jane"])
    # 获取到迭代器，然后保存到变量my_iter中去
    my_iter = iter(company)
    while True:
        try:
            next(my_iter)
        except StopIteration:
            pass
    print(my_iter)
    for item in company:
        print(item)
