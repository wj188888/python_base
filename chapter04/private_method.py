# 自省是通过一定的机制查询到对象的内部结构

from chapter04.class_method import Date

class User:
    def __init__(self, birthday):
        # 私有属性
        self.__birthday = birthday

    def get_age(self):
        # 返回年龄
        return 2018 - self.__birthday.year

class Student(User):
    def __init__(self, birthday):
        self.__birthday = birthday

if __name__ == '__main__':
    user = User(Date(1990,2,1))
    print(user.get_age())
    # print(user.__birthday)
    '''对于私有属性，python可以使用_classname__属性,后面跟私有属性的方式来访问'''
    print(user._User__birthday)
    stu = Student(Date(1990,2,29))
    print(stu._Student__birthday)