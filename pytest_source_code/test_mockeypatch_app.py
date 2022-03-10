# -*- coding: utf-8 -*-
import pytest
import requests

from pytest_source_code import app


def test_get_json(mock_response):

    result = app.get_json("https://fakeurl")
    assert result["mock_key"] == "mock_response"

