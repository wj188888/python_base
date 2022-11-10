#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/13 21:00
# @Author  : wangjie
# @Software: PyCharm
"""
在虚拟环境(seleniumvenv)下执行
"""

from selenium import webdriver

from time import sleep
driver_path = f"chromedriver/chromedriver.exe"
driver = webdriver.Chrome(driver_path)
driver.get("www.baidu.com")
sleep(2)
driver.close()

