# -- coding:utf-8 --
from random import randint


def load_list_data(total_nums, target_nums):
    """
    从文件中读取数据，以list的方式返回
    :param total_nums: 读取的数量
    :param target_nums: 需要查询的数据的数量
    """
    all_data = []
    target_data = []
    file_name = "G:/慕课网课程/AdvancePython/fbobject_idnew.txt"
    with open(file_name, encoding="utf8", mode="r") as f_open:
        for count, line in enumerate(f_open):
            if count < total_nums:
                all_data.append(line)
            else:
                break

    for x in range(target_nums):
        random_index = randint(0, total_nums)
        if all_data[random_index] not in target_data:
            target_data.append(all_data[random_index])
            if len(target_data) == target_nums:
                break

    return all_data, target_data

def load_dict_data(total_nums, target_nums):
    """
    从文件中读取数据，以dict的方式返回
    :param total_nums: 读取的数量
    :param target_nums: 需要查询的数据的数量
    """
    all_data = {}
    target_data = []
    file_name = "G:/慕课网课程/AdvancePython/fbobject_idnew.txt"
    with open(file_name, encoding="utf8", mode="r") as f_open:
        for count, line in enumerate(f_open):
            if count < total_nums:
                all_data[line] = 0
            else:
                break
    all_data_list = list(all_data)
    for x in range(target_nums):
        random_index = randint(0, total_nums-1)
        if all_data_list[random_index] not in target_data:
            target_data.append(all_data_list[random_index])
            if len(target_data) == target_nums:
                break

    return all_data, target_data

def find_test(all_data, target_data):
    #测试运行时间
    test_times = 100
    total_times = 0
    import time
    for i in range(test_times):
        find = 0
        start_time = time.time()
        for data in target_data:
            if data in all_data:
                find += 1
        last_time = time.time() - start_time
        total_times += last_time
    return total_times/test_times


if __name__ == "__main__":
    # 测试list和dict的性能
    all_data, target_data = load_list_data(10000, 1000)
    # all_data, target_data = load_list_data(100000, 1000)
    # all_data, target_data = load_list_data(1000000, 1000)


    # all_data, target_data = load_dict_data(10000, 1000)
    # all_data, target_data = load_dict_data(100000, 1000)
    # all_data, target_data = load_dict_data(1000000, 1000)
    last_time = find_test(all_data, target_data)
    print(last_time)


'''
    结论：
        1.dict查找的性能远大于list；
        2.在list中随着list增大，查找时间会越来越大；
        而dict不会随着dict增大而增大；
        3.哈希表的初始；
        4.dict的key或者set的值   都必须是可以hash的
        5.不可变对象都是可hash的, str, frozenset, tuple
        6.dict的内存花销大，但是查询速度快，自定义的对象或者python内部的对象都是dict包装的
        7.dict的存储顺序和元素添加顺序有关
        8.添加数据可能改变已有数据的顺序，小于1/3就会重新申请空间,数据映射位置会变化;
'''