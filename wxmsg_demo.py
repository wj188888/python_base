# -*- coding:utf-8 -*-

"""
uiautomation
pip install uiautomation
"""

import uiautomation

wx = uiautomation.WindowControl(Name="微信") # 查询微信空间进行绑定
wx.SwitchToThisWindow() # 唤醒windows窗口
sc = wx.EditControl(Name="搜索") # 查找搜索
sc.Click()
sc.SendKeys("铁贵二")
sc.SendKeys("{Enter}")
sr = wx.EditControl(Name="输入")
sr.Click()
for msg in range(3):
    sr.SendKeys("我爱铁贵儿！! {Enter} ", waitTime=0.1)
