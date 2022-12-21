#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/12/21 15:16
# @Author  : WangJie
# @Software: PyCharm

from faker import Faker
fake = Faker()

# first, import a similar Provider or use the default one
from faker.providers import BaseProvider

# create new provider class
class MyProvider(BaseProvider):
    def foo(self) -> str:
        return 'bar'

fake.add_provider(MyProvider)
print(fake.foo())