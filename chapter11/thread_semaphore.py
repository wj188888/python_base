# -- coding:utf-8 --
# Semaphore 是用于控制进入数量的锁
# 文件丶读丶写，写一般只是用于一个线程写，读可以应许有多个

# 做爬虫，也要防止反爬
import threading
import time
from queue import Queue

class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("got html text success\n")
        self.sem.release()

class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()
            html_thread = HtmlSpider(f'https://baidu.com/{i}',self.sem)
            html_thread.start()

if __name__ == '__main__':
    sem = threading.Semaphore(2)
    url_producer = UrlProducer(sem)
    url_producer.start()