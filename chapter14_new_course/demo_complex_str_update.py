# -- coding:utf-8 --
# 如何调整字符串中文本的格式
'''
    解决方案：
    使用正则表达式re.sub()方法做字符串替换，利用正则表达式的捕获组，捕获每个部分内容，在替换
    字符串中调整各个捕获组的顺序.
'''
import re

# 转义字符，\
# 给分组取一个名字，?P<名字>
with open('./data/res1.log', 'r', encoding='utf8') as fp:
    log = fp.read()
# print(re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', './data/res.log'))
print(re.sub(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>-\g<day>-\g<year>', log))