#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/14 20:20
# @Author  : WangJie
# @Software: PyCharm
# @Description:


import paho.mqtt.client as mqtt

# 一旦连接成功，回调此方法
def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))

# 一旦订阅到消息，回调此方法
def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

# 一旦订阅成功，回调此方法
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# 一旦有log，回调此方法
def on_log(mqttc, obj, level, string):
    print(string)

# 新建mqtt客户端，默认没有clientid，clean_session=True, transport="tcp"
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_log = on_log
# 连接broker，心跳时间为60s
mqttc.connect("iot.eclipse.org", 2883, 60)
# 订阅该主题，QoS=0
mqttc.subscribe("paho/test/single", 0)

mqttc.loop_forever()