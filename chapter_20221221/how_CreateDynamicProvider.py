#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/12/21 15:18
# @Author  : WangJie
# @Software: PyCharm

from faker import Faker
from faker.providers import DynamicProvider

medical_professions_provider = DynamicProvider(
     provider_name="medical_profession",
     elements=["dr.", "doctor", "nurse", "surgeon", "clerk"],
)

fake = Faker()
medical_professions_provider.add_element("HHEE.o") # 向provider中添加元素
fake.add_provider(medical_professions_provider)

for _ in range(10):
     print(fake.medical_profession())