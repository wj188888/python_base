# -*- coding:utf-8 -*-

'''
    scope="class"这个类下的执行方式
    执行方式：pytest --setup-show test_demo04.py
'''
import pytest

# @pytest.fixture(scope="class")
# def first():
#     print("\n获取用户名，scope为class级别只运行一次")
#     a = "王杰"
#     return a

class TestCase():
    def test_1(self, first):
        '''用例fixture'''
        print(f"测试账号：{first}")
        assert first == "王杰"

    def test_2(self, first):
        '''用例fixture'''
        print(f"测试账号:{first}")
        assert first == "王杰"