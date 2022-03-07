# -*- coding: utf-8 -*-

import requests

import app

class MockResponse:

    @staticmethod
    def json():
        return {"mock_key": "mock_response"}

def test_get_json(mockeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse

    mockeypatch.setattr(requests, "get", mock_get)

    result = app.get_json("https://fakeurl")
    assert result["mock_key"] == "mock_response"

