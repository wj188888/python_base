# -- coding:utf-8 --
import threading
from threading import Lock, RLock # 可重入的锁

# 获取锁和释放锁会花费很多时间
# RLock
# 在同一线程里面，可以连续调用多次acquire,一定要注意acquire的次数要和release的次数相同
total = 0
lock = RLock()
def add():
    global lock
    global total
    for i in range(1000000):
        # 获取锁，然后这个锁还是要释放掉
        lock.acquire()
        lock.acquire()
        total += 1
        # 一定要释放掉，不然代码无法释放
        lock.release()
        lock.release()

def desc():
    global lock
    global total
    for i in range(1000000):
        # 加上后lock就是线程同步
        lock.acquire()
        total -= 1
        lock.release()
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

def add1(a):
    a += 1

def desc(a):
    a -= 1

'''
    1.load a
    2.load 1
    3. +
    4.赋值给a
'''


# import dis
# print(dis.dis(add1))
# print(dis.dis(desc))
thread1.join()
thread2.join()
print(total)

''':cvar
    1.用锁会影响性能
    2.用锁容易引起死锁
        互相等待，然后你的就是
'''
''':cvar
    A(a,b)
    acquire(a)
    acquire(b)
    
    B(a,b)
    acquire(b)
    acquire(a)
'''