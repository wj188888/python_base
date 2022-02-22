
from demo01 import *
from duotai import length_message
from jicheng import Bird


if __name__ == '__main__':
    # fun = FuncCode()
    # fun.demo_reduce()
    # data = {
    #     "name": "wangjie",
    #     "age": 18
    # }
    # length_message(data)

    bird = Bird();
    bird.sing()

    '''
    方便理解： 这是bird.sing是一个函数，想在将函数给点一个变量，这个变量birdsong是一个函数了，那么你去查看这个函数的类型，就是NoneType
    然后，就可以通过这种方式访问类内部的内容;
    print(type(bird.sing()))
    '''
    birdsong = bird.sing
    print(type(birdsong()))
    print(birdsong())
