# -*- coding:utf-8 -*-

import pytest
# import requests

class TestPeople:
    @pytest.fixture
    def get_config(self):
        config = 10
        return config

    @pytest.fixture
    def get_headers(self, get_config):
        headers = get_config + 100
        return headers

    def test_01(self, get_headers):
        data = get_headers
        assert data == 110

    def test_02(self, get_headers):
        data = get_headers - 10
        assert data == 101
# if __name__ == '__main__':
#     pytest.main(['-vs', "test_demo.py"])