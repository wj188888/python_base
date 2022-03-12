# -*- coding: utf-8 -*-
from pytest_source_code.test_foocompare import Foo
from pytest_source_code.window import Window
import sys

from pytest_source_code import app

import pytest
import requests

class MockResponse:
    """模拟返回mock数据,不通过API"""
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


@pytest.fixture(autouse=True)
def mock_response(monkeypatch):
    """Requests.get() mocked to return {'mock_key':'mock_response'}."""
    def mock_get(*args, **kwargs):
        return MockResponse()
        # mock_get获取一个MockResponse的实例,通过json来返回数据,不需要API接口
    monkeypatch.setattr(requests, "get", mock_get)

@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """如果你想阻止" requests "库在所有测试中执行http请求，你可以这样做:"""
    """Remove requests.sessions.Session.request for all tests."""
    monkeypatch.delattr("requests.sessions.Session.request")

sys.dont_write_bytecode = True


@pytest.fixture
def windowc():
    return Window()

@pytest.fixture
def window(caplog,windowc):
    window = windowc.create_window()
    # yield 返回window值
    yield window
    for when in ("setup", "call"):
        messages = [
            x.message for x in caplog.get_records(when) if x.levelno == logging.WARNING
        ]
        if messages:
            pytest.fail(
                "warning messages encountered during testing: {}".format(messages)
            )

pytest.LogCaptureFixture
def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":

        return ["Comparing Foo instances:", " vals: {} != {}".format(left.val, right.val),]