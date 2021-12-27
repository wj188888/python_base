# -- coding:utf-8 --
# 对于io操作来说，多线程和多进程性能差别不大
# 通过Thread实例化
import threading
import time


def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")

def get_detail_url(url):
    print("get detail html started")
    time.sleep(4)
    print("get detail html end")

if __name__ == '__main__':
    thread1 = threading.Thread(target=get_detail_html, args=("",))
    thread2 = threading.Thread(target=get_detail_url, args=("",))
    start_time = time.time()
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)   # setDaemon是守护线程
    thread1.start()
    thread2.start()
    enter = '\n'

    # 现在的需求是，等子线程执行完成后，再执行主进程
    thread1.join()
    thread2.join()

    # 运行时间是我们两个线程的最大时间，

    # 当主线程退出的时候，子线程kill掉，这是主线程
    print(f'{enter}last time: {round(time.time() - start_time,2)}')