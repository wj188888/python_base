# -*- coding: utf-8 -*-
class Foo:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val

def test_compare():
    f1 = Foo(12)
    f2 = Foo(12)
    assert f1 == f2