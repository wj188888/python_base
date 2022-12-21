#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/12/21 15:33
# @Author  : WangJie
# @Software: PyCharm
# @Description:
# from faker.generator import random
# from faker import Faker
# fake = Faker()
# names = [fake.unique.first_name() for i in range(500)]
# # fake.random
# print(fake.random.getstate())
# assert len(set(names)) == len(names)


from faker import Faker

fake = Faker()
for _ in range(2):
     fake.unique.boolean()
     print(fake.unique)