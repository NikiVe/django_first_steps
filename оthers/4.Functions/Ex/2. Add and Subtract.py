def sum_num(a, b):
    res = a + b
    return res


def sub_num(a, b):
    res = a - b
    return res


def sum_sub_num(a, b, c):
    res = sub_num(sum_num(a, b), c)
    return res


a = int(input())
b = int(input())
c = int(input())
print(sum_sub_num(a, b, c))
