# -*- coding: utf-8 -*-
from pytest_source_code.test_foocompare import Foo
import sys

from pytest_source_code import app


sys.dont_write_bytecode = True


def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":

        return ["Comparing Foo instances:", " vals: {} != {}".format(left.val, right.val),]