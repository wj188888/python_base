# -*- coding:utf-8 -*-

'''
    scope="module"
    执行结果:

      SETUP    M first
        test_demo05.py::test_1 (fixtures used: first).
        test_demo05.py::TestCase::()::test_2 (fixtures used: first).
  TEARDOWN M first

'''
import pytest



def test_1(first):
    '''用例fixture'''
    print(f"测试账号：{first}")
    assert first == "王杰"

# class TestCase():
#     def test_2(self,first):
#         '''用例传fixture'''
#         print(f"测试账号：{first}")
#         assert first == "王杰"