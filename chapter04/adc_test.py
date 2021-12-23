# -- coding:utf-8 --
# 检查每一个类是否有某一个方法
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)

company = Company(["body1", "body2"])
print(len(company))

'''
hasattr可以判断某一个对象是否有某一种属性；
'''
# 判断company，是否有这个函数这个属性
print(hasattr(company, "__init__"))

''':cvar
    抽象基类abc，应用场景一，二
'''
# 场景一：我们在某些情况下希望判定某个对象的类型
from collections.abc import Sized

# 场景二：我们需要强制某个子类必须实现某些方法
# 比如实现一个web框架》（集成cache，如redis，cache，memorychache）
# 需要设计一个抽象基类，指定子类的必须实现某些方法

# 如何去实现模拟抽象基类
class CacheBase(object):
    def get(self, key):
        # 在用户调用的时候，才发现这个方法在继承类中没有实现，没有实现直接抛出异常,
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError


class RedisCache(CacheBase):
    def set(self, key, value):
        pass

redis_cache = RedisCache()
redis_cache.set("key", "value")

