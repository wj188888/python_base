# -- coding:utf-8 --
import redis

REDIS_CONFIG = {
    'host': '192.168.10.70',  # IP
    'port': 6379,  # 端口
    'password': '',  # 密码
    'db': 5,  # 数据库
    'decode_responses': True # 将存入的数据进行解码（主要用于将bytes类型转成string类型）
}


r = redis.StrictRedis(**REDIS_CONFIG)
user1 = r.get(name="user:role:1:3")
print(user1)
# x = 8.99+10.24+8.49+8.8+20.82+26.98
# print(x)