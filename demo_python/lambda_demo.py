# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sum = lambda a,b: a*b
    print(sum(11,23))
    print(type(sum))
    print(sum)
    xx = sum
    print(xx)
    avg = lambda x,y: round((x+y)/4.6, 3)
    print(avg(10,6))

