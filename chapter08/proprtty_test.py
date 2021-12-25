from datetime import date, datetime

class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0


    # def get_age(self):
    #     return datetime.now().year - self.birthday.year

    # 把age编程描述成属性,用于市区转化
    @property
    def age(self):
        return datetime.now().year - self.birthday.year


    @age.setter
    def age(self, value):
        self._age = value



if __name__ == '__main__':
    user = User("bobby", date(year=1972, month=2, day=1))
    # 调用property
    print(user.age)