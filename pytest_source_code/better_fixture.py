# -*- coding: utf-8 -*-

def first_entry():
    return "a"


def order(first_entry):
    return [first_entry]


def test_string(order):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "b"]


def test_int(order):
    # Act
    order.append(2)

    # Assert
    assert order == ["a", 2]

# 上边的代码等同于下边解释,first_entry()作为一个参数,然后把返回值给到下一个调用的值,使用是函数式编程思想;

# test_string(order)的解释
entry = first_entry()
the_list = order(first_entry=entry)
test_string(order=the_list)

# test_int(first_entry())的解释
entry = first_entry()
the_list = order(first_entry=entry)
test_int(order=the_list)