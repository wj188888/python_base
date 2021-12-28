# -- coding:utf-8 --
# 线程间通信

import threading
import time

from . import variables
# 这样做的话如果线程对变量修改可能这个模块是无感知的
# from chapter11.variables import detail_url_list

def get_detail_html():
    # 爬起文章详情页'
    detail_url_list = variables.detail_url_list
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()
            # for url in detail_url_list:
            print("get detail html started")
            time.sleep(2)
            print("get detail html end")

def get_detail_url(detail_url_list):
    # 爬取文章列表页
    while True:
        print("get detail html started")
        time.sleep(4)
        for i in range(20):
            detail_url_list.append(f'http://projectsedu.com/{i}')
        print("get detail html end")

# 线程的通信方式-共享变量,设置全局变量



if __name__ == '__main__':
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_list, ))
    for _ in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_list, ))
        html_thread.start()
    # thread_detail_url1 = threading.Thread(target=get_detail_html)
    # thread_detail_url2 = threading.Thread(target=get_detail_html)

    # thread2 = GetDetailUrl("get_detail_url")

    # thread1 = threading.Thread(target=get_detail_html, args=("",))
    # thread2 = threading.Thread(target=get_detail_url, args=("",))
    start_time = time.time()
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)   # setDaemon是守护线程
    # thread1.start()
    # thread2.start()
    enter = '\n'

    # 现在的需求是，等子线程执行完成后，再执行主进程
    # thread1.join()
    # thread2.join()

    # 运行时间是我们两个线程的最大时间，

    # 当主线程退出的时候，子线程kill掉，这是主线程
    print(f'{enter}last time: {round(time.time() - start_time,6)}')

