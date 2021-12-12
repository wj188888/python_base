def dict_get_func():
    # 定义一个字丶
    counters = {
        'name': 'wj',
        'age': 10,
        'sex': '男'
    }
    key = 'num'
    # if key in counters:
    #     count = counters[key]
    # else:
    #     count = 0
    # print(type(count))

    # 换成另外一种写法
    count = counters.get(key, 0)
    counters[key] = count + 1
    print(counters[key])

    for i, j in counters.items():
        print(i, j)
    '''
        counters.get(key, 0)该方法：查看字典的是否包含某一key值，如果没有找到，添加一个key，第二个参数设置该key默认值
    '''

# 案例二
# 使用defaultdict处理内部状态中缺失的元素，而不要用setdefalut

def default_dict():
    # 场景：
    '''
        笔者要记录自己去过哪些国家，还记录每个国家到过哪些城市
    :return:
    '''
    visits = {
        'japan': {'tokey', 'poton', 'dalong'},
        'afrin': {'hongkong', 'zanbiya'}
    }
    pass

# 不要把函数返回的多个数值拆分到三个以上的变量中,
def return_result(numbers):
    mininum = min(numbers)
    maxinum = max(numbers)
    return mininum, maxinum