# -*- coding: utf-8 -*-

import pytest

@pytest.mark.parametrize("i", range(50))
def test_num(i):
    if i in (17, 25):
        pytest.fail("bad luck")

@pytest.mark.parametrize("j", range(11))
def test_sum(j):
    if j^2 in (100,25,4):
        pytest.fail("so luck failing")