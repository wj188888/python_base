# 闭包函数
def sort_pri(value, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    value.sort(key=helper)


if __name__ == '__main__':
    group = ['apple', 'origin']
    sort_pri('apple', group)