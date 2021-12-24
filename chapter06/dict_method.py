# -- coding:utf-8 --
import copy

a = dict()
#
# b = {"dict1": {"name": "wangjie", "age": 16},
#      "dict2": {"name1": "wangjie1", "age": 18}
#      }

# 清除字典
# b.clear()
# print(b)

# copy，返回浅拷贝
# new_dict = b.copy()
# print(new_dict)
# print(new_dict['dict2']['name1'])
#
# c = {"dict1": {"name": "wangjie", "age": 16},
#      "dict2": {"name1": "wangjie1", "age": 18}
#      }

# 深拷贝
# new_dict_deep = copy.deepcopy(c)
# print(new_dict_deep)
# print(new_dict_deep['dict2']['name1'])


# fromkeys
new_listx = ["wangjie", "luoyao"]
# fromkeys，第一个参数为key值，第二个参数，不管你写什么，都是作为一个value值；
new_dictx = dict.fromkeys(new_listx, 12)
# print(new_dictx)

# 如果去访问一个没有key值得iterbel，序列，就会报KeyError错误
# print(new_dictx['data'])

# 为了判断dict中是否有某一个key值
# print(new_dictx.get("data1", {"哈哈很多事，你坏坏"}))

defalut_value = new_dictx.setdefault("wangjie", {"imooc": 1, "name": 'wj'})
pass
