class A(object):
    pass

class B(A):
    pass

b = B()

print(isinstance(b, B))
print(isinstance(b, A))

id(B)

# 做对比和参考
print(type(b) is A)
# print(type(b) == A)
print(isinstance(b, A))
'''
type(b) == A是值的相等
而
isinstance(b, A),是值对象相等，意味着这样在这个链条中，就是返回True
'''