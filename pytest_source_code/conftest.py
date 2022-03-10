# -*- coding: utf-8 -*-

import pytest
import requests

class MockResponse:
    """模拟返回mock数据,不通过API"""
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


@pytest.fixture(autouse=True)
def mock_response(mockeypatch):
    """Requests.get() mocked to return {'mock_key':'mock_response'}."""
    def mock_get(*args, **kwargs):
        return MockResponse()
        # mock_get获取一个MockResponse的实例,通过json来返回数据,不需要API接口
    mockeypatch.setattr(requests, "get", mock_get)

@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """如果你想阻止" requests "库在所有测试中执行http请求，你可以这样做:"""
    """Remove requests.sessions.Session.request for all tests."""
    monkeypatch.delattr("requests.sessions.Session.request")