#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2023/4/1 18:13
# @Author: WangJie
# @Description:
import time, sys

indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('**********')
        time.sleep(0.1)

        if indentIncreasing:
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
except KeyError:
    sys.exit()
