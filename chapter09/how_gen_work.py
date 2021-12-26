# 生成器的原理

# python中函数的工作原理
'''

'''
import dis
import inspect


frame = None

def foo():
    bar()
def bar():
    global frame
    frame = inspect.currentframe()

'''
    python.exe会用一个叫做PyEval_EvalFramEx(C语言函数)去执行的foo函数
    首先创建一个栈帧
    python一切都是对象，栈帧对象，字节码对象
    当foo调用子函数bar，又会创建一个栈帧，
    所有的栈帧都是放在堆的内存上，这就决定了栈帧可以独立于调用者存在；
'''



foo()
print(frame.f_code.co_name)
caller_frame = frame.f_back
print(caller_frame.f_code.co_name)

def gen_func():
    yield 2
    name = "wangjie"
    yield 3
    age = 30
    return "imooc"
if __name__ == '__main__':
    gen = gen_func()
    print(gen)
    print(dis.dis(gen))
    print(gen.gi_frame.f_lasti)
    print(gen.gi_frame.f_locals)
    next(gen)
    print(gen.gi_frame.f_lasti)
    print(gen.gi_frame.f_locals)
    next(gen)
    print(gen.gi_frame.f_lasti)
    print(gen.gi_frame.f_locals)