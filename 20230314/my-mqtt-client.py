#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/14 19:01
# @Author  : WangJie
# @Software: PyCharm
# @Description:
import logging

from paho.mqtt import client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


def send_data():
    userdata = {
        'name': 'wj',
        'age': 12
    }
    userdata = json.dumps(userdata)
    return userdata



client = mqtt.Client(client_id="MQTT-wj", clean_session=True, userdata=send_data(), transport="tcp")
client.on_connect = on_connect
client.on_message = on_message
client.message_retry_set(retry=10) #设置代理响应为10s，每10s去发送消息到代理
client.max_queued_messages_set(65535) #设置消息队列对大的长度为65535，实际上是要加上20的长度
# client.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
#     tls_version=ssl.PROTOCOL_TLS, ciphers=None) #配置网络加密和认证
client.enable_logger(logger=None)
client.username_pw_set("admin", "admin")
usrdata = {"key": "value1"}
client.user_data_set(usrdata)# 设置私有数据
client.reconnect_delay_set(min_delay=1, max_delay=120)#尝试重试连接的时间间隔，在1-120s 之间


topic = f"mqtt/wj/userdata"
host = "192.168.1.3"
client.connect(host, 1883, 60)
logging.INFO("你好boys")

client.publish(topic=topic, payload=send_data(), qos=0)
client.loop_forever()