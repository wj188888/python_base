#
class User:
    # 新式类，在生成User前加逻辑

    def __new__(cls, *args, **kwargs):
        print("in new")
        return super(User, self).__new__(cls)
    '''
        new 是用来控制对象的生成过程， 在对象生成之前使用
        init 是用来完善对象的
        如果new方法不返回对象， 则不会调用init函数
            return super(User, self).__new__(cls)
        上边这个语句就是调用了对象，所以才会调用init内容的
    '''
    def __init__(self, name):
        print("in init")
        self.name = name


if __name__ == '__main__':
    user = User("body")