# encoding:utf-8
# 多进程编程
# 多进程

import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
# 使用多进程模式
from concurrent.futures import ProcessPoolExecutor


# def fib(n):


#     if n <= 2:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# # print(fib(3))
# if __name__ == '__main__':
#     with ThreadPoolExecutor(3) as executor:
#         all_task = [executor.submit(fib, (num)) for num in range(25,40)]
#         start_time = time.time()
#         for future in as_completed(all_task):
#             data = future.result()
#             print(f'get {data} page')
#         print(f'last time is: {time.time() - start_time}')

# 2.对于io操作来说，多线程优于多进程
def random_sleep(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    with ThreadPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, (num)) for num in [2]*30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print(f'get {data} page')
        print(f'last time is: {time.time() - start_time}')