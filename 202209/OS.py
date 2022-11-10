#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/13 20:28
# @Author  : wangjie
# @Software: PyCharm

"""
OS模块：
os.sep：用来获取系统路径
window：\\,linux和mac是/
os.name:显示使用的平台，windows是nt，linux和macOS是posix
os.getcwd：用于获取当前文件的目录
os.path.exists: 存在当前文件或者目录
"""
import os
print(os.sep)
print(os.name)
print(os.getcwd())
print("=========")
print(os.listdir("E:/3、code/python/python_base")) # 返回指定目录下所有的文件和目录名
# print(os.mkdir('E:/3、code/python/python_base/wangj')) # 新建目录
# print(os.rmdir('E:/3、code/python/python_base/wangj')) # 删除目录
# os.makedirs("E:/3、code/python/python_base/wangj/luoyao/hhalle") # 可以创建多层递归目录
# os.removedirs("E:/3、code/python/python_base/wangj/luoyao/hhalle") # 删除多层递归目录
# os.chdir("E:/3、code/python/python_base/wangj/luoyao/hhalle") # 改变当前目录到指定目录去,切换到指定的类中去了
# print(os.getcwd())  # 测试
print(os.path.getsize("OS.py"))
print(os.path.exists("E:\\3、code\\python\\python_base")) # 存在当前文件或者目录
print(os.path.isfile("E:\\3、code\\python\\python_base")) # 判断是否为文件

