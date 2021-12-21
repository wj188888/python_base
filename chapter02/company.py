# -- coding:utf-8 --
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    # 魔法函数
    def __getitem__(self, item):
        return self.employee[item]

    # 获取类得长度
    def __len__(self):
        return len(self.employee)

company = Company(["tom", "bob", "jane"])

# 进行切片操作
company1 = company[:1]
for em in company1:
    print(em)

# 打印长度
print(len(company))