#

def add(a,b):
    a += b
    return a


class Company:
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs
    def add(self, staff_name):
        self.staffs.append(staff_name)

    def remove(self, staff_name):
        self.staffs.remove(staff_name)


if __name__ == '__main__':
    com1 = Company("wangjie", ["15", "172"])
    com1.add("189")
    com1.remove("172")
    print(com1.staffs)

    com2 = Company("wangjie")
    com2.add("luoyao")
    print(com2.staffs)

    com3 = Company("lisi")
    com3.add("zhangsan")
    # 因为staffs=[]是空列表，是可变的，然后com2和com3都是这个指向默认值，导致他们是一个对象
    print(com3.staffs)
    print(com2.staffs)
    # com2 is com3是true的话，俺么就是证明，他们是同一对象
    print(com2 is com3)
# 第一种情况，第三种，a不受影响，第二种a收到了影响
#     a = 1
#     b = 2
#     c = add(a, b)
#     print(c)
#     print(a, b)

# 第二种情况
#     a = [1, 2]
#     b = [3, 4]
#
#     c = add(a,b)
#
#     print(c)
#     print(a, b)

# 第三种情况
#     a = (1, 2)
#     b = (3, 4)
#
#     c = add(a,b)
#
#     print(c)
#     print(a, b)
