# -- coding:utf-8 --
# 这个包是做线程池和进程池编程的,多进程和多线程很容易


# 线程池，为什么要用线程池？
# 不止是对线程数量的控制

# 现在主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值
# 当一个线程完成的时候我们主线程立即知道
# fetures 可以让多线程和多进程编码接口一致
import time
from concurrent import futures
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
from concurrent.futures import Future

# 未来对象，task的返回容器
# from concurrent.futures import Future 的设计理念很好，是异步编程的核心




def get_html(times):
    time.sleep(times)
    print(f'get page {times} success')
    return times

executor = ThreadPoolExecutor(max_workers=2)
# 通过submit函数提交执行的函数到线程池中
# task1是返回的fetures对象
# task1 = executor.submit(get_html, (3))
# task2 = executor.submit(get_html, (2))

# 要获取已经成功的task的返回
urls = [3, 2, 4]
all_task = [executor.submit(get_html, (url)) for url in urls]
# wait(all_task, return_when=FIRST_COMPLETED)
# print("main")
for future in as_completed(all_task):
    data = future.result()
    print(f'get {data} page')

# 通过executor获取已经完成的task,其中map是按照url的顺序进行完成的
for data in executor.map(get_html, urls):
    print(f'get {data} page')


# 判定函数是否执行成功,done方法用于判定某个任务是否完成
# print(task1.done())
# time.sleep(1)
# 取消只要在没有开始之前可以取消的，其他时候是取消不了的，换句话说就是运行中和运行后不应许取消的
# print(task2.cancel())
# print(task2.done())
# time.sleep(2.1)
# print(task1.done())
# print(task2.done())

# result方法可以获取task的执行结果
# print(task1.result())
# print(task2.result())