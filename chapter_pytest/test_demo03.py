# -*- coding:utf-8 -*-


'''
    function级别的内容

'''
import pytest

@pytest.fixture()
def first():
    print("\n获取用户名")
    a = "王杰"
    return a

@pytest.fixture()
def second():

    print("\n获取密码")
    b = "123456"
    return b

def test_1(first):
    '''用例传fixture'''
    print(f"测试账号{first}")
    assert first == "王杰"

def test_2(second):
    '''用例传fixture'''
    print(f"测试密码{second}")
    assert second == "123456"