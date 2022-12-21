#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/12/21 14:14
# @Author  : WangJie
# @Software: PyCharm
from faker import Faker
from faker_airtravel import AirTravelProvider
from faker.providers.address.zh_CN import Provider as zh_CN

fake = Faker(locale="zh_CN")
fake.add_provider(AirTravelProvider)
fake.add_provider(zh_CN)

for _ in range(10):
    print(fake.airport_object())
print("=====本地语言faker ===")
for _ in range(10):
    # print(fake.address())
    # print(fake.administrative_unit())
    # print(fake.building_number())
    # print(fake.city()) # 城市名
    # print(fake.city_name()) # 城市名字
    # print(fake.company_suffix()) # 公司前缀
    # print(fake.date()) # 时间
    # print(fake.date_between()) # 时间
    # print(fake.date_between_dates()) # 时间
    # print(fake.date_object()) # 时间
    # print(fake.month_name()) # 时间
    # print(fake.timezone()) # 时区
    print(fake.free_email_domain()) # 邮箱