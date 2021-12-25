# __getattr__丶__getattribute__

from datetime import date, datetime

class User:
    def __init__(self, name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        self.info = info

    # __getattr__就是查询不到属性时运用,进入这个函数
    def __getattr__(self, item):
        return self.info[item]

    def __getattribute__(self, item):
        # 比__getattr__更加高级, 是优先访问的，不要去重写他
        return "boods"

'''
    __getattr__就是查询不到属性时运用
'''

if __name__ == '__main__':
    user = User("bobby", date(year=1972, month=2, day=1), info={"company_name": "huawei"})
    # print(user.age) # 报错，找不到age
    #
    print(user.company_name)
