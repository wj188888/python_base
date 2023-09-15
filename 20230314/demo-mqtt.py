#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/14 20:10
# @Author  : WangJie
# @Software: PyCharm
# @Description:

from paho.mqtt import client as mqtt
import random

broker = '192.168.1.3'
port = 1883
topic = "/python/mqtt"
client_id = 'python-mqtt-{}'.format(random.randint(0, 1000))

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("test")

def on_message(client, userdata, msg):
    print(msg.topic+" "+msg.payload.decode("utf-8"))
    # 消息处理
def publich():
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print("Send `{}` to topic `{}`".format(msg,topic))
        else:
            print("Failed to send message to topic {}".format(topic))


 # ClientId不能重复，也可不传入
client = mqtt.Client(client_id)
# 匿名登录不需要设置
client.username_pw_set("admin", "123456")  # 必须设置，否则会返回「Connected with result code 4」
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port, 60)
# 订阅主题
client.subscribe("test")
client.loop_forever()

