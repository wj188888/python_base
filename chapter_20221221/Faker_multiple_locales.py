#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/12/21 15:13
# @Author  : WangJie
# @Software: PyCharm

from faker import Faker
fake = Faker(['it_IT', 'en_US', 'ja_JP', 'zh_CN']) # 支持多种语言
for _ in range(10):
    print(fake.name())