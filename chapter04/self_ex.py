# 自省是通过一定的机制查询到对象的内部结构

from chapter04.class_method import Date

class Person:
    '''
    人们
    '''
    name = "user"

class Student(Person):
    def __init__(self, school_name, age):
        self.school_name = school_name
        self.age = age


if __name__ == '__main__':
    user = Student("慕课网",29)

    # 通过__dict__查询属性
    print(user.__dict__)
    # 因为user是属于Student累的实例，由于向上查找，Student中没有name属性，只有找到Person有
    print(user.name)
    user.__dict__["school_addr"] = "北京市"
    print(user.school_addr)
    print(Person.__dict__)
    print(Person.__doc__)
    a = [1,2]
    print(dir(a))