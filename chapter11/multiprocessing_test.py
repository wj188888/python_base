# -- coding:utf-8 --
import os
import time
# from concurrent.futures import ProcessPoolExecutor
# multiprocessing比ProcessPoolExecutor更加底层


# fork会新建子进程，fork只能用于linux/unix下的
# pid = os.fork()
# print("boody")
# if pid == 0:
#     print(f'子进程{os.getpid()}, 父进程是：{os.getppid()}')
# else:
#     print(f'我是父进程：{pid}')
#
# time.sleep(2)

import multiprocessing
import time
# 多进程编程
def get_html(n):
    time.sleep(n)
    print("sub_progress success")
    return n

# class MyProgress(multiprocessing.Process):
#     def run(self):

if __name__ == '__main__':
    # progress = multiprocessing.Process(target=get_html, args=(2,))
    # print(progress.pid)
    # progress.start()
    # # 在start后才有pid
    # print(progress.pid)
    # progress.join()
    # print("main progress end")
    # print(progress.pid)

    # 使用进程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(get_html, args=(3,))
    #
    # # 等待所有任务完成,在执行join前一定要关闭close，不让其他线程进来
    # pool.close()
    # pool.join()
    # print(result.get())

    # imap
    # for result in pool.imap(get_html, [1, 5, 3]):
    #     print(f'{result} sleep success')

    # 谁先完成就先把谁打印出来
    for result in pool.imap_unordered(get_html, [1, 5, 3, 10, 9]):
        print(f'{result} sleep success')
