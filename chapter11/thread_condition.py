# -- coding:utf-8 --
from threading import Condition

import threading

# 条件变量， 用于复杂的线程间同步
# class XiaoAi(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name="小爱")
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print(f'{self.name}: 在')
#         self.lock.release()
#
# class TianMao(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name="天猫精灵")
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print(f'{self.name}: 小爱同学')
#         self.lock.release()

class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print(f'{self.name}: 在')
            self.cond.notify()

            self.cond.wait()
            print(f'{self.name}: 好啊')
            self.cond.notify()

            self.cond.wait()
            print(f'{self.name}: 君住长江尾')
            self.cond.notify()

            self.cond.wait()
            print(f'{self.name}: 供应长江水')
            self.cond.notify()

            self.cond.wait()
            print(f'{self.name}: 我在长江头')
            self.cond.notify()

            self.cond.wait()
            print(f'{self.name}: 此恨何时有')
            self.cond.notify()

            self.cond.wait()
            print(f'{self.name}: 定不负相思意')
            self.cond.notify()

class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="天猫精灵")
        self.cond = cond

    def run(self):
        with self.cond:
            print(f'{self.name}: 小爱同学')
            self.cond.notify()
            self.cond.wait()

            print(f'{self.name}: 我们来对古诗吧')
            self.cond.notify()
            self.cond.wait()

            print(f'{self.name}: 我在长江头')
            self.cond.notify()
            self.cond.wait()

            print(f'{self.name}: 日日思君不见君')
            self.cond.notify()
            self.cond.wait()

            print(f'{self.name}: 此水几时休')
            self.cond.notify()
            self.cond.wait()

            print(f'{self.name}: 只愿君心似我心')
            self.cond.notify()
            self.cond.wait()

# 通过condition完成协同协读



if __name__ == '__main__':
    cond = threading.Condition()
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)

    # 启动顺序，一定要要先
    # 在调用with之后才能调用wait或者notify()方法
    # condition有两层锁，一把底层锁会在线程调用wait()方法的时候释放，
    # 上面的锁会在每次调用wait的时候分配一把并放入到condition的等待队列中，
    # 等待notify方法的唤醒

    xiaoai.start()
    tianmao.start()
