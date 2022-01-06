# -- coding:utf-8 --
# 装饰函数的装饰工厂,带参数的装饰器
import inspect

def type_assert(*ty_args, **ty_kwargs):
    '''带参数的装饰器'''
    ''':cvar
        带参数的装饰器，也就是根据参数定制化一个装饰器，可以看成生产装饰器的工厂
        每次调用type_assert,返回一个特定的装饰器，然后用他去修饰其他的函数
    '''
    def decorator(func):

        # A...
        # 提取函数的签名
        func_sig = inspect.signature(func)
        bind_type = func_sig.bind_partial(*ty_args, **ty_kwargs).arguments
        def wrap(*args, **kwargs):
            # B...
            for name, obj in func_sig.bind(*args, **kwargs).arguments.items():
                type_ = bind_type.get(name)
                if type_:
                    if not isinstance(obj, type_):
                        raise TypeError('%s must be %s' % (name, type_))
            return func(*args, **kwargs)
        return wrap
    return decorator

@type_assert(int, list, str)
def f(a, b, c):
    pass

if __name__ == '__main__':
    # f_sig = inspect.signature(f)
    # print(f_sig.parameters)
    # pa = f_sig.parameters['a']
    # print(pa.name)
    # print(pa.kind)
    # print(pa.default)
    #
    # ba = f_sig.bind(int, int, str)
    # print(ba.arguments)
    # print(ba.arguments['a'])
    # 绑定
    print(f(5, [], 'abc'))