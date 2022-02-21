# -*- coding:utf-8 -*-

import pytest

@pytest.fixture()
def some_data():
    print("22223")
    yield
    print("jkkda")

def test_some_data(some_data):
    print("test-test")