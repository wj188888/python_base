from demo_python import  dict_get, f_string, uppacking
# from demo_python.default_dict import Visits
from dict_get import return_result
if __name__ == '__main__':
    numbers = [-1,29,100,-93,223]
    minvalue, maxvalue = return_result(numbers)
    enter = '\n'
    print(f'最小值：{minvalue} {enter}最大值：{maxvalue}')