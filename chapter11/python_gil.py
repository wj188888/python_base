# gil global interpreter lock (cpython)
# python 中一个线程对应于c语言中的一个线程
# gil使得，同一时刻只有一个线程运行在一个cpu上执行字节码,无法将多个线程映射到多cpu上
# gil在某些情况可以释放的

'''
gil释放：
    1.gil会根据执行的字节码行数以及时间片释放gil
    2.遇到IO操作时候会主动释放
'''




# import dis
# def add(a):
#     a = a + 1
#     return a
#
# print(dis.dis(add))


import threading


total = 0
def add():
    # dosomething
    # io操作
    global total
    for i in range(1000000):
        total += 1

def desc():
    global total
    for i in range(1000000):
        total -= 1
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)