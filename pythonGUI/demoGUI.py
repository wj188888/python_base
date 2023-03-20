#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2023/3/17 10:26
# @Author: WangJie
# @Description: 编写pythonGUI学习内容

#导入wx GUi 这个库

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        #继承类初始化这个Frame
        wx.Frame.__init__(self, parent, id, title="Frame名称", pos=(100, 100), size=(300, 300))

if __name__ == '__main__':
    #生成app实例
    app = wx.App()
    #实例化一个Frame框架
    frame = MyFrame(parent=None, id=-1)
    #将这个实例显示出来，为false为隐藏框架窗口
    frame.Show(True)
    #一直展示这个app，loop循环出来
    app.MainLoop()


