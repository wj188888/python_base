# -- coding:utf-8 --
# try except finally

def ext_try():
    try:
        f_read = open("./demofile/wj.txt")
        print("code started")
        raise KeyError
        return 1
    except KeyError as e:
        print("Key error")
        return 2
    # 在没有捕获到的异常
    else:
        print("others error")
        return 3
    finally:
        # 前面代码运行不运行都会运行finally中
        print("finally")
        f_read.close()
        # return 4
# 上下文管理器协议
class Sample():
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def do_something(self):
        print("doing something")
'''
    执行属性是，with先去调用__enter__，再去调用with语句，再去调用__exit__这个魔法函数
'''
if __name__ == '__main__':
    result = ext_try()
    print(result)