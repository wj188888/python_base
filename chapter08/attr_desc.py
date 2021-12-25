import numbers

from datetime import date, datetime


'''
    # 对int类型进行定义和验证
    # 数据属性描述符
'''
class IntField:
    '''实现了下面三个方法的都是属性描述符对象'''
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < 0:
            raise ValueError("int value > 0")
        self.value = value

    def __delete__(self, instance):
        pass


class NonDataIntField:
    # 非数据属性描述符
    def __get__(self, instance, owner):
        return self.value


class User:
    # 优先级最高
    age = IntField()
    # 优先级第三
    age3 = 12
    # 优先级第四,这个里面先调用__get__，找不到再找__dict__方法
    age4 = NonDataIntField()
    # 优先级第五__getattr__方法,否则报错；
    def get_age(self):
        # 优先级第二
        age2 = 1
        return age2



# class User:
#     def __init__(self, name, email, birthday):
#         self.name = name
#         self.email = email
#         self.birthday = birthday
#         self._age = 0
#
#     # def get_age(self):
#     #     return datetime.now().year - self.birthday.year
#
#     # 把age编程描述成属性,用于市区转化
#     @property
#     def age(self):
#         return datetime.now().year - self.birthday.year
#
#
#     @age.setter
#     def age(self, value):
#         # 检查是否为字符串类型
#         self._age = value



if __name__ == '__main__':
    user = User()
    user.age = -1
    print(user.age)
    # user = User("bobby", date(year=1972, month=2, day=1))
    # # 调用property
    # print(user.age)
