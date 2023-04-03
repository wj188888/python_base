#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2023/3/22 20:29
# @Author: WangJie
# @Description:

#看python如何简单的处理数据
import numpy as np
from sklearn import preprocessing

data = np.array([[-292, 81.82, 93], [291, 91.291, -21],[1, 33, -3.1]])


#均值预处理
data_pre = preprocessing.scale(data)
print(f"\nMean = {data_pre.mean(axis=0)}")
print(f"Std daviation = {data_pre.std(axis=0)}")

