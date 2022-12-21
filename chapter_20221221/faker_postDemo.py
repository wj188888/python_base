#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/12/21 14:09
# @Author  : WangJie
# @Software: PyCharm
from faker import Faker
from mdgen import MarkdownPostProvider

fake = Faker()
fake.add_provider(MarkdownPostProvider)
fake_post = fake.post(size='small') # available sizes: 'small', 'medium', 'large'
print(fake_post)