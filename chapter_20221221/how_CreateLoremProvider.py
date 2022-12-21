#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/12/21 15:24
# @Author  : WangJie
# @Software: PyCharm
# @Description: 编写自定义的Provider的内容

from faker import Faker
fake = Faker()

my_word_list = [
'danish','cheesecake','sugar',
'Lollipop','wafer','Gummies',
'sesame','Jelly','beans',
'pie','bar','Ice','oat' ]

fake.sentence()
print(fake.sentence(ext_word_list=my_word_list)) # 随机出现几个值得组合