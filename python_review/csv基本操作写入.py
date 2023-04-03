#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2023/3/22 21:20
# @Author: WangJie
# @Description:

import csv

data = [
    ('Name', 'Age', 'Sex'),
    ('Jane', '12', 'Female'),
    ('jack', '18', 'male'),
    ('roles', '21', 'Female'),
]

def csvWrite():
    with open(r'data/csv_data写入.csv', "w", newline='') as fp:
        writer = csv.writer(fp)
        writer.writerows(data)

def csvDictWrite():
    data = [
        {'Name': 'Mark', 'Age': 17, 'Sex': 'Male'},
        {'Name': 'Lisa', 'Age': 16, 'Sex': 'Female'},
        {'Name': 'Jacky', 'Age': 20, 'Sex': 'Male'},
    ]
    with open('data/csv_data写入.csv', 'w', newline='') as f:
        #文件的表头， newline是定义换行的符号
        fieldnames = ['Name', 'Age', 'Sex']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

if __name__ == '__main__':
    csvWrite()