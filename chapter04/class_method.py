class Date:
    # 构造函数
    def __init__(self, year, month, day):
        #定义年月日
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        #明天 在今天的日期上加1
        self.day += 1

    # 静态方法
    @staticmethod
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))

    @staticmethod
    def valid_str(date_str):
        year, month, day = tuple(date_str.split("-"))
        if int(year) > 0:
            return True
        else:
            return False




    @classmethod
    def from_string(cls, date_str):
        '''
        self是实例对象，而cls是类对象本身
        :return:
        '''
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))


    def __str__(self):
        enter = '/'
        return f"{self.year}{enter}{self.month}{enter}{self.day}"

if __name__ == '__main__':
    # new_day = Date(2018, 10, 22)
    # new_day.tomorrow()
    # print(new_day)
    date_str = "2018-12-31"

    # staticmethod完成初始化
    new_day = Date.parse_from_string(date_str)
    print(new_day)

    # 用classmethod来完成初始化
    new_day = Date.from_string(date_str)
    print(new_day)
    print(Date.valid_str(date_str))