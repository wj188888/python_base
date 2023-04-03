#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2023/3/22 21:08
# @Author: WangJie
# @Description:

import csv

def readCsv():
    with open(r"data/csv_data.csv", "r", encoding='utf-8') as fp:
        reader = csv.reader(fp)
        for row in reader:
            print(row)

#dicts为True时，打印出dict字典，为false时打印原始的值
def dictReadCsv(dicts=False):
    with open(r"data/csv_data.csv", "r", encoding='utf-8') as fp:
        reader = csv.DictReader(fp)
        if dicts==1:
            for row in reader:
                print(dict(row))
        elif dicts==0:
            for row in reader:
                print(row)
        else:
            #默认展示成列表
            for row in reader.reader:
                print(row)


if __name__ == '__main__':
    dictReadCsv(dicts=2)

