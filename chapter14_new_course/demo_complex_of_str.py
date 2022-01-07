# -- coding:utf-8 --
# 判断字符串a是否以字符串b开头或结尾
# 某文件系统目录下有意系列文件
'''quicksort.c
graph.py
heap.java
install.sh
stack.cpp
编写程序给其中所有.sh文件和.py文件加上用户可执行权限
'''
# 解决方案
# 使用str.startswitch()和str.endswith()函数
import os
# os.chmod()修改权限


# 查看某个目录下的文件名
# print(os.listdir('.'))
# s = os.stat('demo_complex_of_str.py')
# print(oct(s.st_mode))
#
fn = ('aaa.px', 'xxx.txt', 'yyy.sh')
ue = ('.py', '.sh', '.txt')
# for i in fn:
#     ls = i.endswith(ue)
#     print(ls)
#     if ls:
#         os.chmod(i, s.st_mode | 0o100)

'''
    掩码：0o100
    import stat
    stat.S_IXUSR丶0o100
'''

# 同样的功能有
import stat
#

for fn1 in os.listdir():
    if fn1.endswith(ue):
        fs = os.stat(fn1)
        os.chmod(fn1, fs.st_mode | stat.S_IXUSR)    # 这个stat.S_IXUSR就是