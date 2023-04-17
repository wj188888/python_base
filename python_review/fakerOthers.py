#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2023/4/17 22:04
# @Author: WangJie
# @Description:
import faker.generator
from faker import Faker
fk = Faker()

Faker.seed(1)
print(fk.name())