# -- coding:utf-8 --
'''
    f-string
'''
def f_string_function():
    name = "wangjie"
    age = 18
    yuwen = 78
    math = 88
    english = 90
    sum = yuwen + math + english
    person = f'姓名: {name}，年龄： {age}岁， 总分是:{sum}分，平均分:{round(sum/3, 1)}分'
    print(person)


def get_value():
    dictone = {
        "name": "wangjie",
        "age": 19,
        "sex": '男'
    }
    save_dictone = tuple(dictone.items())
    print(type(save_dictone))
    print(save_dictone)
    itemone = ('wangjie', 'luoyao')
    first, second = itemone
    '''因为使用f-string不能有转义符号，所以将转义的符号设置成变量'''
    enter = '\n'
    print(f'first: {first},first的类型是{type(first)}{enter}{enter}\
    second: {second},second的类型是{type(second)}')


if __name__ == '__main__':
    get_value()