# -- coding:utf-8 --
import time
from multiprocessing import Process, Queue, Pool, Manager ,Pipe
# from queue import Queue

# def producer(a):
#     a += 1
#     # queue.put("a")
#     time.sleep(2)
#
# def consumer(a):
#     time.sleep(2)
#     print(a)
#
# if __name__ == '__main__':
#     # 多进程不能使用来自于queue的Queue，from queue import Queue，而要是用multiprocessing
#     # 的Queue
#     a = 1
#     queue = Queue(10)
#     my_producer = Process(target=producer, args=(a,))
#     my_consumer = Process(target=consumer, args=(a,))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()


# multiprocessing中的deque不能用于pool进程池
# 我们的pool中的进程建通信需要使用Manager中的queue,Manager实例化才能是queue

# def producer(a):
#     a += 1
#     # queue.put("a")
#     time.sleep(2)
#
# def consumer(a):
#     time.sleep(2)
#     print(a)
#
# if __name__ == '__main__':
#     queue = Manager().Queue(10)
#     pool = Pool(2)
#
#     pool.apply_async(producer, args=(queue,))
#     pool.apply_async(consumer, args=(queue,))



# +======================
# 通过Pipe进行进程间通信
# pipe的性能高于queue


# def producer(pipe):
#     pipe.send("bobby")
#
# def consumer(pipe):
#     print(pipe.recv())
#
# if __name__ == '__main__':
#     receive_pipe, send_pipe = Pipe()
#     # Pipe只能使用于两个进程
#     my_producer = Process(target=producer, args=(send_pipe,))
#     my_consumer = Process(target=consumer, args=(receive_pipe,))
#
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()


def add_data(p_dict, key, value):
    p_dict[key] = value

if __name__ == '__main__':
    progcess_dict = Manager().dict()

    first_progress = Process(target=add_data, args=(progcess_dict, "boddy1", 22))
    second_progress = Process(target=add_data, args=(progcess_dict, "boddy2", 25))
    first_progress.start()
    second_progress.start()
    first_progress.join()
    second_progress.join()