# 生成器

# 什么是生成器函数， 函数里只要有yield关键字就是生成器

def gen_func():
    yield 1
    yield 2


# 多行求知，延迟求值提供了可能
# 斐波拉契
# 使用场景
def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index-1) + fib(index-2)
print(fib(10))

# 打印列表，斐波拉契
def fib2(index):
    re_list = []
    n,a,b = 0, 0, 1
    while n < index:
        re_list.append(b)
        a, b = b, a+b
        n += 1
    return re_list
print(fib2(10))


def gen_fib2(index):
    re_list = []
    n,a,b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a+b
        n += 1
    return re_list



def func():
    return 1


if __name__ == '__main__':
    # 生成器对象， 是在python编译字节码的时候产生的，如何访问生成器的值
    # 生成器也是符合迭代器协议的
    gen = gen_func()
    for i in gen:
        print(i)
    # re = func()
    gen2 = gen_fib2(10)
    for data in gen2:
        print(data)
    pass