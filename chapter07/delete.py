# cpython 中垃圾回收的算法是采用 引用计数

a = object()
b = a

# del a是将对象的计数器减为0才会回收；
del b
print(a)
print(b)

class A:
    def __del__(self):
        pass

