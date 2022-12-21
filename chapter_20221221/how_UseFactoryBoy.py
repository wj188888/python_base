#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/12/21 15:27
# @Author  : WangJie
# @Software: PyCharm
# @Description:

from faker import factory
from book_data import Book

class BookFactory(factory.Factory):
    class Meta:
        model = Book

    title = factory.Faker('sentence', nb_words=4)
    author_name = factory.Faker('name')
books = BookFactory()
print(books.title)
print(books.author_name)