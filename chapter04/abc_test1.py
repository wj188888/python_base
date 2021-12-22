# -- coding:utf-8 --
import abc

class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass

# 装饰器装饰过的内容，@abc.abstractmethod，初始化的时候就会去判断是否实现了；
class RedisBase(CacheBase):
    # def set(self, key, value):
    #     pass

    def get(self, key):
        pass
redisbase = RedisBase()
