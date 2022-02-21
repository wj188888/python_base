# -*- coding:utf-8 -*-

import pytest

@pytest.fixture()
def a_list():
    return [1,2,3,4,5,6]

def test_a_list(a_list):
    assert a_list[2] == 3