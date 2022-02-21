# -*- coding:utf-8 -*-

import pytest

'''

执行结果：

    test_demo04.py
SETUP    S first
        test_demo04.py::TestCase::()::test_1 (fixtures used: first).
        test_demo04.py::TestCase::()::test_2 (fixtures used: first).
test_demo05.py
        test_demo05.py::test_1 (fixtures used: first).
TEARDOWN S first

'''



@pytest.fixture(scope="session")
def first():
    print("\n获取用户名，scope为module级别当前.py模块只运行一次")
    a = "王杰"
    return a


