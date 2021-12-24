# -- coding:utf-8 --
from collections import Mapping, MutableMapping


a = {}
print(isinstance(a, MutableMapping))
# 查看字典的所有魔法函数
print(dir(a))