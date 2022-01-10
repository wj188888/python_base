# -- coding:utf-8 --
# 如何对字符串左丶右丶居中对齐
# 方法一:
# 使用字符串的str.ljust(),str.rjust(),str.center()进行左丶右丶居中对齐
s = 'abc'
print(s.ljust(4, '&').__repr__())   # 把内容放左边，空格放右边
print(s.rjust(10, '*').__repr__())   # 把空格放左边，内容放在右边
print(s.center(11, '*').__repr__())   # 把空格放左边，内容放在右边

print(format(s, '<10').__repr__())
print(format(s, '*>18').__repr__())
# 其实是调用的__format__这个函数
print(format(123, '+<10').__repr__())
print(format(-123, '->10').__repr__())
print(format(1234, '0=+10').__repr__())

d = {
    'lodDist': 100.0
}
