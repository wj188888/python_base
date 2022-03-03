# -*- coding: utf-8 -*-

class People:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.__sex = sex

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_sex(self):
        return self.__sex

    def set_sex(self, sex):
        self.__sex = sex

if __name__ == '__main__':
    person1 = People("王杰",118, "男")
    print(person1.name)
    person1.set_name("里斯")
    print(person1.name)
    print(person1.get_sex())
    print(hasattr(person1, "__sex"))
    print(hasattr(People, "get_sex"))
    print(hasattr(People, "get_name"))
    print(hasattr(People, "get_age"))

