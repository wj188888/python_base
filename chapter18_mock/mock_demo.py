# -- coding:utf-8 --
import mock

from mock import mock
def mock_test(mock_method, request_data, url, method, response_data):
    mock_data = mock.Mock(return_value=response_data)
    res = mock_method(url, method, request_data)
    return res