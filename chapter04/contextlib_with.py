# -- coding:utf-8 --
import contextlib

# 把一个函数定义成上下文管理器,函数定义如下
@contextlib.contextmanager
def file_open(file_name):
    print("file open")
    yield {}
    print("file end")

with file_open("./demofile/wj.txt") as f_opened:
    print("file processing")