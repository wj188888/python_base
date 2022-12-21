#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/12/21 12:07
# @Author  : WangJie
# @Software: PyCharm


from faker import Faker

from faker_music import MusicProvider

fake = Faker()
fake.add_provider(MusicProvider)

for _ in range(10):
    print(fake.music_genre())
print("=========")
for _ in range(10):
    print(fake.music_subgenre())
print("========乐器=======")
for _ in range(10):
    print(fake.music_instrument_category())