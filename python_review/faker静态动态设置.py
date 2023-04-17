#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2023/4/17 21:45
# @Author: WangJie
# @Description:

from faker import Faker
from faker.providers import DynamicProvider, BaseProvider
#动态获取值
medical_profession_provider = DynamicProvider(
    provider_name="medical_profession",
    elements=["dr.","doctor", "nurse", "surgon","clerk"],
)

fk = Faker()
fk.add_provider(medical_profession_provider)

print(fk.medical_profession())


# 静态获取值
fk2 = Faker()
class first(BaseProvider):
    def foo(self) -> dict:
        return {"name": "wj", "age": 12}
class two(BaseProvider):
    def foo2(self) -> list:
        return ['lis', '112', 'dasjda']
fk2.add_provider(first)
fk2.add_provider(two)
print(fk2.foo())
print(fk2.foo2())
