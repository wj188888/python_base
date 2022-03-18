# -*- coding: utf-8 -*-

def test_set_comparison():
    set1 = set("8035")
    set2 = set("8031")
    assert set1 == set2

def test_baz(caplog):
    for record in caplog.records:
        assert record.levelname != "CRITICAL"
    assert "wally" not in caplog.text