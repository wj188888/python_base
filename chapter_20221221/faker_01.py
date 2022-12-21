#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/12/21 10:56
# @Author  : wangjie
# @Software: PyCharm
# import faker.providers.person
from faker import Faker
fake = Faker()

# for _ in range(10):
#   print(fake.name())

from faker import Faker
from faker.providers import job

fake = Faker()
fake.add_provider(job)

for _ in range(20):
    print(fake.job()) # fake工作职位